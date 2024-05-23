#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const cTasks = Object.create({});
  const todos = JSON.parse(body);

  let userid = 1;
  let count = 0;
  for (let i = 0; i < todos.length; i++) {
    if (todos[i].userId > userid) {
      if (count) {
        cTasks[userid.toString()] = count;
      }
      userid = todos[i].userId;
      count = 0;
    }
    if (todos[i].completed) {
      count += 1;
    }
  }

  if (count) {
    cTasks[userid.toString()] = count;
  }
  console.log(cTasks);
});
