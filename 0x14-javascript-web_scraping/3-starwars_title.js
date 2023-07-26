#!/usr/bin/node

const request = require('request');

/**
 * Prints the title of a Star Wars movie based on the episode number.
 * @param {number} movieId - The episode number of the movie to retrieve.
 */
function printStarWarsMovieTitle (movieId) {
  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  request.get(apiUrl, (error, response, body) => {
    if (error) {
      console.error(error);
    } else if (response.statusCode === 200) {
      const movieData = JSON.parse(body);
      console.log(movieData.title);
    } else {
      console.error(`Error: Movie with ID ${movieId} not found.`);
    }
  });
}

// Check if the movie ID argument is provided.
if (process.argv.length < 3) {
  console.error('Usage: node 3-starwars_title.js <movie-id>');
} else {
  // The first argument (index 2) contains the movie ID.
  const movieId = process.argv[2];
  printStarWarsMovieTitle(movieId);
}
