#!/usr/bin/env node

/* global
    describe,
    it
*/

/* jshint
    esversion: 6
*/

// ------------
// Coverage2.js
// ------------

// https://gotwarlost.github.io/istanbul/

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
        it('test',
            function () {
                assert.equal(cycle_length(2), 2);});});

/*
% istanbul cover _mocha -- -u tdd Coverage2.js
  cycle_length
    ✓ test


  1 passing (5ms)

=============================================================================
Writing coverage object [/Users/downing/Dropbox/examples/javascript/coverage/coverage.json]
Writing coverage reports at [/Users/downing/Dropbox/examples/javascript/coverage]
=============================================================================

=============================== Coverage summary ===============================
Statements   : 92.86% ( 13/14 )
Branches     : 50% ( 1/2 )
Functions    : 100% ( 3/3 )
Lines        : 92.86% ( 13/14 )
================================================================================
*/
