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

#------------------------------------------------------------
# Генерация словарей
#------------------------------------------------------------
def gen_dict_except_smb(liststring):
    """generate dictionary symbols where is not found combinations
    Arguments:
    - `liststring`: list of string
    """
    # словарь для получения рандомных символов
    # в дальнейшем он используется, если сгенерированной комбинации
    # ненайдено в основном словаре
    dict_smb = {} 
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

def gen_dict_all_on_one(liststring, max_value=2.5):
    """generate dictionary symbols, where simbol NONE is empty symbol
    example, in begin word
    Arguments:
    - `liststring`: list of string
    - `max_value`: maximum value 
    """
    dict_with_none_smb = {}
    key_dict = ''
    valua_dict = ('NONE', 'NONE')
    re_patt = re.compile('[a-z]')
    #-------------------------------------------------------------------
    # генерируем словарь вида { ab:{c:2, k:7}, NONEc:{d:3}, NONENONE:{s:8, t:9} }
    #-------------------------------------------------------------------
    # Алгоритм примерно такой:
    # Если пробел, ввод или таб - сбрасываем значение переменных
    # Если это буква из латиницы, то если ключ уже есть в словаре, 
    # делаем плюс к весам, если нет, то делаем новый ключ с весами = 1
    #-------------------------------------------------------------------
    for string in liststring:
        for symbol in string:
            if symbol == ' ' or symbol == '\n' or symbol == '\t':
                key_dict = ''
                valua_dict = ('NONE', 'NONE')
            symbol_lower = symbol.lower()
            if re_patt.findall(symbol_lower):
                key_dict = valua_dict[0] + valua_dict[1]
                valua_dict = (valua_dict[1], symbol_lower)
                if dict_with_none_smb.has_key(key_dict):
                    if dict_with_none_smb[key_dict].has_key(symbol_lower):
                        dict_with_none_smb[key_dict][symbol_lower] += 1
                    else:
                        dict_with_none_smb[key_dict][symbol_lower] = 1
                else:
                    dict_with_none_smb[key_dict] = { symbol_lower:1}
    #------------------------------------------------------------
    # сглаживаем особо большое значение весов у некоторых комбинаций
    # это позволяет уменьшить число повторяемых паролей
    #------------------------------------------------------------
    summa = 0
    middle_value = 0
    counter = 0
    for key in dict_with_none_smb:
        for key2 in dict_with_none_smb[key]:
            summa += dict_with_none_smb[key][key2]
            counter += 1
        middle_value = summa/counter
        for key2 in dict_with_none_smb[key]:
            if dict_with_none_smb[key][key2] > middle_value*max_value:
                dict_with_none_smb[key][key2] = middle_value*max_value
        summa = 0
        counter = 0
        middle_value = 0
    return dict_with_none_smb

def dict_pass_rules(liststring):
    """ Create dictionary rules for generate passwords
    Arguments:
    - `liststring`: list of string
    """
    main_dict = {}
    main_dict['not_found'] = gen_dict_except_smb(liststring)
    main_dict['all_on_one'] = gen_dict_all_on_one(liststring)
    return main_dict

def random_element(dictionary):
    """ Return random key from dictionary with a light weight
    Arguments:
    - `dictionary`: dictionary type - { 'a':45, 'b':78, 'c':98 }
    """
    # Возвращает рандомный элемент с учетом его веса 
    total = sum(dictionary.values())
    random_num = random.uniform(0, total)
    for key in sorted(dictionary.keys()):
        item = key
        if random_num < dictionary[key]:
            break
        random_num -= dictionary[key]
    return item

#------------------------------------------------------------
# Функции генерации паролей
#------------------------------------------------------------
def gen_password_with_none(main_dict, lenth_pass):
    """generate password on base main_dict['all_on_one']
    Arguments:
    - `main_dict`: main dictionary include all all mini dictionaries    
    - `lenth_pass`: lenth of pass
    """
    password = random_element(main_dict['all_on_one']['NONENONE'])
    two_symbol = 'NONE' + password
    if main_dict['all_on_one'].has_key(two_symbol):
        password = password + random_element(main_dict['all_on_one'][two_symbol])
    else:
        password = password + random_element(main_dict['not_found'])
    next_symbols = password
    while len(password) < lenth_pass:
        if main_dict['all_on_one'].has_key(next_symbols):
            password = password + random_element(main_dict['all_on_one'][next_symbols])
            next_symbols = password[-2:]
        else:
            password = password + random_element(main_dict['not_found'])
            next_symbols = password[-2:]
    return password

#------------------------------------------------------------
# вспомогательные функции
#------------------------------------------------------------
def test_dictionary(num_pass, dictionary, file_pass, lenth_pass):
    """generate big numbers of passwords in file
    Arguments:
    - `num_pass`: number passwords
    - `dictionary`: dictionary file
    - `file_pass`: there save passwords
    - `lenth_pass`: lenth password
    """
    # пишет в файл заданное количество паролей, хоть миллион
    import time
    start = time.time()
    pfile = open(file_pass, 'w')
    dicts = get_dict_from_file(dictionary)
    for i in range(num_pass):
        password = gen_password_with_none(dicts, lenth_pass)
        pfile.write(password + '\n')
    pfile.close()
    finish = time.time()
    print "Сгенерировано за %s секунд." % (finish - start)

def info_passwords(name_file, num_last_password):
    """return information about passwords
    Arguments:
    - `name_file`: name of file passwords
    """
    # возвращает некоторую информацию о сгенерированных в файле паролях
    # такую, как количество паролей, и выводит список наиболее повторяющихся
    import os
    
    num_string = 0
    pfile = open(name_file, 'r')
    for string in pfile.readlines():
        num_string += 1
    print "Количество паролей: %s" % num_string
    pfile.close()
    print "Последних в списке %s повторяющихся паролей" % num_last_password 
    os.system('cat %s | sort -n | uniq -c | sort -n | tail -n %s' % (name_file, num_last_password))
