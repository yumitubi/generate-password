# coding: utf-8


import random


from collections import Counter
from collections import defaultdict


def gen_noexist_rules(text):
    '''Generate dict with symols without combinations.
    '''
    symbols = [s for s in text.lower() if s.isalpha()]
    return dict(Counter(symbols))


def gen_prefix_rules(text, max_weight_coef=2.5):
    '''Generate dictionary with keys, where symbol NONE is empty symbol.'''

    combinations = defaultdict(lambda: Counter()) # noqa

    first, second = 'NONE', 'NONE'

    for symbol in text.lower():

        if symbol.isspace():
            first, second = 'NONE', 'NONE'
            continue

        if symbol.isalpha():
            key = first + second
            first, second = second, symbol
            combinations[key][symbol] += 1

    for d in combinations.values():
        mean = sum(d.values()) / len(d)
        max_value = int(mean * max_weight_coef)

        for k, v in d.items():
            if v > max_value:
                d[k] = max_value

    return {k: dict(v) for k, v in combinations.items()}


def gen_pass_rules(text):
    '''Make rules for password gen functions.'''
    return {
        'not_found': gen_noexist_rules(text),
        'all_on_one': gen_prefix_rules(text)
    }


def rand_element(dicti):
    '''Return random element based on its weight.'''

    random_num = random.uniform(0, sum(dicti.values()))

    for k, v in dicti.items():
        if random_num < v:
            return k
        random_num -= v
        last = k

    return last


def next_symbol(dicti, prefix):
    '''Get next symbol from dict with rules.'''

    subdict = dicti['all_on_one'].get(prefix)

    if subdict is not None:
        return rand_element(subdict)

    return rand_element(dicti['not_found'])


def gen_password(dicti, pass_length):
    '''It generates password based on rules.'''

    assert 'all_on_one' in dicti
    assert 'not_found' in dicti

    password = next_symbol(dicti, 'NONENONE')
    password += next_symbol(dicti, 'NONE' + password)

    while len(password) < pass_length:
        password += next_symbol(dicti, password[-2:])

    return password
