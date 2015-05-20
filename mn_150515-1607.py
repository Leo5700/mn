# coding: utf
# Python: 2.79

'''
    150507-1500 == Трансформируем число в код в соответствии с ключом, 
    получаем из словаря подходящие слова.

    Скрип работает под Windows и под Linux. Под Mac - не проверял.
    000000 ==
'''

import itertools
import os
from sys import platform as _platform
import sys
os.chdir(os.path.dirname(os.path.realpath(__file__)))




# Если скрипт запущен с параметром, используем *его* 
# в качестве числа для кодирования
if __name__ == "__main__":
    for param in sys.argv:
        number = param

##############################################################################
##############################################################################

# Задаём число для кодирования
if number[-3:] == '.py': # Если скрипт запущен без параметра, в sys.argv
                         # передаётся имя скрипта.
    number = '057' # Числа, начинающиеся с нуля, должны быть заданы строкой.


# Задаём код
key=[u'р', u'бп', u'гк', u'зс', u'дт', u'жшщчцч', u'вф', u'м', u'л', u'н']
                    # Нулевой элемент key - это цифра "0", первый - "1" и т.д.

# Задаём имя файла словаря
dictName = 'word_rus.txt'

##############################################################################
##############################################################################


# Проверяем существование словаря
abspath = os.path.abspath(__file__)
absdir = os.path.dirname(abspath)
absDictName = os.path.join(absdir, dictName)
if not os.path.exists(absDictName): 
    raise IOError(dictName+' is not exist')     

# Задаём имя файла для выходных данных
outFilename = os.path.join(absdir, 'out', str(number)+'.txt')

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
def numToChar(number, key=[u'р', u'бп', u'гк', u'зс', u'дт', u'жшщчцч', 
                                                u'вф', u'м', u'л', u'н']):
    '''
    150507 == Кодируем число в строку, используя ключ. 
              Нулевой элемент key - это цифра "0", первый - "1" и т.д.
    000000 ==
    '''
    a, s = number, key
    f = []
    for c in str(a): # str(a) - от дурака
        f.append(s[int(c)])
    return f

# Читаем словарь
d = open (dictName, 'r')
words = []
for w in d.readlines():
    w = w.replace("\r",""); w = w.replace("\n","") # Удаляем все концы строк
    words.append(unicode(w, 'utf'))

# Задаём согласные
sogl = [u'б',u'в',u'г',u'д',u'ж',u'з',u'к',u'л',u'м',u'н',
        u'п',u'р',u'с',u'т',u'ф',u'х',u'ц',u'ч',u'ш',u'щ']

print '    number:'
print number

# Кодируем номер буквами
fChars = numToChar(number, key)
print '    fChars:'
printl(fChars)

# Удаляем гласные из слов в словаре
words2 = []
for word in words:
    word2 = ''
    for c in word:
        if c in sogl:
            word2 = word2 + c
    words2.append(word2)

# Получаем возможные комбинации букв кода
fCharsComb = list(itertools.product(*fChars))
fCharsCombList = []
for fChar in fCharsComb:
    temp = ''
    for c in fChar:
        temp = temp + c
    fCharsCombList.append(temp)

print '    fCharsCombList:'
printl(fCharsCombList)

# Получаем из словаря подходящие слова
trueWords = []
for fc in fCharsCombList:
    for sw in words2:
        if fc == sw[:len(fChars)]: trueWords.append(words[words2.index(sw)])
        # FIXME перестать плодить дубликаты
trueWords = list(set(trueWords)) # Удаляем дубликаты
trueWords.sort()                 # Сортируем

print '    trueWords:'
if trueWords: 
    try: 
        printl(trueWords)
    except: 
        print '\n\nERROR with coding in DOS OEM 866. Shit. Try another console.' 
        print u'Попробуйте скопировать содержимое словаря в новый файл' 
        print u'НЕ блокнотом windows. Формат: Utf-8 без BOM' 
else: print trueWords

# Пишем слова в файл
out = open(outFilename, 'w')
out.write(str(number)+'\n'*2)
for s in fCharsCombList:
    out.write(s.encode('utf')+' ')
out.write('\n'*2)
for s in trueWords:
    out.write(s.encode('utf')+' ')
if not trueWords: out.write('Похоже, ничего не найдено.')
out.write('\n'*2)
for s in zip(range(len(key)), key):
    out.write(str(s[0])+' -- '+s[1].encode('utf')+'\n')
if number == 42:
    out.write('\n\n\nЯ в пятьдесят тысяч раз умнее Вас - и чего?..')
if number == 57:
    out.write('\n\n\nЕщё раз приносим извинения за несоответствия в субтитрах.')
    out.write('\nОтветственные за увольнение уволенных были уволены.')
out.close()
print '\nResult saved in "'+outFilename+'"'

##############################################################################
##############################################################################