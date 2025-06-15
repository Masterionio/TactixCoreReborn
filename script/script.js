// script.js — Frontend logic for TactixCore UI

async function loadConfig() {
  try {
    // Try to fetch config.yaml or config.json if hosted publicly (simulate here)
    const response = await fetch('/config/config.yaml');
    if (!response.ok) throw new Error('Config not found');

    const text = await response.text();
    console.log('Config loaded:', text);
    // Parse YAML or JSON as needed — here we just log
  } catch (error) {
    console.error('Failed to load config:', error);
  }
}

function initUI() {
  document.getElementById('app-title').textContent = 'TactixCore Reborn Dashboard';
  loadConfig();
}

window.onload = initUI;
