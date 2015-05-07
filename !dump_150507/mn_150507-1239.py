# coding: utf

words = ['qwer','asdf','zxcv', 'qr']

glas = ['e','y','u','i','o','a']
sogl = ['q','w','r','t','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']

# fChars = ['q',['r','t']]
fChars = ['q','r']

trueWords = []
numChars = 2
for word in words:
    print 'word:', word
    thisWordTrue = True

    for fChar in fChars:
        print 'fChar:', fChar
        i = 0
        for char in word:
            print 'char:', char
            if char in glas:
                continue
            i += 1
            print 'i=', i
            if i == numChars: 
                break
            if char == fChar:
                thisWordTrue = True
                continue
            if char != fChar:
                thisWordTrue = False
                break
    if thisWordTrue: trueWords.append(word)

        

    # for char in word:
    #     print char
    #     if char in glas:
    #         continue
    #     for fChar in fChars:
    #         if type(fChar) == str:
    #             print fChar
    #             if char != fChar: 
    #                 thisWordTrue = False
    #             print thisWordTrue

            # elif type(fChar) == list:
                # for sShar in fChar:
                    # if sShar != fChar: thisWordTrue = False
            # else: 
            #     raise TypeError('fChars must consist by strings or list of strings')
        # if i == numChars: break
        # i += 1
    # if thisWordTrue: trueWords.append(word)

print trueWords

