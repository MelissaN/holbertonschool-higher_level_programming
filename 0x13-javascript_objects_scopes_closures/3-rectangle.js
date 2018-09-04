#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    for (let col = 0; col < this.height; col += 1) {
      console.log('X'.repeat(this.width));
    }
  }
};
