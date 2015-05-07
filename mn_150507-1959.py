# coding: utf
# Python: 2.79

'''
    150507-1500 ==
    Трансформируем число в код в соответствии с ключом, получаем из словаря 
    подходящие слова.

    Скрип написан под виндой, в среде Canopy.

    150507-1751 == 
    Да.. Расширяем кругозор.. Вот, узнал слово "жмудь".

    TODO Найти словарь, состоящий только из существительных.
    DONE Проверить, как скрипт работет под linux.
    FIXED После добавления новой строки в начало словаря 
          под виндой из консоли cmd вылетает ошибка encode на эту строку.
          Возможно, дело в типе символа конца строки.
          Это было связано со странным символом, который винда иногда добавляет
          в начало файлов.
    000000 ==
'''

import itertools
import os
from sys import platform as _platform
os.chdir(os.path.dirname(os.path.realpath(__file__)))


##############################################################################
##############################################################################

# Задаём число для кодирования
number = 925


# Задаём код
key=[u'р', u'бп', u'гк', u'зс', u'дт', u'жшщчцч', u'вф', u'м', u'л', u'н']
                    # Нулевой элемент key - это цифра "0", первый - "1" и т.д.

# Задаём имя файла словаря
dictName = 'dict_utf.txt'
dictName = 'word_rus.txt'

# Задаём имя файла для выходных данных
# outFilename = 'out.txt'
outFilename = 'out_'+str(number)+'.txt'

##############################################################################
##############################################################################

# Проверка существования словаря:
if _platform == "darwin":
    print 'Hmm... osX...'
if _platform == "win32": # x32 == x64
    slash = '\\'
if _platform == "linux" or _platform == "linux2":
    slash = '/'
if not os.path.isfile(os.getcwd()+slash+dictName): 
    raise IOError(dictName+' is not exist')     

def printl(l):
    '''
    150507 == 
    Функция для консоли Canopy.
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
    for c in str(a):
        f.append(s[int(c)])
    return f

# Читаем словарь
d = open (dictName, 'r')
words = []
for w in d.readlines():
    w = w.replace("\r",""); w = w.replace("\n","") # Удаляем все концы строк
    #if w[-1] == '\n': w = w[:-1]
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