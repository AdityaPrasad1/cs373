#!/usr/bin/env node

/* jshint
    esversion: 6
*/

// -------------
// Assertions.js
// -------------

// https://www.w3schools.com/nodejs/ref_assert.asp

"use strict";

const assert = require('assert');

function cycle_length (n) {
    assert(n > 0);
    let c = 0;
    while (n > 1) {
        if ((n % 2) === 0) {
            n = (n / 2);}
        else {
            n = (3 * n) + 1;}
        c += 1;}
    assert(c > 0);
    return c;}

function test () {
    assert(cycle_length( 1) === 1);
    assert(cycle_length( 5) === 6);
    assert(cycle_length(10) === 7);}

console.log("Assertions.js");
test();
console.log("Done.");

/*
% node Assertions.js
Assertions.js
assert.js:42
  throw new errors.AssertionError({
  ^

AssertionError [ERR_ASSERTION]: false == true
    at cycle_length (/Users/downing/Dropbox/examples/javascript/Assertions.js:26:5)
    at test (/Users/downing/Dropbox/examples/javascript/Assertions.js:30:12)
    at Object.<anonymous> (/Users/downing/Dropbox/examples/javascript/Assertions.js:35:1)
    at Module._compile (module.js:660:30)
    at Object.Module._extensions..js (module.js:671:10)
    at Module.load (module.js:573:32)
    at tryModuleLoad (module.js:513:12)
    at Function.Module._load (module.js:505:3)
    at Function.Module.runMain (module.js:701:10)
    at startup (bootstrap_node.js:193:16)
*/
