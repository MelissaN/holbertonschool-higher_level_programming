#!/usr/bin/node

let id = process.argv[2];
let url = 'http://swapi.co/api/films/' + id;
const request = require('request');

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    body = JSON.parse(body);
    console.log(body['title']);
  } else {
    console.log('Erorr Code:' + response.statusCode);
  }
});
