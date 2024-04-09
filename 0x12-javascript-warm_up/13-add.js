#!/usr/bin/node

// Define the add function
function add (a, b) {
  return a + b;
}

// Make the add function visible from outside by exporting it
module.exports.add = add;
