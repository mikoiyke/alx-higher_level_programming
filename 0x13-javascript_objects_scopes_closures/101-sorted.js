#!/usr/bin/node
const { dict } = require('./101-data.js');

const newDict = {};

for (const [key, value] of Object.entries(dict)) {
  // Check if the value exists as a key in newDict
  if (newDict[value]) {
    // If the key exists, push the original key into the array
    newDict[value].push(key);
  } else {
    // If the key does not exist, create an array and add the original key
    newDict[value] = [key];
  }
}

console.log(newDict);
