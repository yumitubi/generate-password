# -*- coding: utf-8 -*-
#------------------------------------------------------------
# генератор словарей
#------------------------------------------------------------
 
import string
import sys
import os
import re

def gen_dict():
    """generate dictionary symbols
    
    Arguments:
    - `file`: source
    """
    re_patt = re.compile('[A-Za-z]')
    openfile = open('/home/mak/devel/scripts/old_work/gen_pass/pereraboka.txt', 'r')
    file_r = openfile.readlines()
    dict_alfavit = { 'a':0,  'b':1,  'c':2,  'd':3,  'e':4,
                     'f':5,  'g':6,  'h':7,  'i':8,  'j':9,
                     'k':10, 'l':11, 'm':12, 'n':13, 'o':14,
                     'p':15, 'q':16, 'r':17, 's':18, 't':19,
                     't':20, 'u':21, 'v':22, 'w':23, 'x':24,
                     'y':25, 'z':26 }
    dict_words   = { 'a':[], 'b':[], 'c':[], 'd':[], 'e':[],
                     'f':[], 'g':[], 'h':[], 'i':[], 'j':[],
                     'k':[], 'l':[], 'm':[], 'n':[], 'o':[],
                     'p':[], 'q':[], 'r':[], 's':[], 't':[],
                     't':[], 'u':[], 'v':[], 'w':[], 'x':[],
                     'y':[], 'z':[] }
    for i in dict_words:
        dict_words[i] = [ 0 for t in xrange(0, 27) ]
    old_s = 's'
    for st in file_r:
       for smb in st:
           if re_patt.findall(smb):
               z = dict_alfavit[smb.lower()]
               print z
               dict_words[old_s.lower()][z]+=1
               old_s = smb
    return dict_words


def get_passwd():
    """generate paswd
    """
    dict_words = gen_dict()

    dict_summ =    { 'a':0, 'b':0, 'c':0, 'd':0, 'e':0,
                     'f':0, 'g':0, 'h':0, 'i':0, 'j':0,
                     'k':0, 'l':0, 'm':0, 'n':0, 'o':0,
                     'p':0, 'q':0, 'r':0, 's':0, 't':0,
                     't':0, 'u':0, 'v':0, 'w':0, 'x':0,
                     'y':0, 'z':0 }
    for i in dict_words:
        for p in dict_words[i]:
            dict_summ[i] = dict_summ[i] + dict_words[i].index(p)
