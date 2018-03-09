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
    assert((typeof b) !== "object");
    assert((typeof b) !== Boolean);
    assert((typeof b) !== Object);
    assert(!(b instanceof Boolean));
    assert(!(b instanceof Object));}

function test2 () {
    const i = 2;
    assert(i          === 2);
    assert((typeof i) === "number");
    assert((typeof i) !== "object");
    assert((typeof i) !== Number);
    assert((typeof i) !== Object);
    assert(!(i instanceof Number));
    assert(!(i instanceof Object));}

function test3 () {
    const f = 2.34;
    assert(f          === 2.34);
    assert((typeof f) === "number");
    assert((typeof f) !== "object");
    assert((typeof f) !== Number);
    assert((typeof f) !== Object);
    assert(!(f instanceof Number));
    assert(!(f instanceof Object));}

function test4 () {
    const s = "abc";
    assert(s === "abc");
    assert((typeof s) === "string");
    assert((typeof s) !== "object");
    assert((typeof s) !== String);
    assert((typeof s) !== Object);
    assert(!(s instanceof String));
    assert(!(s instanceof Object));}

function test5 () {
    const a = [2, 3, 4];
    assert(a !== [2, 3, 4]);         // !!!
    assert(a !=  [2, 3, 4]);         // !!!
    assert(_.isEqual(a, [2, 3, 4]));
    assert((typeof a) === "object");
    assert((typeof a) !== Array);
    assert((typeof a) !== Object);
    assert(a instanceof Array);      // !!!
    assert(a instanceof Object);}

function test6 () {
    const x = {2: "abc", 3: "def", 4: "ghi"};
    assert(x !== {2: "abc", 3: "def", 4: "ghi"});         // !!!
    assert(x !=  {2: "abc", 3: "def", 4: "ghi"});         // !!!
    assert(_.isEqual(x, {2: "abc", 3: "def", 4: "ghi"}));
    assert((typeof x) === "object");
    assert((typeof x) !== Object);
    assert(x instanceof Object);}

function test7 () {
    const n = null;
    assert(n          === null);
    assert((typeof n) === "object");
    assert((typeof n) !== Object);
    assert(!(n instanceof Object));} // !!!

function test8 () {
    let u;
    assert(u          === undefined);
    assert((typeof u) === "undefined");
    assert((typeof u) !== "object");
    assert((typeof u) !== Object);
    assert(!(u instanceof Object));}

function test9 () {
    function f (v) {
        return v + 1;}
    assert(f(2) == 3);
    assert((typeof f) === "function");
    assert((typeof f) !== "object");
    assert((typeof f) !== Object);
    assert((f instanceof Object));}    // !!!

function test10 () {
    const f = (v) => {return v + 1;};
    assert(f(2) == 3);
    assert((typeof f) === "function");
    assert((typeof f) !== "object");
    assert((typeof f) !== Object);
    assert((f instanceof Object));}    // !!!

function test11 () {
    const x = {"i": 2, "j": 3};
    assert((typeof x) === "object");
    assert(x instanceof Object);
    assert(x.i    === 2);
    assert(x.j    === 3);
    assert(x["i"] === 2);
    assert(x["j"] === 3);}

function test12 () {
    function A (i, j) {
        this.i = i;
        this.j = j;}

//  const x = A(2, 3);               // TypeError: Cannot set property 'i' of undefined
    const x = new A(2, 3);
    assert((typeof x) === "object");
    assert((typeof x) !== A);        // !!!
    assert(x instanceof A);
    assert(x instanceof Object);
    assert(x.i    === 2);
    assert(x.j    === 3);
    assert(x["i"] === 2);
    assert(x["j"] === 3);}

function test13 () {
    class A {
        constructor (i, j) {
            this.i = i;
            this.j = j;}}

    const x = new A(2, 3);
    assert((typeof x) === "object");
    assert((typeof x) !== A);        // !!!
    assert(x instanceof A);
    assert(x instanceof Object);
    assert(x.i    === 2);
    assert(x.j    === 3);
    assert(x["i"] === 2);
    assert(x["j"] === 3);}

function main () {
    console.log("Types.js");
    for (const i of _.range(13))
        eval("test" + (i + 1) + "()");
    console.log("Done.");}

main();
