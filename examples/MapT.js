#!/usr/bin/env node

/* global
    before,
    describe,
    it
*/

/* jshint
    esversion: 6
*/

// -------
// MapT.js
// -------

// https://www.w3schools.com/jsref/jsref_reduce.asp

"use strict";

const assert = require('assert');
const _      = require('lodash');

function my_map (a, uf) {
    let x = [];
    for (let v of a)
        x = x.concat(uf(v));
    return x;}

describe('map',
    function () {
        let a;

        before(function () {
            a = [
                my_map,
                _.map];});

        it('test1',
            function () {
                for (let f of a) {
                    const m = f([2, 3, 4], (x) => {return x * x;});
                    assert((typeof m) === "object");
                    assert(m instanceof Array);
                    assert(m instanceof Object);
                    assert(_.isEqual(m, [4, 9, 16]));
                    assert(_.isEqual(m, [4, 9, 16]));}});

        it('test2',
            function () {
                for (let f of a) {
                    const m = f([], null);
                    assert((typeof m) === "object");
                    assert(m instanceof Array);
                    assert(m instanceof Object);
                    assert(_.isEqual(m, []));}});});
