#!/usr/bin/node
const request = require("request");
const url = "https://swapi-api.alx-tools.com/api/films/" + process.argv[2];

async function fetchData(url) {
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error("Problem with response")
        }

        const data = await response.json()
        return data;
    } catch (error) {
        console.log("Error:", error)
    }
}

async function fetchMultiple(urls) {
    const results = [];

    for (const url of urls) {
        const data = await fetchData(url);
        results.push(data.name);
    }
    return results;
}

request(url, (error, response, body) => {
    if (error) {
        console.log(error);
        return;
    }

    const characters = JSON.parse(body).characters;
    fetchMultiple(characters)
        .then(results => {
            for (const result of results) {
                console.log(results);
            }
        })
        .catch(error => {
            console.log("Error:", error);
        })
})
