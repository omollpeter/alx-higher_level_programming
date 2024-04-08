#!/usr/bin/node
const intList = process.argv;
const listToProcess = [];

for (let i = 2; i < intList.length; i++) {
  listToProcess.push(parseInt(intList[i]));
}

if (listToProcess.length <= 1) {
  console.log(0);
} else {
  let max = listToProcess[0];
  for (let i = 1; i < listToProcess.length; i++) {
    if (listToProcess[i] > max) {
      max = listToProcess[i];
    }
  }
  console.log(max);
}