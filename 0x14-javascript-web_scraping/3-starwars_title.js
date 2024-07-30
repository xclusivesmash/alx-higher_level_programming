#!/usr/bin/node
/* prints the title of a Star Wars movie */

const request = require('request');
// format url
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
// query using url
request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const content = JSON.parse(body);
    console.log(content.title);
  }
});
