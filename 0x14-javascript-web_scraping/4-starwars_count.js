#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const films = JSON.parse(body).results;
  let count = 0;

  for (const film of films) {
    for (const char of film.characters) {
      if (char.includes('18')) {
        count += 1;
      }
    }
  }

  console.log(count);
});
