# coding: utf

import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))


d = open ('dict_utf.txt', 'r')
#words = [line.split('\n') for line in d.readlines()]
words = d.readlines()