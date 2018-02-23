#!/usr/bin/env node

/* jshint
    esversion: 6,
    evil:      true
*/

// ---------
// Reduce.js
// ---------

// https://www.w3schools.com/jsref/jsref_reduce.asp

"use strict";

const assert = require('assert');
const _      = require('lodash');

function test1 () {
    assert(_.reduce([2, 3, 4], _.add,      0) == 9);}

function test2 () {
    assert(_.reduce([2, 3, 4], _.multiply, 1) == 24);}

function test3 () {
    assert(_.reduce([2, 3, 4], _.subtract, 2) == -7);}

function test4 () {
    assert(_.reduce([],        null,       3) == 3);}

function main () {
    for (let i of _.range(4))
        eval("test" + (i + 1) + "()");}

console.log("Reduce.js");
main();
console.log("Done.");
