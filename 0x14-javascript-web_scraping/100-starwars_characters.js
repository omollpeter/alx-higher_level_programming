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
    fetch(character)
      .then(response => {
        if (!response.ok) {
          console.log('Problem with response');
        }
        return response.json();
      })
      .then(data => {
        console.log(data.name);
      })
      .catch(error => {
        console.log('Error:', error);
      });
  });
});
