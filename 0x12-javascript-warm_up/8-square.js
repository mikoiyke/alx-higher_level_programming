#!/usr/bin/node

const { argv } = require('process');

const num = Number.parseInt(argv[2]);

if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < num; x++) {
    let row = '';
    for (let j = 0; j < num; j++) {
      row += 'x';
    }
    console.log(row);
  }
}
