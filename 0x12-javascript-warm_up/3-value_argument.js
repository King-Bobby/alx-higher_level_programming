#!/usr/bin/node
let count = 0;
for (let i = 2; i < process.argv.length; i++) {
  count++;
}

if (count === 0) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
