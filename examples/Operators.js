#!/usr/bin/env node

/* jshint
    esversion: 6,
    evil:      true,
    sub:       true
*/

// ------------
// Operators.js
// ------------

// http://www.w3schools.com/js/js_operators.asp

"use strict";

const assert = require('assert');
const _      = require('lodash');

function test1 () {
    let   i = 2;
    const j = ++i;    // pre-increment
    assert(i === 3);
    assert(j === 3);}

function test2 () {
    let   i = 2;
    const j = i++;    // post-increment
    assert(i === 3);
    assert(j === 2);}

function test3 () {
    const i = 2;
    const j = -i;      // negation
    assert(i ===  2);
    assert(j === -2);}

function test4 () {
    let   i = 2;
    const j = 3;
    const k = (i = j); // assignment
    assert(i === 3);
    assert(j === 3);
    assert(k === 3);}

function test5 () {
    const i = 2;
    const j = 3;
    const k = (i + j); // addition
    assert(i === 2);
    assert(j === 3);
    assert(k === 5);}

function test6 () {
    let   i = 2;
    const j = 3;
    const k = (i += j); // in-place addition
    assert(i === 5);
    assert(j === 3);
    assert(k === 5);}

function test7 () {
    const i = 5;
    const j = 2;
    const k = (i / j); // division
    assert(i === 5);
    assert(j === 2);
    assert(k === 2.5);}

function test8 () {
    let   i = 5;
    const j = 2;
    const k = (i /= j); // in-place division
    assert(i === 2.5);
    assert(j === 2);
    assert(k === 2.5);}

function test9 () {
    const i = 5;
    const j = 2;
    const k = (i % j); // mod
    assert(i === 5);
    assert(j === 2);
    assert(k === 1);}

function test10 () {
    let   i = 5;
    const j = 2;
    const k = (i %= j); // in-place mod
    assert(i === 1);
    assert(j === 2);
    assert(k === 1);}

function test11 () {
    const i = 2;
    const j = ~i;      // bit complement
    const k = ~j;
    assert(i ===  2);
    assert(j === -3);
    assert(k ===  2);}

function test12 () {
    const i = 2.5;
    const j = ~i;      // bit complement
    const k = ~j;
    assert(i ===  2.5);
    assert(j === -3);
    assert(k ===  2);}

function test13 () {
    const i = 2;
    const j = 3;
    const k = (i << j); // bit shift left
    assert(i ===  2);
    assert(j ===  3);
    assert(k === 16);}

function test14 () {
    let   i = 2;
    const j = 3;
    const k = (i <<= j); // in-place bit shift left
    assert(i === 16);
    assert(j ===  3);
    assert(k === 16);}

function test15 () {
    const i = 10;      // 1010
    const j = 12;      // 1100
    const k = (i & j); // 1000: bit and
    assert(i === 10);
    assert(j === 12);
    assert(k ===  8);}

function test16 () {
    let   i = 10;
    const j = 12;
    const k = (i &= j); // in-place bit and
    assert(i ===  8);
    assert(j === 12);
    assert(k ===  8);}

function test17 () {
    const i = 10;      // 1010
    const j = 12;      // 1100
    const k = (i | j); // 1110: bit or
    assert(i === 10);
    assert(j === 12);
    assert(k === 14);}

function test18 () {
    let   i = 10;
    const j = 12;
    const k = (i |= j); // in-place bit or
    assert(i === 14);
    assert(j === 12);
    assert(k === 14);}

function test19 () {
    const i = 10;      // 1010
    const j = 12;      // 1100
    const k = (i ^ j); // 0110: bit exclusive or
    assert(i === 10);
    assert(j === 12);
    assert(k ===  6);}

function test20 () {
    let   i = 10;
    const j = 12;
    const k = (i ^= j); // in-place bit exclusive or
    assert(i ===  6);
    assert(j === 12);
    assert(k ===  6);}

function test21 () {
    let i = 10;
    let j = 12;
    i ^= j;
    j ^= i;
    i ^= j;
    assert(i === 12);
    assert(j === 10);}

function test22 () {
    const a = true;
    const b = true;
    const c = false;
    assert(a && b);
    assert(!(a && c));
    assert(a || b);
    assert(a || c);}

function test23 () {
    const a = [2, 3, 4];
    assert(a[1] === 3);  // array index
    a[1] += 1;
    assert(a[1] === 4);}

function test24 () {
    const s = "a";
    const t = "bc";
    const u = s + t;      // string concatenation
    assert(u === "abc");}

function test25 () {
    const a = [2];
    const b = [3, 4];
    const c = a.concat(b);            // array concatenation
    assert(c !== [2, 3, 4]);
    assert(c !=  [2, 3, 4]);
    assert(_.isEqual(c, [2, 3, 4]));}

function test26 () {
    const a = [2, 3];
    const [i, j] = a;
    assert(i === 2);
    assert(j === 3);}

function test27 () {
    const a = [2, 3, 4];
    const [i, , k] = a;
    assert(i === 2);
    assert(k === 4);}

function test28 () {
    const a = [2, 3];
    const [i, j, k = 5] = a;
    assert(i === 2);
    assert(j === 3);
    assert(k === 5);}

function test29 () {
    const a = [2, 3, 4];
    const [i, j, k = 5] = a;
    assert(i === 2);
    assert(j === 3);
    assert(k === 4);}

function test30 () {
    const a = [2, 3, 4, 5, 6];
    const [i, j, ...k] = a;
    assert(i === 2);
    assert(j === 3);
    assert(_.isEqual(k, [4, 5, 6]));}

function test31 () {
    const a = {"i": 2, "j": 3};
    const {i, j} = a;
    assert(i === 2);
    assert(j === 3);}

function test32 () {
    const a = {"x": 2, "y": 3};
    const {x: i, y: j} = a;
    assert(i === 2);
    assert(j === 3);}

function main () {
    console.log("Operators.js");
    for (const i of _.range(32))
        eval("test" + (i + 1) + "()");
    console.log("Done.");}

main();
