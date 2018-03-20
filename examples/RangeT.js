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

class my_range_iterator_1 {
    constructor (b, e) {
        this.b = b;
        this.e = e;}

    [Symbol.iterator] () {
        return this;}

    next () {
        let n = {
            value: this.b,
            done:  (this.b == this.e)};
        ++this.b;
        return n;}}

class my_range_1 {
    constructor (b, e) {
        const self = this;
        this.b = b;
        this.e = e;
        const h = {
            get : function (x, v) {
                if (v in x)
                    return x[v];
                return self.b + parseInt(v);}};
        return new Proxy(this, h);}

    [Symbol.iterator] () {
        return new my_range_iterator_1(this.b, this.e);}}

class my_range_2 {
    constructor (b, e) {
        this.b = b;
        this.e = e;
        const h = {
            get: (x, v) => {
                if (v in x)
                    return x[v];
                return this.b + parseInt(v);}};
        return new Proxy(this, h);}

    * [Symbol.iterator] () {
        let b = this.b;
        while (b != this.e) {
            yield b;
            ++b;}}}

describe('Range',
    function () {
        let a;

        before(function () {
            a = [
                (b, e) => {return new my_range_1(b, e);},
                (b, e) => {return new my_range_2(b, e);},
                (b, e) => {return _.range(b, e);}];});

        it('test1',
            function () {
                for (let f of a) {
                    const x = f(2, 2);
                    const a = [];
                    for (let v of x)
                        a.push(v);
                    assert(_.isEqual(a, []));}});

        it('test2',
            function () {
                for (let f of a) {
                    const x = f(2, 3);
                    const a = [];
                    for (let v of x)
                        a.push(v);
                    assert(_.isEqual(a, [2]));}});

        it('test3',
            function () {
                for (let f of a) {
                    const x = f(2, 4);
                    const a = [];
                    for (let v of x)
                        a.push(v);
                    assert(_.isEqual(a, [2, 3]));}});

        it('test4',
            function () {
                for (let f of a) {
                    const x = f(2, 5);
                    assert(x[0] === 2);
                    assert(x[1] === 3);
                    assert(x[2] === 4);}});});
