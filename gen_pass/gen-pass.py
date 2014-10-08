#!/usr/bin/env python3
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
parser.add_argument('-d', '--pass-dict', metavar='name_dictionary',
                    help='Выбрает словарь, на основе которого будет сгенерирован пароль')
parser.add_argument('-l', '--pass-length', metavar='N', type=int, default=10,
                    help='Указать длину пароля, поумолчанию - 10 символов')
parser.add_argument('-t', '--pass-count', metavar='N', type=int, default=10,
                    help='Указать, какое количество паролей сгенерировать для теста, по умолчанию - 10')
parser.add_argument('-s', '--save-pass', metavar='name_file',
                    help='Указать, в какой файл сохранить сгенерированные пароли')
parser.add_argument('-i', '--info', metavar='name_file',
                    help='Указать, информацию для какого файла паролей показать')
parser.add_argument('-n', '--last-pass', metavar='N', type=int, default=10,
                    help='Указать, какое количество паролей из наиболее часто дублирующихся показать, по умолчанию 10')

args = parser.parse_args()

if args.create_dict and args.from_file:
    liststring = genpassword.read_file(args.from_file)
    print('Генерация словаря...')
    pass_dict = genpassword.pass_dict_rules(liststring)
    genpassword.save_dict_in_file(pass_dict, args.create_dict)
    print('Словарь был сохранен в файл ' + args.create_dict)

if args.pass_dict:
    dict_rules = genpassword.get_dict_from_file(args.pass_dict)
    for i in range(args.pass_count):
        print(genpassword.gen_password_with_none(dict_rules, args.pass_length))

if args.save_pass:
    genpassword.test_dictionary(args.pass_count, args.pass_dict, args.save_pass, args.pass_length)
    print("Сгенерировано %s паролей" % args.pass_count)

if args.info:
    print(args.save_pass, args.last_pass)
    genpassword.info_passwords(args.info, args.last_pass)
