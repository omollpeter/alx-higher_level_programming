#!/usr/bin/node
const fs = require('fs');
const path = require('path');

function concat (file1, file2, file3) {
  const fileContent1 = fs.readFileSync(file1, 'utf-8');
  const fileContent2 = fs.readFileSync(file2, 'utf-8');

  const concatContent = fileContent1 + '\n' + fileContent2;

  fs.writeFileSync(file3, concatContent, "utf-8");
}

const { _, fileName, filePath1, filePath2, filePath3 } = process.argv;
concat(filePath1, filePath2, filePath3);
