#!/usr/bin/node

const argv = process.argv;
const count = parseInt(argv[2]);
if (count) {
  for (let i = 0; i < count; i++) {
    let line = '';
    let n = count;
    while (n > 0) {
      line = line + 'X';
      n--;
    }
    console.log(line);
  }
} else {
  console.log('Missing size');
}
