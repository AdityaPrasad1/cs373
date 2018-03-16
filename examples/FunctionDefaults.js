#!/usr/bin/env node

/* jshint
    esversion: 6,
    evil:      true,
    -W138:     true  // Regular parameters should not come after default parameters.
*/

// -------------------
// FunctionDefaults.js
// -------------------

// https://www.w3schools.com/js/js_function_parameters.asp

"use strict";

const assert = require('assert');
const _      = require('lodash');

function f (x, y, z=5) {
    return [x, y, z];}

function test1 () {
    assert(_.isEqual(f(),        [undefined, undefined, 5]));
    assert(_.isEqual(f(2),       [2,         undefined, 5]));
    assert(_.isEqual(f(2, 3),    [2,         3,         5]));
    assert(_.isEqual(f(2, 3, 4), [2,         3,         4]));}

function g (x, y=5, z) {
    return [x, y, z];}

function test2 () {
    assert(_.isEqual(g(),        [undefined, 5, undefined]));
    assert(_.isEqual(g(2),       [2,         5, undefined]));
    assert(_.isEqual(g(2, 3),    [2,         3, undefined]));
    assert(_.isEqual(g(2, 3, 4), [2,         3, 4]));}

function h (x=[]) {
    x.push(2);
    return x;}

function test3 () {
    assert(_.isEqual(h(), [2]));
    assert(_.isEqual(h(), [2]));}

function main () {
    console.log("FunctionDefaults.js");
    for (let i of _.range(3))
        eval("test" + (i + 1) + "()");
    console.log("Done.");}

main();
