#!/usr/bin/node
exports.esrever = function (list) {
  const len = list.length;
  const reversed = [];

  for (let i = len - 1; i >= 0; i--) {
    reversed.push(list[i]);
  }

  return reversed;
};
