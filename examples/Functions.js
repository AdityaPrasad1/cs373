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

function A () {
    this.v = 2;}

function test5 () {
//  const x = A();        // TypeError: Cannot set property 'v' of undefined
    const x = new A();
    assert(x.v    == 2);
    assert(x["v"] == 2);}

function main () {
    console.log("Functions.js");
    for (let i of _.range(5))
        eval("test" + (i + 1) + "()");}
    console.log("Done.");

main();
