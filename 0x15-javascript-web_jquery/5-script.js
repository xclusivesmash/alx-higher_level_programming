#!/usr/bin/env node
/* adds a lu tag to element */
$('div#add_item').click(function () {
    let element = '<li>Item</li>';
    $('ul.my_list').append(element);
  });
