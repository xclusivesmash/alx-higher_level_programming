#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let i = 0; i < list.length; i++) {
    const number = list[i];
    if (number === searchElement) {
      count = count + 1;
    }
  }
  return count;
};
