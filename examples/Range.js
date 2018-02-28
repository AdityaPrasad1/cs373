#!/usr/bin/env node

/* jshint
    esversion: 6,
    evil:      true
*/

// --------
// Range.js
// --------

"use strict";

const assert = require('assert');
const _      = require('lodash');

function test1 () {
    const x = _.range(2, 2);
    const a = [];
    for (let v of x)
        a.push(v);
    assert(_.isEqual(a, []));}

function test2 () {
    const x = _.range(2, 3);
    const a = [];
    for (let v of x)
        a.push(v);
    assert(_.isEqual(a, [2]));}

function test3 () {
    const x = _.range(2, 4);
    const a = [];
    for (let v of x)
        a.push(v);
    assert(_.isEqual(a, [2, 3]));}

function test4 () {
    const x = _.range(2, 5);
    assert(x[0] === 2);
    assert(x[1] === 3);
    assert(x[2] === 4);}

function main () {
    console.log("Range.js");
    for (let i of _.range(4))
        eval("test" + (i + 1) + "()");}
    console.log("Done.");

main();
