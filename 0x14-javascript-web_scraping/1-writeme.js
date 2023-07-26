#!/usr/bin/node

const fs = require('fs');

/**
 * Writes a string to a file.
 * @param {string} filePath - The path to the file to be written.
 * @param {string} content - The string content to be written to the file.
 */
function writeToFile (filePath, content) {
  fs.writeFile(filePath, content, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
}

// Check if both the file path and content arguments are provided.
if (process.argv.length < 4) {
  console.error('Usage: node 1-writeme.js <file-path> <content-to-write>');
} else {
  // The first argument (index 2) contains the file path.
  const filePath = process.argv[2];

  // The second argument (index 3) contains the content to be written.
  const content = process.argv[3];

  writeToFile(filePath, content);
}
