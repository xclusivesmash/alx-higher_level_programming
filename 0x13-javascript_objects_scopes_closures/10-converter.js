#!/usr/bin/node

exports.converter = function (base) {
  function baseConversion (number) {
    return number.toString(base);
  }
  return baseConversion;
};
