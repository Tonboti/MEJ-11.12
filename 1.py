class file:
    filePath = 'file.md'
    fileString = open(filePath, 'r').read()
    fileContent = list(fileString)

class alphabet:
    str = 'abcdefghijklmnopqrstuvwxyz'
    array = list(str) 

def positionOverflow(place, nbMax = 25) :
    a = place // nbMax
    b = place - a * nbMax
    return b 

def changeLetter(texte, decalage) : 
    for i in range(len(texte)) :
        # print(i)
        for y in range (26) :
            if alphabet.array[y] == texte[i]:
                texte[i] = alphabet.array[positionOverflow(y + decalage)]
                break
    return(texte)

print(changeLetter(file.fileContent, 5))
