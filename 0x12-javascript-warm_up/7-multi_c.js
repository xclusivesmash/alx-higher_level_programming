#!/usr/bin/node

const argv = process.argv;
const count = parseInt(argv[2]);
if (count) {
  for (let i = 0; i < count; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
