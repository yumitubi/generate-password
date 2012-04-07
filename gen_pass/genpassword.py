# -*- coding: utf-8 -*-
#------------------------------------------------------------
# генератор словарей
#------------------------------------------------------------
"""
This is set of functions ...
""" 

import re
import json
import random

def read_file(source_file):
    """open file for get list of strings
    Arguments:
    - `source_file`: source file
    """
    with open(source_file, 'r') as openfile:
        return openfile.readlines()

def save_dict_in_file(dict_json, name_file):
    """ save dictionary in file
    Arguments:
    - `dict_json`: dictionary of format json
    - `dict_json`: name file for save to hard
    """
    json.dump(dict_json, open(name_file, 'w'))

def get_dict_from_file(name_file):
    """load dictionary from file on the hard
    Arguments:
    - `name_file`: source file where store the dictionary
    """
    data = json.load(open(name_file, 'r'))
    return data

def gen_dict_first_smbs(liststring):
    """generate dictionary first and second symbols
    Arguments:
    - `liststring`: list of string
    """
    dict_fsmb = {} # словарь первых двух символов
    key_dict = ''
    re_patt = re.compile('[A-Za-z]')
    #------------------------------------------------------------
    # генерим словарь вида {'gu': 7, 'gr': 20, 'ge': 7, 'ga': 8}
    #------------------------------------------------------------        
    for st in liststring:
        for smb in st:
            if smb == ' ' or smb == '\n' or smb == '\t':
                key_dict = ''
            if re_patt.findall(smb):
                key_dict = key_dict + smb.lower()
                if len(key_dict) == 2:
                    if dict_fsmb.has_key(key_dict):
                        dict_fsmb[key_dict] += 1
                    else:
                        dict_fsmb[key_dict] = 1
    return dict_fsmb

def gen_dict_other_smb(liststring):
    """generate dictionary other symbols
    Arguments:
    - `liststring`: list of string
    """
    dict_othsmb = {} # словарь правил для остальных двойных символов
    key_dict = ''
    re_patt = re.compile('[A-Za-z]')
    #------------------------------------------------------------
    # генерим словарь вида {'ab':{'c':1, 'm':2}, 'bc':{'d':1}}
    #------------------------------------------------------------
    for st in liststring:
        for smb in st:
            if smb == ' ' or smb == '\n' or smb == '\t':
                key_dict = ''
            if re_patt.findall(smb):
                key_dict = key_dict + smb.lower()
                if len(key_dict) > 2:
                    d_smb = key_dict[-3:-1]
                    if dict_othsmb.has_key(d_smb):
                        if dict_othsmb[d_smb].has_key(smb):
                            dict_othsmb[d_smb][smb] += 1
                        else:
                            dict_othsmb[d_smb][smb.lower()] = 1
                    else:
                        dict_othsmb[d_smb] = { smb.lower():1 }
    return dict_othsmb

def gen_dict_one_smb(liststring):
    """generate dictionary if one symbols in prev dictionary
    Arguments:
    - `liststring`: list of string
    """
    dict_one_smb = {} # словарь правил для одного символа
    key_dict = ''
    re_patt = re.compile('[A-Za-z]')
    #------------------------------------------------------------
    # генерим словарь вида {'a':{'c':1, 'm':2}, 'b':{'d':1}}
    #------------------------------------------------------------
    for st in liststring:
        for smb in st:
            if smb == ' ' or smb == '\n' or smb == '\t':
                key_dict = ''
            if re_patt.findall(smb):
                key_dict = key_dict + smb.lower()
                if len(key_dict) > 1:
                    o_smb = key_dict[-2:-1]
                    if dict_one_smb.has_key(o_smb):
                        if dict_one_smb[o_smb].has_key(smb):
                            dict_one_smb[o_smb][smb] += 1
                        else:
                            dict_one_smb[o_smb][smb.lower()] = 1
                    else:
                        dict_one_smb[o_smb] = { smb.lower():1 }
    return dict_one_smb

def gen_dict_except_smb(liststring):
    """generate dictionary symbols where is not found combinations
    Arguments:
    - `liststring`: list of string
    """
    dict_smb = {} # словарь для получения рандомных символов
    re_patt = re.compile('[A-Za-z]')
    #------------------------------------------------------------
    # генерим словарь вида {'a':1, 'm':2}
    #------------------------------------------------------------
    for st in liststring:
        for smb in st:
            if re_patt.findall(smb):
                if dict_smb.has_key(smb):
                    dict_smb[smb] += 1
                else:
                    dict_smb[smb.lower()] = 1
    return dict_smb
    
def dict_pass_rules(liststring):
    """ Create dictionary rules for generate passwords
    Arguments:
    - `liststring`: list of string
    """
    main_dict = {}
    main_dict['first_two_smb'] = gen_dict_first_smbs(liststring)
    main_dict['next_smb'] = gen_dict_other_smb(liststring)
    main_dict['next_smb_if_one'] = gen_dict_one_smb(liststring)
    main_dict['not_found'] = gen_dict_except_smb(liststring)
    return main_dict

def random_element(dictionary):
    """ Return random key from dictionary with a light weight
    Arguments:
    - `dictionary`: dictionary type - { 'a':45, 'b':78, 'c':98 }
    """
    total = sum(dictionary.values())
    random_num = random.uniform(0, total)
    for key in sorted(dictionary.keys()):
        item = key
        if random_num < dictionary[key]:
            break
        random_num -= dictionary[key]
    return item

def gen_password(main_dict, lenth_pass):
    """generate password
    Arguments:
    - `main_dict`: main dictionary include all all mini dictionaries    
    - `lenth_pass`: lenth of pass
    """
    password = random_element(main_dict['first_two_smb'])
    dict_next_smb = main_dict['next_smb']
    dict_smb_if_one = main_dict['next_smb_if_one']
    last_smbs = password
    while len(password) < lenth_pass:
        if dict_next_smb.has_key(last_smbs):
            password = password + random_element(dict_next_smb[last_smbs])
            last_smbs = password[-2:]
        elif dict_smb_if_one.has_key(last_smbs[-1:]):
            password = password + random_element(dict_smb_if_one[last_smbs[-1:]])
            last_smbs = password[-2:]
        else:
            password = password + random_element(main_dict['not_found'])
            last_smbs = password[-2:]
    return password
