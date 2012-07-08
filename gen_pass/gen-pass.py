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
parser.add_argument('-l', '--lenth-pass', metavar='N', type=int, default=10,
                    help='Указать длину пароля, поумолчанию - 10 символов')
parser.add_argument('-t', '--generate-pass', metavar='N', type=int, default=1000,
                    help='Указать, какое количество паролей сгенерировать для теста, по умолчанию - 1000')
parser.add_argument('-s', '--save-pass', metavar='name_file', 
                    help='Указать, в какой файл сохранить сгенерированные пароли')
parser.add_argument('-i', '--info', metavar='name_file', 
                    help='Указать, информацию для какого файла паролей показать')
parser.add_argument('-n', '--last-pass', metavar='N', type=int, default=10,
                    help='Указать, какое количество паролей из наиболее часто дублирующихся показать, по умолчанию 10')

args = parser.parse_args()

if args.create_dict and args.from_file:
    liststring = genpassword.read_file(args.from_file)
    print 'Генерация словаря...'
    dict_pass = genpassword.dict_pass_rules(liststring)
    genpassword.save_dict_in_file(dict_pass, args.create_dict)
    print 'Словарь был сохранен в файл ' + args.create_dict

if args.dict_pass:
    dict_rules = genpassword.get_dict_from_file(args.dict_pass)
    print genpassword.gen_password_with_none(dict_rules, args.lenth_pass)
    
if args.save_pass:
    genpassword.test_dictionary(args.generate_pass, args.dict_pass, args.save_pass, args.lenth_pass)
    print "Сгенерировано %s паролей" % args.generate_pass

if args.info:
    genpassword.info_passwords(args.save_pass, args.last_pass)
