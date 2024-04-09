#!/usr/bin/node

const { argv } = require('node:process');

function factorial (n) {
  if (n === 0) {
    return (1);
  }
  return n * factorial(n - 1);
}

if (argv[2] === undefined) {
  console.log(1);
} else {
  const result = factorial(Number.parseInt(argv[2]));
  console.log(result);
}
