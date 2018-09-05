#!/usr/bin/node

let filename = process.argv[2];
const fs = require('fs');
fs.readFile(filename, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
