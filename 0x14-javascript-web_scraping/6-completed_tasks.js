#!/usr/bin/node

const request = require('request');

/**
 * Computes the number of tasks completed by user id.
 * @param {string} apiUrl - The API URL to request.
 */
function countCompletedTasksByUserId(apiUrl) {
  const completedTasksByUser = {};

  request.get(apiUrl, (error, response, body) => {
    if (error) {
      console.error(error);
    } else if (response.statusCode === 200) {
      const tasks = JSON.parse(body);

      tasks.forEach((task) => {
        if (task.completed) {
          const userId = task.userId;
          completedTasksByUser[userId] = (completedTasksByUser[userId] || 0) + 1;
        }
      });

      console.log(completedTasksByUser);
    } else {
      console.error('Error: Failed to fetch data from the API.');
    }
  });
}

// Check if the API URL argument is provided.
if (process.argv.length < 3) {
  console.error('Usage: node 6-completed_tasks.js <API-URL>');
} else {
  // The first argument (index 2) contains the API URL.
  const apiUrl = process.argv[2];
  countCompletedTasksByUserId(apiUrl);
}
