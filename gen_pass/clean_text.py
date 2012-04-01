# -*- coding: utf-8 -*-
#------------------------------------------------------------
# очищает исходный текст от всего лишнего, и записывает
# измененый текст в новый файл
#------------------------------------------------------------

import string
import os
import sys
import re

#------------------------------------------------------------
# ваяем регулярку
#------------------------------------------------------------
re_patt = re.compile('[A-Za-z\s]')

openfile = open('tolkien.txt', 'r')
readls = openfile.readlines()
open_write_f = open('pereraboka.txt', 'a+' )

for st in readls:
    for smb in st:
        if re_patt.findall(smb):
            open_write_f.write(smb)
print 'Готово'
openfile.close()
open_write_f.close()
