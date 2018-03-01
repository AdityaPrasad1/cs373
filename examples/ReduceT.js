#!/usr/bin/env node

/* global
    before,
    describe,
    it
*/

/* jshint
    esversion: 6
*/

// ----------
// ReduceT.js
// ----------

// https://www.w3schools.com/jsref/jsref_reduce.asp

"use strict";

const assert = require('assert');
const _      = require('lodash');

function reduce_for (a, bf, v) {
    for (const w of a)
        v = bf(v, w);
    return v;}

function reduce_while (a, bf, v) {
    const p = a[Symbol.iterator]();
    while (true) {
        const n = p.next();
        if (n.done)
            break;
        const w = n.value;
        v = bf(v, w);}
    return v;}

describe('reduce',
    function () {
        let a;

        before(function () {
            a = [
                reduce_for,
                reduce_while,
                _.reduce];});

        it('test1',
            function () {
                for (let f of a)
                    assert(f([2, 3, 4], _.add,      0) == 9);});

        it('test2',
            function () {
                for (let f of a)
                    assert(f([2, 3, 4], _.multiply, 1) == 24);});

        it('test3',
            function () {
                for (let f of a)
                    assert(f([2, 3, 4], _.subtract, 2) == -7);});

        it('test4',
            function () {
                for (let f of a)
                    assert(f([],        null,       3) == 3);});});
