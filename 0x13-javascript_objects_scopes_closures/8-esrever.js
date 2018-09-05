#!/usr/bin/node

exports.esrever = function (list) {
  let beg = 0;
  let end = list.length - 1;
  while (beg < end) {
    let tmp = list[beg];
    list[beg] = list[end];
    list[end] = tmp;
    beg++;
    end--;
  }
  return list;
};
