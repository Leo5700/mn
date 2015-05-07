# coding: utf

'''
    150507 ==
    TODO получать слова из словаря (есть в проверке правописания)
         из него надо будет получать только существительные
    TODO написать трянслятор числа в буквы
    000000 ==
'''

import itertools
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))

def printl(l):
    '''
    150507 == Печатаем список, содержащий кириллицу в строку.
    Иначе в списке вместо кириллицы печатается крокозябра.
    000000 ==
    '''
    for w in l: print w,
    print

def numToChar(a):
    s = [u'р', u'бп', u'гк', u'зс', u'дт', u'жшщчцч', u'вф', u'м', u'л', u'н']
    f = []
    for c in str(a):
        f.append(s[int(c)])
    return f

d = open ('dict_utf_cut.txt', 'r')
d = open ('dict_utf_cut.txt', 'r')
words = []
for w in d.readlines():
    # print type(w) ###
    if w[-1] == '\n': w = w[:-1]
    words.append(unicode(w, 'utf'))

print '    words:'
printl(words)
sogl = [u'б',u'в',u'г',u'д',u'ж',u'з',u'к',u'л',u'м',u'н',u'п',u'р',u'с',u'т',u'ф',u'х',u'ц',u'ч',u'ш',u'щ']

print '    number:'
number = 114
print number
fChars = numToChar(number)
print '    fChars:'
printl(fChars)

# Удалим гласные
words2 = []
for word in words:
    word2 = ''
    for c in word:
        if c in sogl:
            word2 = word2 + c
    words2.append(word2)

# Получим возможные комбинации
fCharsComb = list(itertools.product(*fChars))
fCharsCombList = []
for fChar in fCharsComb:
    temp = ''
    for c in fChar:
        temp = temp + c
    fCharsCombList.append(temp)

print '    fCharsCombList:'
printl(fCharsCombList)

# Получим подходящие слова
trueWords = []
for fc in fCharsCombList:
    for sw in words2:
        if fc == sw[:len(fChars)]: trueWords.append(words[words2.index(sw)])

print '    trueWords:'
if trueWords: printl(trueWords)
else: print trueWords

