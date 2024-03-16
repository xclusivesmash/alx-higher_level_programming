#!/usr/bin/node
/*
 * Description: processing cmd args.
 */

if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
