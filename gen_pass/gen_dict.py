# -*- coding: utf-8 -*-
#------------------------------------------------------------
# генератор словарей
#------------------------------------------------------------
 
import re
import json

def opfile(sfile):
    """open file for get string
    Arguments:
    - `sfile`: source file
    """
    with open(sfile, 'r') as openfile:
        return openfile.readlines()

def gen_dict_fsmb(sfile, dfile):
    """generate dictionary first and second symbols
    
    Arguments:
    - `sfile`: source file for dictionary
    - `dfile`: distonation for save in json
    """
    dict_fsmb = {} # словарь первых двух символов
    key_dict = ''
    re_patt = re.compile('[A-Za-z]')
    #------------------------------------------------------------
    # генерим словарь вида {'gu': 7, 'gr': 20, 'ge': 7, 'ga': 8}
    #------------------------------------------------------------        
    for st in opfile(sfile):
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
    try:
        json.dump(dict_fsmb, open(dfile+'_fsmb.dic', 'w'))
        return 'Генерация словаря: ' + dfile + '_fsmb.dic' + 'Завершена'
    except IOError:
        return 'При генерация словаря: ' + dfile + '_fsmb.dic' + 'Произошла ошибка.'
        

def gen_dict_othsmb(sfile, dfile):
    """generate dictionary other symbols

    Arguments:
    - `sfile`: source file for dictionary
    - `dfile`: distonation for save in json
    """
    dict_othsmb = {} # словарь правил для остальных двойных символов
    key_dict = ''
    re_patt = re.compile('[A-Za-z]')
    #------------------------------------------------------------
    # генерим словарь вида {'ab':{'c':1, 'm':2}, 'bc':{'d':1}}
    #------------------------------------------------------------
    for st in opfile(sfile):
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
    try:
        json.dump(dict_othsmb, open(dfile+'_othsmb.dic', 'w'))
        return 'Генерация словаря: ' + dfile + '_othsmb.dic ' + 'завершена'
    except IOError:
        return 'При генерация словаря: ' + dfile + '_othsmb.dic ' + 'произошла ошибка.'

def gen_dict_one_s(sfile, dfile):
    """generate if one symbols in prev dictionary

    Arguments:
    - `sfile`: source file for dictionary
    - `dfile`: distonation for save in json
    """
    dict_one_smb = {} # словарь правил для одного символа
    key_dict = ''
    re_patt = re.compile('[A-Za-z]')
    #------------------------------------------------------------
    # генерим словарь вида {'a':{'c':1, 'm':2}, 'b':{'d':1}}
    #------------------------------------------------------------
    for st in opfile(sfile):
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
    try:
        json.dump(dict_one_smb, open(dfile+'_one_smb.dic', 'w'))
        return 'Генерация словаря: ' + dfile + '_one_smb.dic ' + 'завершена'
    except IOError:
        return 'При генерация словаря: ' + dfile + '_one_smb.dic ' + 'произошла ошибка.'

def gen_dict_exc(sfile, dfile):
    """generate dictionary symbols where is not in combination

    Arguments:
    - `sfile`: source file for dictionary
    - `dfile`: distonation for save in json
    """
    dict_smb = {} # словарь для получения рандомных символов
    re_patt = re.compile('[A-Za-z]')
    #------------------------------------------------------------
    # генерим словарь вида {'a':1, 'm':2}
    #------------------------------------------------------------
    for st in opfile(sfile):
        for smb in st:
            if re_patt.findall(smb):
                if dict_smb.has_key(smb):
                    dict_smb[smb] += 1
                else:
                    dict_smb[smb.lower()] = 1
    try:
        json.dump(dict_smb, open(dfile+'_smb.dic', 'w'))
        return 'Генерация словаря: ' + dfile + '_smb.dic ' + 'завершена'
    except IOError:
        return 'При генерация словаря: ' + dfile + '_smb.dic ' + 'произошла ошибка.'
    
