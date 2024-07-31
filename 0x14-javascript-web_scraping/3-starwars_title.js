#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

// Construct the API URL with the provided movie ID
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make an HTTP GET request to the API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const content = JSON.parse(body);
    console.log(content.title);
  }
});
