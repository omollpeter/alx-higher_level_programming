#!/usr/bin/node
const loopCount = parseInt(process.argv[2]);
if (loopCount) {
  for (let i = 0; i < loopCount; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
