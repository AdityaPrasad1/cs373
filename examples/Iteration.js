#!/usr/bin/env node

/* jshint
    esversion: 6,
    evil:      true
*/

// ------------
// Iteration.js
// ------------

// https://www.w3schools.com/jsref/jsref_forin.asp

"use strict";

const assert = require('assert');
const _      = require('lodash');

function test1 () {
    const a = [2, 3, 4];
    let   s = 0;
    for (let k in a) {                   // warning: order NOT guaranteed
        assert((typeof k) === "string");
        const v = a[k];
        assert((typeof v) === "number");
        s += v;}
    assert(s === 9);}

function test2 () {
    const a = [2, 3, 4];
    let   s = 0;
    for (let v of a) {                   // order guaranteed
        assert((typeof v) === "number");
        s += v;}
    assert(s === 9);}

function test3 () {
    class A {
        constructor (i, j, k) {
            this.i = i;
            this.j = j;
            this.k = k;}}
    const x = new A(2, 3, 4);
    let   s = 0;
    for (let k in x) {                   // warning: order NOT guaranteed
        assert((typeof k) === "string");
        const v = x[k];
        assert((typeof v) === "number");
        s += v;}
    assert(s === 9);}

function test4 () {
    class A {
        constructor (i, j, k) {
            this.i = i;
            this.j = j;
            this.k = k;}}
    const x = new A(2, 3, 4);
    let   s = 0;
//  for (let v of x) {                   // TypeError: x is not iterable
//      assert((typeof v) === "number");
//      s += v;}
//  assert(s === 9);
    }

function main () {
    console.log("Iteration.js");
    for (let i of _.range(4))
        eval("test" + (i + 1) + "()");
    console.log("Done.");}

main();
