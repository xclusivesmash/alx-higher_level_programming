#!/usr/bin/env node
/* updates contents of the header element */
const $ = window.$;
$('DIV#update_header').click(function () {
  $('header').text('New Header!!!');
});
