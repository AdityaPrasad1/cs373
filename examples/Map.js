#!/usr/bin/env node

/* jshint
    esversion: 6,
    evil:      true
*/

// ------
// Map.js
// ------

// https://www.w3schools.com/jsref/jsref_map.asp

"use strict";

const assert = require('assert');
const _      = require('lodash');

function test1 () {
    const m = _.map([2, 3, 4], (x) => {return x * x;});
    assert((typeof m) === "object");
    assert(m instanceof Array);
    assert(m instanceof Object);
    assert(_.isEqual(m, [4, 9, 16]));
    assert(_.isEqual(m, [4, 9, 16]));}

function test2 () {
    const m = _.map([], null);
    assert((typeof m) === "object");
    assert(m instanceof Array);
    assert(m instanceof Object);
    assert(_.isEqual(m, []));}

function test3 () {
    const m = [2, 3, 4].map((x) => {return x * x;});
    assert((typeof m) === "object");
    assert(m instanceof Array);
    assert(m instanceof Object);
    assert(_.isEqual(m, [4, 9, 16]));
    assert(_.isEqual(m, [4, 9, 16]));}

function main () {
    for (let i of _.range(3))
        eval("test" + (i + 1) + "()");}

console.log("Map.js");
main();
console.log("Done.");
