#!/usr/bin/env node

/* jshint
    esversion: 6,
    evil:      true
*/

// --------
// Yield.js
// --------

"use strict";

const assert = require('assert');
const _      = require('lodash');

function* f () {
    yield 2;
    yield 3;
    yield 4;}

function test1 () {
    const p = f();
    assert(p === p[Symbol.iterator]());
    var n = p.next();
    assert(!n.done);
    assert(n.value === 2);
    n = p.next();
    assert(!n.done);
    assert(n.value === 3);
    n = p.next();
    assert(!n.done);
    assert(n.value === 4);
    n = p.next();
    assert(n.done);}

function test2 () {
    const p = f();
    const a = [];
    for (let v of p)
        a.push(v);
    assert(_.isEqual(a, [2, 3, 4]));}

function* g () {
    for (let v of [2, 3, 4])
        yield v;}

function test3 () {
    const p = g();
    assert(p === p[Symbol.iterator]());
    var n = p.next();
    assert(!n.done);
    assert(n.value === 2);
    n = p.next();
    assert(!n.done);
    assert(n.value === 3);
    n = p.next();
    assert(!n.done);
    assert(n.value === 4);
    n = p.next();
    assert(n.done);}

function test4 () {
    const p = g();
    const a = [];
    for (let v of p)
        a.push(v);
    assert(_.isEqual(a, [2, 3, 4]));}

function main () {
    console.log("Yield.js");
    for (let i of _.range(4))
        eval("test" + (i + 1) + "()");}
    console.log("Done.");

main();
