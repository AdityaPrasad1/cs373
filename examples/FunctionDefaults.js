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

function f (x, y, z) {
    return [x, y, z];}

function test1 () {
    assert(_.isEqual(f(),        [undefined, undefined, undefined]));
    assert(_.isEqual(f(2),       [2,         undefined, undefined]));
    assert(_.isEqual(f(2, 3),    [2,         3,         undefined]));
    assert(_.isEqual(f(2, 3, 4), [2,         3,         4]));}

function g1 (x, y, z=5) {
    return [x, y, z];}

function test2 () {
    assert(_.isEqual(g1(),        [undefined, undefined, 5]));
    assert(_.isEqual(g1(2),       [2,         undefined, 5]));
    assert(_.isEqual(g1(2, 3),    [2,         3,         5]));
    assert(_.isEqual(g1(2, 3, 4), [2,         3,         4]));}

function g2 (x, y=5, z) {
    return [x, y, z];}

function test3 () {
    assert(_.isEqual(g2(),        [undefined, 5, undefined]));
    assert(_.isEqual(g2(2),       [2,         5, undefined]));
    assert(_.isEqual(g2(2, 3),    [2,         3, undefined]));
    assert(_.isEqual(g2(2, 3, 4), [2,         3, 4]));}

function h (x=[]) {
    x.push(2);
    return x;}

function test4 () {
    assert(_.isEqual(h(), [2]));
    assert(_.isEqual(h(), [2]));}

function main () {
    console.log("FunctionDefaults.js");
    for (let i of _.range(4))
        eval("test" + (i + 1) + "()");
    console.log("Done.");}

main();
