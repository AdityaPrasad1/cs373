#!/usr/bin/env node

/* jshint
    esversion: 6,
    evil:      true
*/

// ----------------
// RangeIterator.js
// ----------------

"use strict";

const assert = require('assert');
const _      = require('lodash');

function test1 () {
    const x = _.range(2, 2);
    const p = x[Symbol.iterator]();
    assert(p === p[Symbol.iterator]());
    const n = p.next();
    assert(n.done);}

function test2 () {
    const x = _.range(2, 3);
    const p = x[Symbol.iterator]();
    assert(p === p[Symbol.iterator]());
    let n = p.next();
    assert(!n.done);
    assert(n.value === 2);
    n = p.next();
    assert(n.done);}

function test3 () {
    const x = _.range(2, 4);
    const p = x[Symbol.iterator]();
    assert(p === p[Symbol.iterator]());
    let n = p.next();
    assert(!n.done);
    assert(n.value === 2);
    n = p.next();
    assert(!n.done);
    assert(n.value === 3);
    n = p.next();
    assert(n.done);}

function test4 () {
    const x = _.range(2, 5);
    const p = x[Symbol.iterator]();
    assert(p === p[Symbol.iterator]());
    const a = [];
    for (let v of p)
        a.push(v);
    assert(_.isEqual(a, [2, 3, 4]));}

function main () {
    for (let i of _.range(4))
        eval("test" + (i + 1) + "()");}

console.log("RangeIterator.js");
main();
console.log("Done.");
