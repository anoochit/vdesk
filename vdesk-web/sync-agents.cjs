const fs = require('fs');
const path = require('path');

// Resolve paths relative to the script's location
const agentsPyPath = path.join(__dirname, '../vdesk-agents/root_agent/agent.py');
const agentsTsPath = path.join(__dirname, 'src/config/agents.ts');

console.log(`Reading agents from: ${agentsPyPath}`);
const agentsPy = fs.readFileSync(agentsPyPath, 'utf8');

// Extract all agent IDs (e.g. name="ops_agent")
const agentIds = [...agentsPy.matchAll(/name=["']([^"']+)["']/g)].map(m => m[1]);
console.log(`Found agent IDs: ${agentIds.join(', ')}`);

console.log(`Updating config at: ${agentsTsPath}`);
let agentsTs = fs.readFileSync(agentsTsPath, 'utf8');

// Parse existing agents to preserve their custom display names and sprites
const existingAgents = {};
const agentPattern = /{\s*["']?agentId["']?\s*:\s*["']([^"']+)["']\s*,\s*["']?name["']?\s*:\s*["']([^"']+)["']\s*,\s*["']?sprite["']?\s*:\s*["']([^"']+)["']\s*}/g;

for (const match of agentsTs.matchAll(agentPattern)) {
    existingAgents[match[1]] = { name: match[2], sprite: match[3] };
}

// Generate the new array content
const newAgentsArrayStr = agentIds.map((id, index) => {
    // Generate a default name (e.g., ops_agent -> Ops)
    let name = id.replace('_agent', '');
    name = name.charAt(0).toUpperCase() + name.slice(1);
    
    // Assign a default sprite based on a random index (0-5)
    const randomSpriteIndex = Math.floor(Math.random() * 6);
    let sprite = `/assets/characters/char_${randomSpriteIndex}.png`;
    
    // Keep existing overrides if the agent already existed
    if (existingAgents[id]) {
        name = existingAgents[id].name;
        sprite = existingAgents[id].sprite;
    }
    
    return `\t{ "agentId" : "${id}", "name" : "${name}", "sprite": "${sprite}" }`;
}).join(',\n');

// Replace the agents array in the TypeScript file
const newAgentsTs = agentsTs.replace(
    /export const agents:\s*Agent\[\]\s*=\s*\[([\s\S]*?)\];/,
    `export const agents: Agent[] = [\n${newAgentsArrayStr}\n];`
);

fs.writeFileSync(agentsTsPath, newAgentsTs, 'utf8');
console.log('Successfully synchronized agents.ts with agents.py!');
