class file:
    filePath = 'file.md'
    fileString = open(filePath, 'r').read()
    fileContent = list(fileString)

class alphabet:
    str = 'abcdefghijklmnopqrstuvwxyz'
    array = list(str) 

def positionOverflow(place, nbMax = 26) :
    a = place // nbMax
    b = place - a * nbMax
    return b 

def changeLetterBasic(texte, decalage) : 
    for i in range(len(texte)) :
        for y in range (26) :
            if alphabet.array[y] == texte[i]:
                texte[i] = alphabet.array[positionOverflow(y + decalage)]
                break
    return(texte)

def changeLetterAffine(texte, decalage) : 
    for i in range(len(texte)) :
        for y in range (26) :
            if alphabet.array[y] == texte[i]:
                texte[i] = alphabet.array[positionOverflow(stringToAffine(3,2,y))]
                break
    return(texte)

def stringToAffine(a,b,x) :
    return x**a 

print(changeLetterAffine(file.fileContent, 5))
