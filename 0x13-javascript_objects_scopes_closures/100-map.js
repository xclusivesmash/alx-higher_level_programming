#!/usr/bin/node

const myList = require('./100-data').list;
const newList = myList.map((x, index) => (x * index));

console.log(myList);
console.log(newList);
