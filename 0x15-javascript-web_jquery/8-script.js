/* fetches and lists titles of movies */
let URL = 'https://swapi.co/api/films/?format=json';
$.get(URL, function (data) {
  let movies = data.results;
  for (let movie of movies) {
    $('ul#list_movies').append(`<li>${movie.title}</li>`);
  }
});
