#!/usr/bin/node
const firstArg = parseInt(process.argv[2]);
if (firstArg) {
  console.log(firstArg);
} else {
  console.log('Not a number');
}
