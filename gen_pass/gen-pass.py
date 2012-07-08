#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Консольная утилита для генерации паролей 
# на основе создания правил после анализац текста
#------------------------------------------------------------

import genpassword
import argparse
import random

p = 0.00001

parser = argparse.ArgumentParser(description='Генератор паролей')
parser.add_argument('-c', '--create-dict', metavar='name_file', 
                    help='Создает словарь и записывает его в указанный файл')
parser.add_argument('-f', '--from-file', metavar='name_file',
                    help='Указывает, из какого файла брать текст для составления словаря')
parser.add_argument('-d', '--dict-pass', metavar='name_dictionary',
                    help='Выбрает словарь, на основе которого будет сгенерирован пароль')
parser.add_argument('-v', '--generate-version', metavar='N', type=int, default=1,
                    help='Использовать новый алгоритм генерации пароля')
parser.add_argument('-l', '--lenth-pass', metavar='N', type=int, default=10,
                    help='Указать длину пароля, поумолчанию - 9 символов')
parser.add_argument('-p', '--probability', metavar='N', default=p,
                    help='указать допустимую вероятность')

args = parser.parse_args()

if args.create_dict and args.from_file:
    liststring = genpassword.read_file(args.from_file)
    print 'Генерация словаря...'
    dict_pass = genpassword.dict_pass_rules(liststring)
    genpassword.save_dict_in_file(dict_pass, args.create_dict)
    print 'Словарь был сохранен в файл ' + args.create_dict

if args.dict_pass and args.generate_version == 1:
    dict_rules = genpassword.get_dict_from_file(args.dict_pass)
    print genpassword.gen_password(dict_rules, args.lenth_pass)

if args.dict_pass and args.generate_version == 2:
    dict_rules = genpassword.get_dict_from_file(args.dict_pass)
    print genpassword.gen_password_with_none(dict_rules, args.lenth_pass)
    
if args.dict_pass and args.generate_version == 3 and args.probability:
    dict_rules = genpassword.get_dict_from_file(args.dict_pass)
    password, probability = genpassword.gen_password_verification_probability(dict_rules, args.lenth_pass)
    print probability
    print args.probability
    if probability < args.probability:
        print password
    elif random.uniform(0, 99) == 50:
        print password
    else:
        print "неудача"
