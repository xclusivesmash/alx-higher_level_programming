#!/usr/bin/node
/*
 * Description: data types switching.
 */

const number = parseInt(process.argv[2]);
if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${number}`);
}
