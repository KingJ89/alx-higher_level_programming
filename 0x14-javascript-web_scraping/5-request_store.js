#!/usr/bin/node

// Import required modules
const request = require('request');
const fs = require('fs');

const apiUrl = process.argv[2];
const file = process.argv[3];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    // Write the response body to the file
    fs.writeFile(file, body, 'utf-8', (error) => {
      if (error) {
        console.error(error);
      }
    });
  }
});
