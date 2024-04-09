#!/usr/bin/node

const { argv } = require('node:process');

const array = [
  'C is fun',
  'Python is cool',
  'JavaScript is amazing'
];

let m = 0;

for (m of array) {
  console.log(m);
}
