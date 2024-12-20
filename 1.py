class file:
    filePath = 'file.md'
    fileString = open(filePath, 'r').read()
    fileContent = list(fileString)

class alphabet:
    str = 'abcdefghijklmnopqrstuvwxyz'
    array = list(str) 

# def handleSameLetters()

def transformY(x) :
    a = 2
    return x **3

def positionOverflow(place, nbMax = 26) :
    a = place // nbMax
    b = place - a * nbMax
    return b 

def createKey(referenceAlphabet = alphabet.array ):
    # precedentLetters = []
    alphabet = []
    arrayUsedIndex = []
    for i in range(26) :
        newIndex = positionOverflow(transformY(i))
        # a = alse
        if newIndex in arrayUsedIndex :
            while newIndex in arrayUsedIndex :
                newIndex = positionOverflow(newIndex + 1)
                if newIndex >= 26 :
                    return 1
        
        alphabet.append(referenceAlphabet[newIndex])
        arrayUsedIndex.append(newIndex)

        
        # if  alphabet[newIndex] in precedentLetters : 
        #     print('Letter Already existing')

        #     # print(precedentLetters)
        #     # while alphabet[newIndex] in precedentLetters :
        #     add = 1
        #     while alphabet[newIndex] in precedentLetters : 
        #         newIndex = positionOverflow(transformY(i) + add)
        #         print(alphabet[newIndex]) 
        #         add+=1
        #         if add > 26 :
        #             print('It broke')
        #             # print(precedentLetters)
        #             return 1 
        
        # precedentLetters.append(alphabet[i])
            
        # newIndex = positionOverflow(transformY(i)) if positionOverflow(transformY(i)) != precedentLetters else positionOverflow(transformY(i)) + 1 
    # print(len(alphabet))
    
    return alphabet

def areTwoLettersTheSame(array) : 
    seen = set()
    for num in array:
        if num in seen:
            return True
        seen.add(num)
        
print( 'Key : ',createKey())
print('Same letters : ', areTwoLettersTheSame(createKey()))


# def changeLetterBasic(texte, decalage) : 
#     for i in range(len(texte)) :
#         for y in range (26) :
#             if alphabet.array[y] == texte[i]:
#                 texte[i] = alphabet.array[positionOverflow(y + decalage)]
#                 break
#     return(texte)

# def changeLetterAffine(texte, decalage) : 
#     for i in range(len(texte)) :
#         for y in range (26) :
#             if alphabet.array[y] == texte[i]:
#                 texte[i] = alphabet.array[positionOverflow(transformY(y))]
#                 break
#     return(texte)



# print(changeLetterAffine(file.fileContent, 5))
