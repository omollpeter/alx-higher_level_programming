#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

function fetchData (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      }
      resolve(JSON.parse(body).name);
    });
  });
}

async function fetchMultiple (urls) {
  if (urls.length === 0) {
    return [];
  }

  const url = urls.shift();
  const data = await fetchData(url);
  const remData = await fetchMultiple(urls);
  return [data, ...remData];
}

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const characters = JSON.parse(body).characters;
  fetchMultiple(characters)
    .then(results => {
      for (const res of results) {
        console.log(res);
      }
    })
    .catch(error => {
      console.log(error);
    });
});
