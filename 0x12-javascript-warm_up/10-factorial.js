#!/usr/bin/node
function factorial (num) {
  const n = parseInt(num);
  if (isNaN(n)) {
    return 1;
  } else if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const number = process.argv[2];
const result = factorial(number);
console.log(result);
