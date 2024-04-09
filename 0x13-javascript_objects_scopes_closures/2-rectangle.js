#!/usr/bin/node
class Rectangle {
  width;
  height;

  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      this.width = null;
      this.height = null;
    } else {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
