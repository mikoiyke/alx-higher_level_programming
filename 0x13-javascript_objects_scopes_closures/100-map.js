#!/usr/bin/node

const { list } = require('./100-data.js');

console.log(list); // Print the initial list

const mappedList = list.map((currentValue, index) => currentValue * index);

console.log(mappedList); // Print the new list after the map operation

