#!/usr/bin/node

function factorial (n) {
  if (!n || n === 0 || n === 1) {
    return (1);
  }
  return (n * factorial(n - 1));
}

const argv = process.argv;
const number = parseInt(argv[2]);
console.log(factorial(number));
