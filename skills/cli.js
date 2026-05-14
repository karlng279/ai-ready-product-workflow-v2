#!/usr/bin/env node
// cli.js — AI-Ready Product Workflow CLI entry point
// Called by: npx ai-ready-workflow install [target-dir]

'use strict';

const { execSync } = require('child_process');
const path = require('path');
const fs = require('fs');

const SCRIPT_DIR = __dirname;
const command = process.argv[2];
const targetDir = process.argv[3] || process.cwd();

function printUsage() {
  console.log('');
  console.log('  AI-Ready Product Workflow');
  console.log('');
  console.log('  Usage:');
  console.log('    npx ai-ready-workflow install              # install into current directory');
  console.log('    npx ai-ready-workflow install <target>     # install into <target>');
  console.log('    npx ai-ready-workflow mcp                  # start MCP server for Claude Desktop');
  console.log('');
  console.log('  What it does:');
  console.log('    • Copies 16 skills to <target>/.agent/skills/');
  console.log('    • Copies agent entry points: AGENTS.md, GEMINI.md, .cursorrules, GETTING_STARTED.md');
  console.log('    • Appends the skill registry to <target>/CLAUDE.md (if it exists)');
  console.log('');
  console.log('  Supports: Claude Code, OpenAI Codex, Gemini Code Assist, Cursor');
  console.log('');
}

if (!command || command === 'help' || command === '--help' || command === '-h') {
  printUsage();
  process.exit(0);
}

if (command === 'mcp') {
  require('./mcp-server.js');
  return;
}

if (command !== 'install') {
  console.error(`  Unknown command: "${command}"`);
  printUsage();
  process.exit(1);
}

// Resolve target directory
const resolvedTarget = path.resolve(targetDir);
if (!fs.existsSync(resolvedTarget)) {
  console.error(`  Target directory does not exist: ${resolvedTarget}`);
  process.exit(1);
}

// Dispatch to platform-appropriate installer
if (process.platform === 'win32') {
  const ps1 = path.join(SCRIPT_DIR, 'install.ps1');
  execSync(
    `powershell -ExecutionPolicy Bypass -File "${ps1}" "${resolvedTarget}"`,
    { stdio: 'inherit' }
  );
} else {
  const sh = path.join(SCRIPT_DIR, 'install.sh');
  fs.chmodSync(sh, '755');
  execSync(`bash "${sh}" "${resolvedTarget}"`, { stdio: 'inherit' });
}
