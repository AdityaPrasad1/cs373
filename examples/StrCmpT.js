#!/usr/bin/env node

/* global
    describe,
    it
*/

/* jshint
    esversion: 6
*/

// ----------
// StrCmpT.js
// ----------

"use strict";

const assert = require('assert');

function strcmp (s, t) {
    return (s > t) - (s < t);}

describe('strcmp',
    function () {
        it('test1',
            function () {
                assert(strcmp("", "") == 0);});

        it('test2',
            function () {
                assert(strcmp("abc", "abc") == 0);});

        it('test3',
            function () {
                assert(strcmp("abc", "ab") > 0);});

        it('test4',
            function () {
                assert(strcmp("abc", "aba") > 0);});

        it('test5',
            function () {
                assert(strcmp("ab", "abc") < 0);});

        it('test6',
            function () {
                assert(strcmp("aba", "abc") < 0);});});
