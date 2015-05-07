# coding: utf

import itertools

def printl(l):
    '''
    150507 == Печатаем список, содержащий кириллицу в строку.
    Иначе в списке вместо кириллицы печатается крокозябра.
    000000 ==
    '''
    for w in l: print w,
    print

words = ['qwer','asdf','zxcv', 'aqaartaatt', 'sadat', 'проверка']

printl(words)


# glas = ['e','y','u','i','o','a']
sogl = ['q','w','r','t','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m', 'п','р']

# fChars = ['s','dt']
fChars = ['п','р']
printl(fChars)

# Удалим гласные
words2 = []
for word in words:
    word2 = ''
    for c in word:
        if c in sogl:
            word2 = word2 + c
    words2.append(word2)

fCharsComb = list(itertools.product(*fChars))
fCharsCombList = []
for fChar in fCharsComb:
    temp = ''
    for c in fChar:
        temp = temp + c
    fCharsCombList.append(temp)

# print words2
# print fCharsCombList

trueWords = []
for fc in fCharsCombList:
    for sw in words2:
        if fc == sw[:len(fChars)]: trueWords.append(words[words2.index(sw)])

printl(trueWords)

