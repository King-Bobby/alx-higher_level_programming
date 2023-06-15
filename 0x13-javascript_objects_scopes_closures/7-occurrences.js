#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const l = list;
  const elem = searchElement;
  let count = 0;
  for (let i = 0; i < l.length; i++) {
    if (l[i] === elem) {
      count++;
    }
  }
  return count;
};
