#!/usr/bin/node

let url = process.argv[2];
const request = require('request');

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    let dic = {};
    let tasks = JSON.parse(body);
    for (let i in tasks) {
      if (dic[tasks[i].userId] === undefined) {
	dic[tasks[i].userId] = 0;
      }
      if (tasks[i].completed) {
	dic[tasks[i].userId]++;
      }
    }
    console.log(dic);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
