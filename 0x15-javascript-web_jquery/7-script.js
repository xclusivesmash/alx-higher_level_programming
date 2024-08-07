#!/usr/bin/env node
/* fetches an attribite from a url */
const $ = window.$;
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
$.get(url, function (data) {
  $('DIV#character').text(data.name);
});
