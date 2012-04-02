# -*- coding: utf-8 -*-
#------------------------------------------------------------
# генератор пароля
#------------------------------------------------------------

import random
    
def gen_pass(dict_f, dict_s, dict_r, dict_o, len_pass):
    """generate password
    
    Arguments:
    - `dict_f`: dictionary first two symbols ~ {'gu': 7, 'gr': 20, 'ge': 7, 'ga': 8}
    - `dict_s`: dictionary all other symbols ~ {'ab':{'c':1, 'm':2}, 'bc':{'d':1}}
    - `dict_r`: dictionary all other random symbols ~ {'a':1, 'm':2}
    - `dict_o`: dictionary alone symbols ~ {'a':{'c':1, 'm':2}, 'b':{'d':1}}    
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
        if dict_s.has_key(pr_st): # если имеется совпадение с ключем из двух символов
            for k, v in dict_s[pr_st].items():
                for p in range(v):
                    list_s.append(k)
            f_st = f_st + random.sample(list_s, 1)[0]
            pr_st = f_st[-2:]
            list_s = []
        elif dict_o.has_key(f_st[-1:]): # если имеются совпадение с ключем из одного символа
            for k2, v2 in dict_o[f_st[-1:]].items():
                for p in range(v2):
                    list_s.append(k2)
            f_st = f_st + random.sample(list_s, 1)[0]
            pr_st = f_st[-2:]
            list_s = []
        else: # если нет совпадений, то random с учетом предыдущего символа
            first_smb = f_st[-1:]
            print 'first smb %s' % first_smb
            sec_smb = random.sample(list_r, 1)[0]
            while first_smb == sec_smb:
                sec_smb = random.sample(list_r, 1)[0]
            f_st = f_st + sec_smb
            pr_st = f_st[-2:]
        itr = itr + 1
    return f_st

    
