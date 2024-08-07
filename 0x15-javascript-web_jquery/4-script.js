#!/usr/bin/env node
/* toggles the class of header element */
const $ = window.$;
$('div#toggle_header').click(function () {
    $('header').ToggleClass('red');
    $('header').toggleClass('green');
  });
