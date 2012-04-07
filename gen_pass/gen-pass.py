#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Консольная утилита для генерации паролей 
# на основе создания правил после анализац текста
#------------------------------------------------------------

import genpassword
import argparse

parser = argparse.ArgumentParser(description='Генератор паролей')
parser.add_argument('-c', '--create-dict', metavar='name_file', 
                    help='Создает словарь и записывает его в указанный файл')
parser.add_argument('-f', '--from-file', metavar='name_file',
                    help='Указывает, из какого файла брать текст для составления словаря')
parser.add_argument('-d', '--dict-pass', metavar='name_dictionary',
                    help='Выбрает словарь, на основе которого будет сгенерирован пароль')
parser.add_argument('-l', '--lenth-pass', metavar='N', type=int, default=9,
                    help='Указать длину пароля, поумолчанию - 9 символов')

args = parser.parse_args()

print args.create_dict
print args.from_file
print args.dict_pass
print args.lenth_pass

if args.create_dict and args.from_file:
    liststring = genpassword.read_file(args.from_file)
    print 'Генерация словаря...'
    dict_pass = genpassword.dict_pass_rules(liststring)
    genpassword.save_dict_in_file(dict_pass, args.create_dict)
    print 'Словарь был сохранен в файл ' + args.create_dict

if args.dict_pass:
    print 'Загружаю словарь...'
    dict_rules = genpassword.get_dict_from_file(args.dict_pass)
    print 'Генерация пароля начата...'
    print 'Ваш новый пароль: ' 
    print genpassword.gen_password(dict_rules, args.lenth_pass)

