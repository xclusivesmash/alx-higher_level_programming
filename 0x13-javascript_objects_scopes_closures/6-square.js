#!/usr/bin/node

const SquareOld = require('./5-square');

/*
* Square class definition
*/
class Square extends SquareOld {
  charPrint (c) {
    const mSymb = c === undefined ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      let m = '';
      for (let j = 0; j < this.width; j++) {
        m = m + mSymb;
      }
      console.log(m);
    }
  }
}

module.exports = Square;
