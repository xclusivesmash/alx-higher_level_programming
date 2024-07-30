#!/usr/bin/node
/* display the status code of a GET request. */

const request = require('request');
// url in 2nd arg of agrv.
const url = process.argv[2];
// query using url.
request.get(url, function (error, response) {
  if (error) {
    console.log(error);
  } else {
    console.log('code:' + ' ' + response.statusCode);
  }
});
