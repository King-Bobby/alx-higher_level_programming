#!/usr/bin/node

const request = require('request');

/**
 * Prints the number of movies where the character "Wedge Antilles" is present.
 * @param {string} apiUrl - The API URL of the Star Wars API films endpoint.
 */
function countMoviesWithWedgeAntilles (apiUrl) {
  const characterId = 18;
  let count = 0;

  request.get(apiUrl, (error, response, body) => {
    if (error) {
      console.error(error);
    } else if (response.statusCode === 200) {
      const responseData = JSON.parse(body);
      const filmsData = responseData.results;

      filmsData.forEach((film) => {
        const characters = film.characters;
        if (characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
          count++;
        }
      });
      console.log(count);
    } else {
      console.error('Error: Failed to fetch data from the Star Wars API.');
    }
  });
}

// Check if the API URL argument is provided.
if (process.argv.length < 3) {
  console.error('Usage: node 4-starwars_count.js <API-URL>');
} else {
  // The first argument (index 2) contains the API URL.
  const apiUrl = process.argv[2];
  countMoviesWithWedgeAntilles(apiUrl);
}
