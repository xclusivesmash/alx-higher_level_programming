#!/usr/bin/env node

/* displays a value from a fetch request */
const $ = window.$;
const URL = 'https://fourtonfish.com/hellosalut/?lang=fr';
$.get(URL, function (data) {
  const hello_data = data.hello;
  $('DIV#hello').text(hello_data);
});
