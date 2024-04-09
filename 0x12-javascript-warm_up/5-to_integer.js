#!/usr/bin/node

const { argv } = require('node:process');

const convertint = Number.parseInt(argv[2]);

if (isNaN(convertint === undefined || argv.length !== 3)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + convertint);
}
