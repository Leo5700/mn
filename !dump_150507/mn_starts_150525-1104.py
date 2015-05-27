# coding: utf
# Python: 2.79

'''
    150525 == Подбор похожих слов


    Рейтинг:
    Можно так: каждая звёздочка - минус буква в совпадении. 
    Т.е. при выборе между 
    "слово" -> "слон" и "слива **", "слива" окажется в списке раньше.

    В словаре рейтинг может быть указан через любое число пробелов и табуляций:
    рейтинг *
    рейтинг             *
    рейтинг*

    TODO Написать каких-нибудь рекомендаций по поводу рейтинга.

    TODO Обеспечить ввод сразу нескольких слов
    000000 ==
'''

import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))


##############################################################################
##############################################################################

# Задаём слово
myWords = u'Семён семёнович'



# Выбираем минимальное число совпадающих букв
minNum = 2 # Обычно 2..3

# Задаём имя файла словаря
dictName = 'word_rus_150525.txt'

# Выбираем, учитывать ли рейтинг:
keepRating = True # Может быть True/False, 0/1

##############################################################################
##############################################################################


def printl(l):
    '''
    150507 == Функция для консоли Canopy.
    Печатаем список, содержащий кириллицу, как строки.
    Иначе вместо кириллицы печатается крокозябра.
    000000 ==
    '''
    for w in l: print w,
    print
#
def cleanString(S, space=' '):
    '''
    150525 == Функция удаляет из строки повторяющиеся пробелы, табуляции и пр.
    tags: =очистить =строку.
    Весь этот хлам превращается в "space".
    000000 ==
    '''
    return space.join(S.split())


# Проверяем существование словаря
abspath = os.path.abspath(__file__)
absdir = os.path.dirname(abspath)
absDictName = os.path.join(absdir, dictName)
if not os.path.exists(absDictName): 
    raise IOError(dictName+' is not exist')    


myWords = cleanString(myWord) # Чистим фразу от мусора
myWords = myWord.lower() # Переводим слова в нижний регистр



# Задаём имя файла для выходных данных, если нужно, создаём папку
outFilename = os.path.join(absdir, 'out_words', myWord+'.txt')
if not os.path.exists(os.path.dirname(outFilename)): 
    os.mkdir(os.path.dirname(outFilename))





# Читаем словарь
d = open (dictName, 'r')
words = []
for w in d.readlines():
    w = cleanString(w, '')
    w = unicode(w, 'utf')
    w = w.lower()
    words.append(w)
d.close()
words.sort()


# Считаем число совпадающих первых букв
myWordBeg = ''
trueWords = []
numChars = []
for c in myWord:
    myWordBeg += c
    for word in words:
        if word.startswith(myWordBeg):
            bonus = word.count('*') * keepRating
            numChars.append(len(myWordBeg) + bonus)
            trueWords.append(word)

# Сортируем полученные данные по релевантности
b = zip(numChars, trueWords)
b.sort(reverse=True)

# Выбираем наиболее релевантные данные с учётом рейтинга
trueWords1 = []
for i in xrange(len(b)-1):
    if b[i+1][1] != b[i][1]:
        if b[i][0] >= minNum:
            trueWords1.append(b[i][1])

# Убиваем повторяющиеся слова
trueWords2 = []
trueWords1.reverse()
for s, i in zip(trueWords1, range(len(trueWords1))):
    if trueWords1[i:].count(s) <= 1:
        trueWords2.append(s)
trueWords2.reverse()

# Что-то печатаем
print
print myWord, '\n'
print
printl(trueWords2)


# Пишем слова в файл
out = open(outFilename, 'w')
out.write(myWord.encode('utf')+'\n'*2)
for s in trueWords2:
    out.write(s.encode('utf')+' ')
out.close()
print '\nResult saved in "'+outFilename+'"'





##############################################################################
##############################################################################