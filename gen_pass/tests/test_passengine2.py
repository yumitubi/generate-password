#!/usr/bin/env python3
# coding: utf-8


import json


from collections import Counter
from passengine2 import gen_noexist_rules
from passengine2 import gen_prefix_rules
from passengine2 import rand_element
from genpassword import random_element
from passengine2 import gen_password
from passengine2 import next_symbol


TEXT_FILE = 'tests/some_text.txt'


def test_gen_except_smb():

    with open(TEXT_FILE, 'r') as text_fp:
        data_passengine2 = gen_noexist_rules(text_fp.read())

    with open('tests/expect_symbols.json', 'r') as json_expect:
        json_data = json.load(json_expect)

    assert data_passengine2 == json_data


def test_gen_all_one_symbols():

    with open(TEXT_FILE, 'r') as text_fp:
        data_passengine2 = gen_prefix_rules(text_fp.read())

    with open('tests/expect_all_one.json') as json_expect:
        json_data = json.load(json_expect)

    assert data_passengine2 == json_data


def test_get_random_element():

    data = {
        'a': 33,
        'b': 44,
        'c': 12,
        'd': 1,
        'h': 10
    }

    c = Counter()

    for i in range(10001):
        c[rand_element(data)] += 1

    assert 3100 < c['a'] < 3500
    assert 4200 < c['b'] < 4500
    assert 1000 < c['c'] < 1400
    assert 0 < c['d'] < 300
    assert 800 < c['h'] < 1200

    c = Counter()

    for i in range(10001):
        c[random_element(data)] += 1

    assert 3100 < c['a'] < 3500
    assert 4200 < c['b'] < 4500
    assert 1000 < c['c'] < 1400
    assert 0 < c['d'] < 300
    assert 800 < c['h'] < 1200


def test_gen_password():

    with open('tests/rules.json') as rules_fp:
        rules = json.load(rules_fp)

    password = gen_password(rules, 10)
    assert isinstance(password, str)
    assert len(password) == 10
    assert password.isalpha()
    

def test_next_symbol():

    with open('tests/rules.json') as rules_fp:
        rules = json.load(rules_fp)

    symbol = next_symbol(rules, 'NONENONE')
    assert len(symbol) == 1
    assert symbol.isalpha()

    symbol = next_symbol(rules, 'BadKey')
    assert len(symbol) == 1
    assert symbol.isalpha()
