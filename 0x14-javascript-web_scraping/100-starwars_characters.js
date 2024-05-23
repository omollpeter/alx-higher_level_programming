#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const characters = JSON.parse(body).characters;
  characters.forEach(character => {
        request(character, (error, response, body) => {
            console.log(JSON.parse(body).name);
        })

  });
});
