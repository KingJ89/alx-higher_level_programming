#!/usr/bin/node

// Import the filesystem module
const fs = require('fs');

const filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', (error, data) => {
  if (error) {
    console.error('Error reading file:', error);
  return;
  }
    console.log(data);
});
