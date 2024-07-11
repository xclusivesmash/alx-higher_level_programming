#!/usr/bin/node

function add (a, b) {
  return (a + b);
}

const argv = process.argv;
const one = parseInt(argv[2]);
const two = parseInt(argv[3]);
console.log(add(one, two));
