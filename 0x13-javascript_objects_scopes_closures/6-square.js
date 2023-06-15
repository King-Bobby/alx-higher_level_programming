#!/usr/bin/node
const ParentSquare = require('./5-square');

class Square extends ParentSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let squareString = '';
    for (let i = 0; i < this.height; i++) {
      squareString += c.repeat(this.width) + '\n';
    }
    console.log(squareString);
  }
}
module.exports = Square;
