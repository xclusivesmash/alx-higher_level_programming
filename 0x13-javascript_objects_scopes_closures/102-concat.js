#!/usr/bin/node
const fs = require('fs');
const argv = process.argv;

const fileA = argv[2];
const fileB = argv[3];
const fileC = argv[4];

if (fs.existsSync(fileA) && fs.statSync(fileA).isFile && fs.existsSync(fileB) &&
fs.statSync(fileB).isFile &&
fileC !== undefined
) {
  const fileAContent = fs.readFileSync(fileA);
  const fileBContent = fs.readFileSync(fileB);
  const stream = fs.createWriteStream(fileC);

  stream.write(fileAContent);
  stream.write(fileBContent);
  stream.end();
}
