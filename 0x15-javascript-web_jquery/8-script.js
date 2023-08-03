$(function() {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(response, status) {
    if (status === 'success') {
      let movies = response.results;
      for (let index in movies) {
        $('#list_movies').append('<li>' + movies[index].title + '</li>');
      };
    };
  });
})
