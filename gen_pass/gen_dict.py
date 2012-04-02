# -*- coding: utf-8 -*-
#------------------------------------------------------------
# генератор словарей
#------------------------------------------------------------
 
import re

def gen_dict_fsmb(sfile):
    """generate dictionary symbols
    
    Arguments:
    - `file`: source
    """

    dict_fsmb = {} # словарь первых двух символов
    key_dict = ''
    re_patt = re.compile('[A-Za-z]')
    try:
        openfile = open(sfile, 'r')
        file_r = openfile.readlines()
    except:
        print 'Файл не существует'
    #------------------------------------------------------------
    # генерим словарь вида {'gu': 7, 'gr': 20, 'ge': 7, 'ga': 8}
    #------------------------------------------------------------        
    for st in file_r:
        for smb in st:
            if smb == ' ':
                key_dict = ''
            if re_patt.findall(smb):
                key_dict = key_dict + smb.lower()
                if len(key_dict) == 2:
                    if dict_fsmb.has_key(key_dict):
                        dict_fsmb[key_dict] += 1
                    else:
                        dict_fsmb[key_dict] = 1
    openfile.close()
    return dict_fsmb

def gen_dict_othsmb(sfile):
    """generate dictionary other symbols
    """
    dict_othsmb = {} #словарь правил для остальных символов
    key_dict = ''
    re_patt = re.compile('[A-Za-z]')
    try:
        openfile = open(sfile, 'r')
        file_r = openfile.readlines()
    except:
        print 'Файл не существует'
    #------------------------------------------------------------
    # генерим словарь вида {'ab':{'c':1, 'm':2}, 'bc':{'d':1}}
    #------------------------------------------------------------
    for st in file_r:
        for smb in st:
            if smb == ' ':
                key_dict = ''
            if re_patt.findall(smb):
                key_dict = key_dict + smb.lower()
                if len(key_dict) > 2:
                    d_smb = key_dict[-3:-1]
                    if dict_othsmb.has_key(d_smb):
                        if dict_othsmb[d_smb].has_key(smb):
                            dict_othsmb[d_smb][smb] += 1
                        else:
                            dict_othsmb[d_smb][smb] = 1
                    else:
                        dict_othsmb[d_smb] = { smb:1 }
    openfile.close()
    return dict_othsmb

def gen_dict_one_s(sfile):
    """generate if one symbols in prev dictionary
    """
    dict_one_smb = {} #словарь правил для остальных символов
    key_dict = ''
    re_patt = re.compile('[A-Za-z]')
    try:
        openfile = open(sfile, 'r')
        file_r = openfile.readlines()
    except:
        print 'Файл не существует'
    #------------------------------------------------------------
    # генерим словарь вида {'a':{'c':1, 'm':2}, 'b':{'d':1}}
    #------------------------------------------------------------
    for st in file_r:
        for smb in st:
            if smb == ' ':
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
    openfile.close()
    return dict_one_smb

def gen_dict_exc(sfile):
    """generate dictionary symbols where is not in combination
    """
    dict_smb = {}
    re_patt = re.compile('[A-Za-z]')
    try:
        openfile = open(sfile, 'r')
        file_r = openfile.readlines()
    except:
        print 'Файл не существует'
    #------------------------------------------------------------
    # генерим словарь вида {'a':1, 'm':2}
    #------------------------------------------------------------
    for st in file_r:
        for smb in st:
            if re_patt.findall(smb):
                if dict_smb.has_key(smb):
                    dict_smb[smb] +=1
                else:
                    dict_smb[smb.lower()] = 1
    return dict_smb
