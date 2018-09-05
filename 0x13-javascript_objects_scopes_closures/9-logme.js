#!/usr/bin/node

let num = -1;
exports.logMe = function (item) {
  num++;
  console.log(num + ': ' + item);
};
