#!/usr/bin/node

const request = require('request');
const fs = require('fs');

/**
 * Gets the contents of a webpage and stores it in a file.
 * @param {string} url - The URL to request.
 * @param {string} filePath - The file path to store the body response.
 */
function getRequestAndStoreToFile(url, filePath) {
  request.get(url, (error, response, body) => {
    if (error) {
      console.error(error);
    } else if (response.statusCode === 200) {
      fs.writeFile(filePath, body, 'utf-8', (err) => {
        if (err) {
          console.error(err);
        }
      });
    } else {
      console.error(`Error: Failed to fetch data from ${url}. Status Code: ${response.statusCode}`);
    }
  });
}

// Check if both the URL and file path arguments are provided.
if (process.argv.length < 4) {
  console.error('Usage: node 5-request_store.js <URL> <file-path>');
} else {
  // The first argument (index 2) contains the URL to request.
  const url = process.argv[2];

  // The second argument (index 3) contains the file path to store the response.
  const filePath = process.argv[3];

  getRequestAndStoreToFile(url, filePath);
}
