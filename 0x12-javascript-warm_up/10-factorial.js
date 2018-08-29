#!/usr/bin/node

const n = parseInt(process.argv[2], 10);
function factorial (n) {
  if (isNaN(n) || n === 0) {
    return (1);
  }
  return (n * factorial(n - 1));
}
console.log(factorial(n));
