#!/usr/bin/node
const loopCount = parseInt(process.argv[2]);
if (loopCount) {
  for (let j = 0; j < loopCount; j++) {
    console.log('X'.repeat(loopCount));
  }
} else {
  console.log('Missing size');
}
