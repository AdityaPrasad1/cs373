#!/usr/bin/env node

/* global
    describe,
    it
*/

/* jshint
    esversion: 6
*/

// -------------
// UnitTests3.js
// -------------

// http://mochajs.org

"use strict";

const assert = require('assert');

function cycle_length (n) {
    assert(n > 0);
    let c = 1;
    while (n > 1) {
        if ((n % 2) === 0) {
            n = n / 2;}
        else {
            n = (3 * n) + 1;}
        c += 1;}
    assert(c > 0);
    return c;}

describe('cycle_length',
    function () {
        it('test1',
            function () {
                assert.equal(cycle_length( 1), 1);});

        it('test2',
            function () {
                assert.equal(cycle_length( 5), 6);});

        it('test3',
            function () {
                assert.equal(cycle_length(10), 7);});});

/*
% mocha -u tdd UnitTests3.js
  cycle_length
    ✓ test1
    ✓ test2
    ✓ test3


  3 passing (6ms)
*/
