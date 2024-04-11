#!/usr/bin/node

const { argv } = require('node:process');
const fs = require('fs');

fs.readFile(argv[2], 'utf-8', (err, fileContent) => {
  if (err) {
    console.error(err);
    return -1; // Note: Returning -1 here won't affect the flow in async callbacks.
  }
  fs.writeFile(argv[4], fileContent, 'utf-8', (err) => {
    if (err) {
      console.error(err);
      return -1; // Same note as above.
    }
  });
});

fs.readFile(argv[3], 'utf-8', (err, fileContent) => {
  if (err) {
    console.error(err);
    return -1; // Same note as above.
  }
  fs.appendFile(argv[4], fileContent, 'utf-8', (err) => {
    if (err) {
      console.error(err);
      return -1; // Same note as above.
    }
  });
});
