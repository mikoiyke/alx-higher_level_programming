
#!/usr/bin/node

const { argv } = require('node:process');

const fs = require('fs');

fs.readFile(argv[2], 'utf-8', (errMsg, fileContent) => {
  if (errMsg) {
    console.error(errMsg);
	return -1;
  }
  fs.writeFile(argv[4], fileContent, 'utf-8', (errMsg) => {
    if (errMsg) {
      console.error(errMsg);
	  return -1;
    }
  });
});

fs.readFile(argv[3], 'utf-8', (errMsg, fileContent) => {
  if (errMsg) {
    console.error(errMsg);
	return -1;
  }
  fs.appendFile(argv[4], fileContent, 'utf-8', (errMsg) => {
    if (errMsg) {
      console.error(errMsg);
	  return -1;
    }
  });
});
