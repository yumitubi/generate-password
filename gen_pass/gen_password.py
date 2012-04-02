# -*- coding: utf-8 -*-
#------------------------------------------------------------
# генератор словарей
#------------------------------------------------------------

from gen_dict import gen_dict_fsmb
from gen_dict import gen_dict_othsmb
import random

sfile = '/home/mak/devel/scripts/old_work/gen_pass/pereraboka.txt'
dict_first = gen_dict_fsmb(sfile)
dict_sec = gen_dict_othsmb(sfile)

def gen_pass(dict_f, dict_s):
    """generate password
    
    Arguments:
    - `dict_f`: dictionary first two symbols
    - `dict_s`: dictionary all other symbols
    """
    # password = ''
    list_f = []
    for k, v in dict_f.items():
        for p in range(v):
            list_f.append(k)
    f_st = random.sample(list_f, 1)[0]
    print f_st
    list_s = []
    pr_st = f_st
    for ch_smb in range(10):
        for k, v in dict_s.items():
            if k == pr_st:
                for k2, v2 in v.items():
                    for p2 in range(v2):
                        list_s.append(p2)
            else:
                
            print list_s
            f_st = f_st + random.sample(list_s, 1)[0]
            pr_st = f_st[-1:]
    print f_st
    
gen_pass(dict_first, dict_sec)
    
