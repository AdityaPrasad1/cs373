#!/usr/bin/env node

/* global
    describe,
    it
*/

/* jshint
    esversion: 6
*/

// -------------
// UnitTests1.js
// -------------

// http://mochajs.org

"use strict";

const assert = require('assert');

function cycle_length (n) {
    assert(n > 0);
    let c = 0;
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
% which mocha
/usr/local/bin/mocha



% mocha --version
4.1.0



% mocha --help
...



% mocha UnitTests1.js
  cycle_length
    1) test1
    2) test2
    3) test3


  0 passing (7ms)
  3 failing

  1) cycle_length
       test1:

      AssertionError [ERR_ASSERTION]: false == true
      + expected - actual

      -false
      +true

      at cycle_length (UnitTests1.js:22:5)
      at Context.<anonymous> (UnitTests1.js:29:30)

  2) cycle_length
       test2:

      AssertionError [ERR_ASSERTION]: 5 == 6
      + expected - actual

      -5
      +6

      at Context.<anonymous> (UnitTests1.js:33:24)

  3) cycle_length
       test3:

      AssertionError [ERR_ASSERTION]: 6 == 7
      + expected - actual

      -6
      +7

      at Context.<anonymous> (UnitTests1.js:37:24)
*/
