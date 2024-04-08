#!/usr/bin/node
const numberOfCliArgs = process.argv.length;

if (numberOfCliArgs === 2) {
  console.log('No argument');
} else if (numberOfCliArgs === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
