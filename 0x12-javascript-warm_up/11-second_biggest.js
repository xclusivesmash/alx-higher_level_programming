#!/usr/bin/node

const myArray = process.argv.slice(2);
function secondLargest (array) {
  if (array.length < 2) {
    return (0);
  } else {
    array.sort((a, b) => a - b);
    array.pop(); /* pop the largest first */
    /* the 2nd pop gives out 2nd largest */
    return (array.pop());
  }
}
console.log(secondLargest(myArray));
