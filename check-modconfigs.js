const glob = require('glob');
const fs = require('fs');

// Find all ModConfigs files
const files = glob.sync('ModConfigs/**/*.json');

// Check each file
files.forEach((file) => {
  const data = fs.readFileSync(file);
  const json = JSON.parse(data);
  if (!json[0].mods || !json[0].desc || !json[0].name || !json[0].authors) {
    console.error(`Error in ${file}: JSON object is missing required properties`);
    process.exit(1);
  }
});
