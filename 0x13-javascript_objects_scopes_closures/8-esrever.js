#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];
  let i = list.length;
  while (i > 0) {
    newList.push(list[i - 1]);
    i = i - 1;
  }
  return newList;
};
