#!/usr/bin/env node

/* jshint
    esversion: 6,
    evil:      true
*/

// -------------
// Exceptions.js
// -------------

// https://nodejs.org/api/errors.html

"use strict";

const assert = require('assert');
const _      = require('lodash');

function f (b) {
    if (b) {
        throw new Error("abc");}
    return 0;}

function test1 () {
    try {
        assert(f(false) === 0);}
    catch (e) {
        assert(false);}
    finally {
        assert(true);}}

function test2 () {
    try {
        assert(f(true) === 1);
        assert(false);}
    catch (e) {
        assert(e         instanceof Error);
        assert(e.message ===        "abc");}
    finally {
        assert(true);}}

function main () {
    console.log("Exceptions.js");
    for (let i of _.range(2))
        eval("test" + (i + 1) + "()");}
    console.log("Done.");

main();
