#!/usr/bin/env node

/* global
    before,
    describe,
    it
*/

/* jshint
    esversion: 6
*/

// -----------------
// RangeIteratorT.js
// -----------------

"use strict";

const assert   = require('assert');
const _        = require('lodash');
const readline = require('readline');

class range_iterator_1 {
    constructor (b, e) {
        this.b = b;
        this.e = e;}

    [Symbol.iterator] () {
        return this;}

    next () {
        var n = {"value": this.b, "done": (this.b == this.e)};
        ++this.b;
        return n;}}

describe('RangeIterator',
    function () {
        let a;

        before(function () {
            a = [
                (b, e) => {
                    return new range_iterator_1(b, e);},
                (b, e) => {
                    const x = _.range(b, e);
                    return x[Symbol.iterator]();}];});

        it('test1',
            function () {
                for (let f of a) {
                    const p = f(2, 2);
                    assert(p === p[Symbol.iterator]());
                    const n = p.next();
                    assert(n.done);}});

        it('test2',
            function () {
                for (let f of a) {
                    const p = f(2, 3);
                    assert(p === p[Symbol.iterator]());
                    let n = p.next();
                    assert(!n.done);
                    assert(n.value === 2);
                    n = p.next();
                    assert(n.done);}});

        it('test3',
            function () {
                for (let f of a) {
                    const p = f(2, 4);
                    assert(p === p[Symbol.iterator]());
                    let n = p.next();
                    assert(!n.done);
                    assert(n.value === 2);
                    n = p.next();
                    assert(!n.done);
                    assert(n.value === 3);
                    n = p.next();
                    assert(n.done);}});

        it('test4',
            function () {
                for (let f of a) {
                    const p = f(2, 5);
                    assert(p === p[Symbol.iterator]());
                    const a = [];
                    for (let v of p)
                        a.push(v);
                    assert(_.isEqual(a, [2, 3, 4]));}});});
