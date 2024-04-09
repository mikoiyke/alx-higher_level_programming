#!/usr/bin/node

const { argv } = require('process');

// Check if there are less than 3 arguments
if (argv.length <= 3) {
  console.log(0);
} else {
  // Initialize variables
  let largest = Number.NEGATIVE_INFINITY;
  let secondLargest = Number.NEGATIVE_INFINITY;

  // Loop through command-line arguments starting from index 2
  for (let i = 2; i < argv.length; i++) {
    const num = parseInt(argv[i]);

    // Update largest and secondLargest if necessary
    if (num > largest) {
      secondLargest = largest;
      largest = num;
    } else if (num > secondLargest && num !== largest) {
      secondLargest = num;
    }
  }

  // Check if secondLargest is still negative infinity
  if (secondLargest === Number.NEGATIVE_INFINITY) {
    console.log(0);
  } else {
    console.log(secondLargest);
  }
}
