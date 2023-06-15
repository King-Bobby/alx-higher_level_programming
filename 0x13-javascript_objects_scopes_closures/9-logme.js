#!/usr/bin/node
let numArgumentPrinted = 0;

exports.logMe = function (item) {
  console.log(numArgumentPrinted + ': ' + item);
  numArgumentPrinted++;
};
