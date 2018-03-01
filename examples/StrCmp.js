#!/usr/bin/env node

/* jshint
    esversion: 6,
    evil:      true
*/

// ----------
// StrCmps.js
// ----------

"use strict";

const assert = require('assert');
const _      = require('lodash');

function test1 () {
    assert(strcmp("",    "")    == 0);}

function test2 () {
    assert(strcmp("abc", "abc") == 0);}

function test3 () {
    assert(strcmp("abc", "ab")  >  0);}

function test4 () {
    assert(strcmp("abc", "aba") >  0);}

function test5 () {
    assert(strcmp("ab",  "abc") <  0);}

function test6 () {
    assert(strcmp("aba", "abc") <  0);}

function main () {
    console.log("StrCmp.js");
    for (const i of _.range(6))
        eval("test" + (i + 1) + "()");}
    console.log("Done.");

main();
