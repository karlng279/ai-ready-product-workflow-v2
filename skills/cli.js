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
  console.log('    npx ai-ready-workflow install-cowork       # install into Claude Desktop Cowork mode');
  console.log('    npx ai-ready-workflow mcp                  # start MCP server for Claude Desktop');
  console.log('');
  console.log('  What it does:');
  console.log('    • install        — copies 16 skills to <target>/.agent/skills/ (Claude Code, Cursor, Codex)');
  console.log('    • install-cowork — copies 16 skills to Claude Desktop Local Agent / Cowork skills folder');
  console.log('    • mcp            — starts the MCP server for Claude Desktop regular chat');
  console.log('');
  console.log('  Supports: Claude Code, Claude Desktop (chat + Cowork), OpenAI Codex, Gemini, Cursor');
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

if (command === 'install-cowork') {
  if (process.platform !== 'darwin') {
    console.error('  install-cowork is only supported on macOS (Claude Desktop for Mac).');
    process.exit(1);
  }
  const sh = path.join(SCRIPT_DIR, 'install.sh');
  fs.chmodSync(sh, '755');
  execSync(`bash "${sh}" --cowork`, { stdio: 'inherit' });
  process.exit(0);
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
