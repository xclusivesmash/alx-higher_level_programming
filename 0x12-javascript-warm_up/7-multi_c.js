#!/usr/bin/node

const myString = 'C is fun';
const number = parseInt(process.argv[2]);
if (isNaN(number)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < number; i++) {
    console.log(myString);
  }
}
