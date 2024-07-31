#!/usr/bin/node
// Import the filesystem module
const fs = require('fs');

// Get the file path and content from command-line arguments
const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, 'utf-8', (error) => {
  if (error) {
    console.error('Error writing to file:', error);
  }
});
