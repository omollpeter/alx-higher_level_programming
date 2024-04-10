#!/usr/bin/node
const { dict } = require('./101-data');

const newDict = {};

Object.values(dict).forEach(value => {
  newDict[value] = [];
});

Object.keys(dict).forEach(key => {
  newDict[dict[key]].push(key);
});
console.log(newDict);
