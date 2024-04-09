#!/usr/bin/node

const { argv } = require('process');

const num = Number.parseInt(argv[2]);

// Check if num is not a number
if (isNaN(num)) {
  console.log('Missing size');
} else {
  // Loop to print rows
  for (let x = 0; x < num; x++) {
    let row = '';
    // Loop to construct each row
    for (let j = 0; j < num; j++) {
      row += 'x'; // Add 'x' to the row
    }
    console.log(row); // Print the row
  }
}
