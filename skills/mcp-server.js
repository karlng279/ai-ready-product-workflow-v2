#!/usr/bin/env node
'use strict';

const { McpServer } = require('@modelcontextprotocol/sdk/server/mcp.js');
const { StdioServerTransport } = require('@modelcontextprotocol/sdk/server/stdio.js');
const { spawnSync } = require('child_process');
const { z } = require('zod');
const fs = require('fs');
const path = require('path');

const SKILLS_DIR = __dirname;

function parseSkillFrontmatter(content) {
  const match = content.match(/^---\n([\s\S]*?)\n---/);
  if (!match) return { name: null, description: '' };
  const block = match[1];
  const name = (block.match(/^name:\s*(.+)$/m) || [])[1]?.trim();
  const description = (block.match(/^description:\s*(.+)$/m) || [])[1]?.trim() || '';
  return { name, description };
}

const skills = fs.readdirSync(SKILLS_DIR)
  .filter(d => {
    try { return fs.statSync(path.join(SKILLS_DIR, d)).isDirectory(); } catch { return false; }
  })
  .map(d => {
    const skillPath = path.join(SKILLS_DIR, d, 'SKILL.md');
    if (!fs.existsSync(skillPath)) return null;
    const content = fs.readFileSync(skillPath, 'utf8');
    const { name, description } = parseSkillFrontmatter(content);
    return { name: name || d, folderName: d, skillPath, description, content };
  })
  .filter(Boolean);

const server = new McpServer({ name: 'ai-ready-workflow', version: '0.1.2' });

// ── Resources ──────────────────────────────────────────────────────────────

for (const skill of skills) {
  server.resource(
    skill.name,
    `skill://${skill.name}`,
    { mimeType: 'text/markdown', description: skill.description },
    async () => ({ contents: [{ uri: `skill://${skill.name}`, text: skill.content }] })
  );
}

// ── Tools ──────────────────────────────────────────────────────────────────

server.tool('list_skills', {}, async () => ({
  content: [{
    type: 'text',
    text: skills.map(s => `- **${s.name}**: ${s.description}`).join('\n')
  }]
}));

server.tool(
  'get_skill',
  { name: z.string().describe('Skill name e.g. po-brief-to-prd') },
  async ({ name }) => {
    const skill = skills.find(s => s.name === name || s.folderName === name);
    if (!skill) {
      return { content: [{ type: 'text', text: `Skill "${name}" not found. Call list_skills to see available options.` }] };
    }
    return { content: [{ type: 'text', text: skill.content }] };
  }
);

server.tool(
  'search_ui_ux',
  {
    query: z.string().describe('Design system search query'),
    domain: z.enum(['style', 'color', 'chart', 'landing', 'product', 'ux', 'typography']).optional(),
    stack: z.enum(['html-tailwind', 'react', 'nextjs', 'shadcn', 'vue', 'svelte', 'flutter', 'swiftui', 'react-native', 'astro']).optional(),
  },
  async ({ query, domain, stack }) => {
    const scriptPath = path.join(SKILLS_DIR, 'ui-ux-pro-max', 'scripts', 'search.py');
    if (!fs.existsSync(scriptPath)) {
      return { content: [{ type: 'text', text: 'Python search script not found at ui-ux-pro-max/scripts/search.py' }] };
    }
    const args = [scriptPath, query];
    if (domain) args.push('--domain', domain);
    if (stack) args.push('--stack', stack);
    const result = spawnSync('python3', args, { encoding: 'utf8', cwd: SKILLS_DIR });
    if (result.error) return { content: [{ type: 'text', text: `Error: ${result.error.message}` }] };
    return { content: [{ type: 'text', text: result.stdout || result.stderr || 'No results.' }] };
  }
);

// ── Prompts ────────────────────────────────────────────────────────────────

for (const skill of skills) {
  server.prompt(
    skill.name,
    { context: z.string().optional().describe('Your input, brief, or context for this skill') },
    ({ context }) => ({
      messages: [{
        role: 'user',
        content: {
          type: 'text',
          text: skill.content + (context ? `\n\n---\n\n## My Input\n\n${context}` : '')
        }
      }]
    })
  );
}

// ── Start ──────────────────────────────────────────────────────────────────

const transport = new StdioServerTransport();
server.connect(transport);
