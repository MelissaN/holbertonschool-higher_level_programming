#!/usr/bin/node
let myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

/*
adding line below prints as a result:
{ type: 'object', value: 12 }
{ type: 'object', value: 13, incr: [Function] }
{ type: 'object', value: 14, incr: [Function] }
{ type: 'object', value: 15, incr: [Function] }
*/
myObject.incr = function () { this.value += 1; };

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
