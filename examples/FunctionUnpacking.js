#!/usr/bin/env node

/* jshint
    esversion: 6,
    evil:      true
*/

// --------------------
// FunctionUnpacking.js
// --------------------

// https://www.w3schools.com/js/js_function_parameters.asp

"use strict";

const assert = require('assert');
const _      = require('lodash');

function f (x, y, z) {
    return [x, y, z];}

function test1 () {
    const a = [3, 4];
    assert(_.isEqual(f(2, 5, a), [2, 5, [3, 4]]));
    assert(_.isEqual(f(2, ...a), [2, 3, 4]));}

function test2 () {
    const a = [2, 3];
    const b = [4];
    assert(_.isEqual(f(...a, ...b), [2, 3, 4]));}

function main () {
    console.log("FunctionUnpacking.js");
    for (let i of _.range(2))
        eval("test" + (i + 1) + "()");
    console.log("Done.");}

main();
