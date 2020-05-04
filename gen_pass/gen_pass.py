#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import argparse


from passengine2 import gen_password
from passengine2 import gen_pass_rules
from utils import as_string
from utils import save_rules
from utils import load_rules
from utils import gen_passwords2file


parser = argparse.ArgumentParser(description='Генератор паролей')
parser.add_argument(
    '-c', '--create-rules', metavar='name_file',
    help='Создает словарь с правилами и записывает его в указанный файл'
)
parser.add_argument(
    '-f', '--from-file', metavar='name_file',
    help='Указывает, из какого файла брать текст для составления словаря'
)
parser.add_argument(
    '-r', '--rules', metavar='name_file_with_rules',
    help='Выбрает словарь, на основе которого будет сгенерирован пароль'
)
parser.add_argument(
    '-l', '--pass-length', metavar='N', type=int, default=10,
    help='Указать длину пароля, поумолчанию - 10 символов'
)
parser.add_argument(
    '-t', '--pass-count', metavar='N', type=int, default=10,
    help='Указать, какое количество паролей сгенерировать для теста, по умолчанию - 10'
)
parser.add_argument(
    '-s', '--save-pass', metavar='name_file',
    help='Указать, в какой файл сохранить сгенерированные пароли'
)


args = parser.parse_args()


if args.create_rules and args.from_file:
    print('Генерация словаря...')
    pass_rules = gen_pass_rules(as_string(args.from_file))
    save_rules(pass_rules, args.create_rules)
    print('Словарь был сохранен в файл ' + args.create_rules)


if args.rules and args.save_pass is None:
    rules = load_rules(args.rules)
    for i in range(args.pass_count):
        print(gen_password(rules, args.pass_length))

if args.save_pass and args.rules:
    rules = load_rules(args.rules)
    gen_passwords2file(args.pass_count, rules, args.save_pass, args.pass_length)
    print("Сгенерировано %s паролей" % args.pass_count)

