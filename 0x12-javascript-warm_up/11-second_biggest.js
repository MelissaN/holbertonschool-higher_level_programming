#!/usr/bin/node

const nums_array = process.argv.slice(2);
function second_max (array) {
  if (array.length < 2) {
    return (0);
  } else {
    array.sort((x, y) => x - y);
    array.pop();
    return (array.pop());
  }
}
console.log(second_max(nums_array));
