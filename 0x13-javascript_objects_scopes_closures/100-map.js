#!/usr/bin/node

const { list } = require('./100-data');

let i = 0;

const map1 = list.map((x) => x * 1);
const map2 = list.map((x) => x * i++);

console.log(map1);
console.log(map2);
