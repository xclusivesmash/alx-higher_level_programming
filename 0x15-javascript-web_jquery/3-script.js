#!/usr/bin/env node
/* adds a class to the header element */
const $ = window.$;
$('div#red_header').click(function () {
    $('header').addClass('red');
  });
