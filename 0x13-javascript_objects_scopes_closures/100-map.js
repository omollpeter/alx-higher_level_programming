#!/usr/bin/node

const { list } = require('./100-data');

let index = 0;
const newList = list.map((item) => item * index++);

console.log(list);
console.log(newList);
