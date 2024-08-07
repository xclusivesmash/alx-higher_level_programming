#!/usr/bin/env node
/* fetches and lists titles of movies */
const $ = window.$;
const URL = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.get(URL, function (data) {
  const res = data.results;
  $.each(res, function (key, value) {
    $('UL#list_movies').append('<li>' + value.title + '</li>');
  });
});
