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

  for (let i = 0; i < films.length; i++) {
    if (films[i].characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      count += 1;
    }
  }

  console.log(count);
});
