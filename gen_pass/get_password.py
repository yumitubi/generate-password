# -*- coding: utf-8 -*-
#------------------------------------------------------------
# запускает генератор паролей и выводит полученный пароль
#------------------------------------------------------------

from gen_dict import gen_dict_fsmb, gen_dict_othsmb, gen_dict_exc, gen_dict_one_s
from gen_password import gen_pass
from conf import len_pass, sfile

def get_pass(sfile, len_pass):
    """generate password
    
    Arguments:
    - `sfile`: source file
    - `len_pass`: lenth password
    """
    dict_first = gen_dict_fsmb(sfile)
    dict_sec = gen_dict_othsmb(sfile)
    dict_ran = gen_dict_exc(sfile)
    dict_one = gen_dict_one_s(sfile)
    return gen_pass(dict_first, dict_sec, dict_ran, dict_one, len_pass)

if __name__ == '__main__':
    password = get_pass(sfile, len_pass)
    print password

    


