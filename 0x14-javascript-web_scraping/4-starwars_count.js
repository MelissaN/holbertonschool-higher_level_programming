#!/usr/bin/node

let url = process.argv[2];
const request = require('request');

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    let films = JSON.parse(body).results;
    let count = 0;
    for (let i in films) {
      let chars = films[i].characters;
      for (let c in chars) {
	if (chars[c].includes('18')) {
	  count++;
	}
      }
    }
    console.log(count);
  } else {
    console.log('Erorr Code:' + response.statusCode);
  }
});
