#!/usr/bin/env node
/* updates content and responds with a callback function */
const $ = window.$;
$('div#red_header').click(function () {
    $('header').css('color', '#FF0000');
  });
