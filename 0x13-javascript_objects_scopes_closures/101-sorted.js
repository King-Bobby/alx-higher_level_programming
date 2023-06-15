#!/usr/bin/node
const dict = require('./101-data').dict;

const sortedDict = {};
for (const key in dict) {
  const value = dict[key];
  if (value in sortedDict) {
    sortedDict[value].push(key);
  } else {
    sortedDict[value] = [key];
  }
}

console.log(sortedDict);
