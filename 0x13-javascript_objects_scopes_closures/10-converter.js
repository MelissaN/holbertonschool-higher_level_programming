#!/usr/bin/node

exports.converter = function (base) {
  function convert (n) {
    return n.toString(base);
  }
  return convert;
};
