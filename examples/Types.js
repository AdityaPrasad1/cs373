#!/usr/bin/env node

/* jshint
    esversion: 6,
    evil:      true,
    sub:       true
*/

// --------
// Types.js
// --------

// https://www.w3schools.com/js/js_datatypes.asp

"use strict";

const assert = require('assert');
const _      = require('lodash');

function test1 () {
    const b = false;
    assert(b          === false);
    assert((typeof b) === "boolean");
    assert(!(b instanceof Boolean));
    assert(!(b instanceof Object));}

function test2 () {
    const i = 2;
    assert(i          === 2);
    assert((typeof i) === "number");
    assert(!(i instanceof Number));
    assert(!(i instanceof Object));}

function test3 () {
    const f = 2.34;
    assert(f          === 2.34);
    assert((typeof f) === "number");
    assert(!(f instanceof Number));
    assert(!(f instanceof Object));}

function test4 () {
    const s = "abc";
    assert(s          === "abc");
    assert((typeof s) === "string");
    assert(!(s instanceof String));
    assert(!(s instanceof Object));}

function test5 () {
    const a = [2, 3, 4];
    assert(a          !== [2, 3, 4]);  // !!!
    assert(a          !=  [2, 3, 4]);  // !!!
    assert((typeof a) === "object");
    assert(a instanceof Array);        // !!!
    assert(a instanceof Object);       // !!!
    assert(_.isEqual(a, [2, 3, 4]));}

function test6 () {
    const x = {2: "abc", 3: "def", 4: "ghi"};
    assert(x          !== {2: "abc", 3: "def", 4: "ghi"});  // !!!
    assert(x          !=  {2: "abc", 3: "def", 4: "ghi"});  // !!!
    assert((typeof x) === "object");
    assert(x instanceof Object);
    assert(_.isEqual(x, {2: "abc", 3: "def", 4: "ghi"}));}

function test7 () {
    const n = null;
    assert(n          === null);
    assert((typeof n) === "object");
    assert(!(n instanceof Object));} // !!!

function test8 () {
    let x;
    assert(x          === undefined);
    assert((typeof x) === "undefined");
    assert(!(x instanceof Object));}    // !!!

function test9 () {
    function f (v) {
        return v + 1;}
    assert((typeof f) === "function");
    assert(f(2) == 3);}

function test10 () {
    const f = (v) => {return v + 1;};
    assert((typeof f) === "function");
    assert(f(2) == 3);}

function test11 () {
    function A (i, j) {
        this.i = i;
        this.j = j;}

//  const x = A(2, 3);                 // TypeError: Cannot set property 'i' of undefined
    const x = new A(2, 3);
    assert((typeof x) === "object");
    assert(x instanceof A);
    assert(x instanceof Object);
    assert(x.i    == 2);
    assert(x.j    == 3);
    assert(x["i"] == 2);
    assert(x["j"] == 3);}

function test12 () {
    const x = {"i": 2, "j": 3};
    assert((typeof x) === "object");
    assert(x instanceof Object);
    assert(x.i    == 2);
    assert(x.j    == 3);
    assert(x["i"] == 2);
    assert(x["j"] == 3);}

function test13 () {
    class A {
        constructor (i, j) {
            this.i = i;
            this.j = j;}}

    const x = new A(2, 3);
    assert((typeof x) === "object");
    assert(x instanceof A);
    assert(x instanceof Object);
    assert(x.i    == 2);
    assert(x.j    == 3);
    assert(x["i"] == 2);
    assert(x["j"] == 3);}

function main () {
    console.log("Types.js");
    for (let i of _.range(13))
        eval("test" + (i + 1) + "()");
    console.log("Done.");}

main();
