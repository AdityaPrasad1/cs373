#!/usr/bin/env node

/* global
    before,
    describe,
    it
*/

/* jshint
    esversion: 6
*/

// -------------
// FactorialT.js
// -------------

"use strict";

const assert = require('assert');
const _      = require('lodash');

function factorial_recursion (n) {
    assert(n >= 0);
    if (n < 2)
        return 1;
    return n * factorial_recursion(n - 1);}

function factorial_while (n) {
    assert(n >= 0);
    let v = 1;
    while (n > 1) {
        v *= n;
        n -= 1;}
    return v;}

function factorial_range_for (n) {
    assert(n >= 0);
    let v = 1;
    for (let i of _.range(1, n + 1))
        v *= i;
    return v;}

function factorial_range_iterator (n) {
    assert(n >= 0);
    let   v = 1;
    const r = _.range(1, n + 1);
    const p = r[Symbol.iterator]();
    while (true) {
        const n = p.next();
        if (n.done)
            break;
        const i = n.value;
        v *= i;}
    return v;}

function factorial_range_reduce_1 (n) {
    assert(n >= 0);
    return _.reduce(_.range(1, n + 1), (x, y) => {return x * y;}, 1);}

function factorial_range_reduce_2 (n) {
    assert(n >= 0);
    return _.reduce(_.range(1, n + 1), _.multiply, 1);}

describe('strcmp',
    function () {
        let a;

        before(function () {
            a = [
                factorial_recursion,
                factorial_while,
                factorial_range_for,
                factorial_range_iterator,
                factorial_range_reduce_1,
                factorial_range_reduce_2];});

        it('test1',
            function () {
                for (let f of a)
                    assert(f(0) == 1);});

        it('test2',
            function () {
                for (let f of a)
                    assert(f(1) == 1);});

        it('test3',
            function () {
                for (let f of a)
                    assert(f(2) == 2);});

        it('test4',
            function () {
                for (let f of a)
                    assert(f(3) == 6);});

        it('test5',
            function () {
                for (let f of a)
                    assert(f(4) == 24);});

        it('test6',
            function () {
                for (let f of a)
                    assert(f(5) == 120);});});
