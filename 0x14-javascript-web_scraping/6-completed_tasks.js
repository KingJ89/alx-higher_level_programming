#!/usr/bin/node

// Import the request module
const request = require('request');
const apiUrl = process.argv[2];
const dictionary = {};

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    data.forEach(result => {
      if (result.completed) {
        const userId = result.userId;
        dictionary[userId] = (dictionary[userId] || 0) + 1;
      }
    });
    console.log(dictionary);
  }
});
