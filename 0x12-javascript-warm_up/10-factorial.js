#!/usr/bin/node
const factNumber = parseInt(process.argv[2]);

function factorial (n) {
  if (!n) {
    return 1;
  } else if (n < 1) {
    return 1;
  } else if (n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

console.log(factorial(factNumber));
