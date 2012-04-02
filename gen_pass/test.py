# -*- coding: utf-8 -*-
#------------------------------------------------------------
# тесты
#------------------------------------------------------------

from gen_dict import gen_dict_fsmb
from gen_dict import gen_dict_othsmb
from gen_dict import gen_dict_exc
# from gen_password import gen_pass

sfile = '/home/mak/devel/scripts/old_work/gen_pass/pereraboka.txt'

def test_gen_dict(txt_file):
    dictionary = gen_dict_fsmb()
    return dictionary

def test_gen_dict2(txt_file):
    dictionary = gen_dict_othsmb()    
    return dictionary

def test_gen_dict3(txt_file):
    dictionary = gen_dict_exc(sfile)    
    return dictionary

# def test_gen_pass(dict_f):
#     return gen_pass()
# 
# dict1 = test_gen_dict(sfile)
# 
# print dict1
# password = test_gen_pass(dict1)
# print password

a = test_gen_dict3(sfile)
print a
