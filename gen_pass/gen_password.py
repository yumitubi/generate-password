# -*- coding: utf-8 -*-
#------------------------------------------------------------
# генератор словарей
#------------------------------------------------------------

from gen_dict import gen_dict_fsmb
from gen_dict import gen_dict_othsmb
from gen_dict import gen_dict_exc
from gen_dict import gen_dict_one_s
import random

sfile = '/home/mak/devel/scripts/old_work/gen_pass/pereraboka.txt'
dict_first = gen_dict_fsmb(sfile)
dict_sec = gen_dict_othsmb(sfile)
dict_ran = gen_dict_exc(sfile)
dict_one = gen_dict_one_s(sfile)

def gen_pass(dict_f, dict_s, dict_r, dict_o, len_pass):
    """generate password
    
    Arguments:
    - `dict_f`: dictionary first two symbols
    - `dict_s`: dictionary all other symbols
    - `dict_r`: dictionary all other random symbols
    - `dict_o`: dictionary alone symbols    
    - `len_pass`: lenth of pass
    """
    list_f = []
    for k, v in dict_f.items():
        for p in range(v):
            list_f.append(k)
    f_st = random.sample(list_f, 1)[0]
    list_s = []
    list_r = []
    pr_st = f_st
    # генерация списка для несуществующих в словаре комбинаций символов
    for k3, v3 in dict_r.items():
        for p3 in range(v3):
            list_r.append(k3)
    itr = 0
    while itr < len_pass:
        if dict_s.has_key(pr_st):
            for k, v in dict_s[pr_st].items():
                for p in range(v):
                    list_s.append(k)
            f_st = f_st + random.sample(list_s, 1)[0]
            pr_st = f_st[-2:]
            list_s = []
        elif dict_o.has_key(f_st[-1:]):
            for k2, v2 in dict_o[f_st[-1:]].items():
                for p in range(v2):
                    list_s.append(k2)
            f_st = f_st + random.sample(list_s, 1)[0]
            pr_st = f_st[-2:]
            list_s = []
        else:
            first_smb = f_st[-1:]
            print 'first smb %s' % first_smb
            sec_smb = random.sample(list_r, 1)[0]
            while first_smb == sec_smb:
                sec_smb = random.sample(list_r, 1)[0]
            f_st = f_st + sec_smb
            pr_st = f_st[-2:]
        itr = itr + 1
    print f_st
    
gen_pass(dict_first, dict_sec, dict_ran, dict_one, 10)
    
