#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const file = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  fs.writeFile(file, body, 'utf-8', (error) => {
    if (error) {
      console.log(error);
    }
  });
});
