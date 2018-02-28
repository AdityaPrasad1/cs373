#!/usr/bin/env node

/* jshint
    esversion: 6,
    evil:      true
*/

// ------------
// Factorial.js
// ------------

"use strict";

const assert = require('assert');
const _      = require('lodash');

function test1 () {
    assert(factorial(0) == 1);}

function test2 () {
    assert(factorial(1) == 1);}

function test3 () {
    assert(factorial(2) == 2);}

function test4 () {
    assert(factorial(3) == 6);}

function test5 () {
    assert(factorial(4) == 24);}

function test6 () {
    assert(factorial(5) == 120);}

function main () {
    console.log("Factorial.js");
    for (let i of _.range(6))
        eval("test" + (i + 1) + "()");}
    console.log("Done.");

main();
