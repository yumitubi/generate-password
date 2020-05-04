# coding: utf-8


import json
import time


from passengine2 import gen_password


def as_string(path):

    with open(path, 'r') as fp:
        text = fp.read()

    return text


def save_rules(rules, path):

    with open(path, 'w') as fp:
        json.dump(rules, fp)


def load_rules(path):

    with open(path, 'r') as fp:
        return json.load(fp)


def how_much_time(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        stop = time.time()
        print(f'A Function {func.__name__} worked for {stop - start} seconds.')

    return wrapper

    
@how_much_time
def gen_passwords2file(num_pass, rules, path, length_pass):

    with open(path, 'w') as pass_fp:
        for _ in range(num_pass):
            pass_fp.write(gen_password(rules, length_pass) + '\n')
