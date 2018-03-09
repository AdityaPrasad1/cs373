#!/usr/bin/env node

/* jshint
    esversion: 6,
    evil:      true,
    sub:       true
*/

// ------------
// Functions.js
// ------------

"use strict";

const assert = require('assert');
const _      = require('lodash');

function square (v) {
    return Math.pow(v, 2);}

function test1 () {
    const a = [2, 3, 4];
    const m = a.map(square);
    assert(_.isEqual(m, [4, 9, 16]));}

function test2 () {
    const a = [2, 3, 4];
    const m = a.map(function (v) {return Math.pow(v, 2);});
    assert(_.isEqual(m, [4, 9, 16]));}

function test3 () {
    const a = [2, 3, 4];
    const m = a.map((v) => {return Math.pow(v, 2);});
    assert(_.isEqual(m, [4, 9, 16]));}

function test4 () {
    const a = [2, 3, 4];
    const n = 2;
    const m = a.map((v) => {return Math.pow(v, n);});
    assert(_.isEqual(m, [4, 9, 16]));}

function test5 () {
    const a = [2, 3, 4];
    let   n = 1;
    const f = (v) => {return Math.pow(v, n);};
    ++n;
    const m = a.map(f);
    assert(_.isEqual(m, [4, 9, 16]));}

function test6 () {
    const a  = [2, 3, 4];
    const fs = [];
    for (var n = 0; n != 3; ++n)
        fs.push((v) => {return Math.pow(v, n);});
    const ms = [];
    for (var i = 0; i != 3; ++i)
        ms.push(a.map(fs[i]));
    assert(_.isEqual(ms, [[8, 27, 64], [8, 27, 64], [8, 27, 64]]));}

function A () {
    this.v = 2;}

function test7 () {
//  const x = A();         // TypeError: Cannot set property 'v' of undefined
    const x = new A();
    assert(x.v    == 2);
    assert(x["v"] == 2);}

function main () {
    console.log("Functions.js");
    for (let i of _.range(7))
        eval("test" + (i + 1) + "()");}
    console.log("Done.");

main();
