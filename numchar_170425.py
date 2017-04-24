# coding: utf
# Python: 2.79

'''
    170425-0119 == Трансформируем число в код в соответствии с ключом, 
    получаем из словаря подходящие слова.

    Скрип работает под Windows и под Linux. Под Mac - не проверял.

    #цифро-буквенное_кодирование

    TODO Добавить возможность вводить по нескольку чисел
    000000 ==
'''

import itertools
import os
import sys
os.chdir(os.path.dirname(os.path.realpath(__file__)))


code_number = 44


# Если скрипт запущен с параметром, используем *его* 
# в качестве числа для кодирования
if __name__ == "__main__":
    param = sys.argv[-1]
    print param


##############################################################################
##############################################################################

# Задаём код
key=[u'р', u'бп', u'гк', u'зс', u'дт', u'жшщцч', u'вф', u'м', u'л', u'н']
                    # Нулевой элемент key - это цифра "0", первый - "1" и т.д.

# Задаём имя файла словаря
dictName = 'word_rus_150525.txt'


# Задаём число для кодирования

if param in ['Help', 'help', 'HELP', 'hElP', 'H', 'h', 
                                    'code', 'kode', 'kod', 'cod', '-h', '--h', '\h', '/h']:
    print u'\nДобро пожаловать в программу поддержки мнемотехнического метода'
    print u'цифро-буквенного кодирования.'
    print u'Для получения слов из числа, запустите скрипт с параметром "42".'
    print u'Более подробная информация находится в файле README.MD'
    print u'\nДля подбора слов применяется код:'  
    for i in xrange(len(key)):
        print i, '--', key[i]
    sys.exit()

if param[-3:] == '.py':
    number = code_number

else:
    number = param


##############################################################################
##############################################################################


# Проверяем существование словаря
abspath = os.path.abspath(__file__)
absdir = os.path.dirname(abspath)
absDictName = os.path.join(absdir, dictName)
if not os.path.exists(absDictName): 
    raise IOError(dictName+' is not exists')     

# Задаём имя файла для выходных данных, если нужно, создаём папку
outFilename = os.path.join(absdir, 'out', str(number)+'.txt')
if not os.path.exists(os.path.dirname(outFilename)): 
    os.mkdir(os.path.dirname(outFilename))


def printl(l):
    '''
    150507 == Специальная функция для печати в консоли Canopy.
    Печатаем список, содержащий кириллицу, как строки.
    Иначе вместо кириллицы печатается крокозябра.
    000000 ==
    '''
    for w in l: print w,
    print
#
def numToChar(number, key=[u'р', u'бп', u'гк', u'зс', u'дт', u'жшщцч', 
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
#
def cleanString(S, space=' '):
    '''
    150525 == Функция удаляет из строки повторяющиеся пробелы, табуляции и пр.
    tags: =очистить =строку.
    Весь этот хлам превращается в "space".
    000000 ==
    '''
    return space.join(S.split())



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
