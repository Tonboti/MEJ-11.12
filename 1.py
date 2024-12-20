class file:
    #nom du fichier a changer selon les cas
    filePath = 'file.md' 
    fileString = open(filePath, 'r').read()
    fileContent = list(fileString)

class alphabet:
    str = 'abcdefghijklmnopqrstuvwxyz'
    array = list(str) 
    # L'alphabet encrypte depend d'une fonction declaree plus loin qui elle meme depend de l'alphabet, donc il sera declare plus tard
    encrypted = []


#########################################################################
#########################################################################


# Simple conversion d'array en string 
def arrayToString(array) :
    outputString = ''
    for i in range(len(array)) : 
        outputString += array[i]
    return outputString 

def intArrayToString(my_list, separator = ''):
    array = separator.join(map(str, my_list))
    return int(array)

# Encrypte l'index des lettres grace a une fonction mathematique, a changer si souhaite
def transformY(x) :
    return round((5 * (x ** 2 ))/3 + 15)

# Assigne un nombre entre 1 et 26 a un nombre superieur a 26 
def positionOverflow(place, nbMax = 26) :
    a = place // nbMax
    b = place - a * nbMax
    return b 

# Cree un alphabet encrypte - donc la clef selon la fonction transformY
def createKey(returnIndex = False, referenceAlphabet = alphabet.array):
    # clef 
    alphabet = []
    # array qui recueille les nombres d'index deja utilises pour pallier a une reutilisation de lettres pour deux lettres differentes 
    arrayUsedIndex = []

    for i in range(26) :
        # index qui serait assigne a l'index non ecrypte 
        newIndex = positionOverflow(transformY(i))

        # si cet index est deja utilise, on passe au suivant jusqu'a ce que ne soit plus le cas
        if newIndex in arrayUsedIndex :
            while newIndex in arrayUsedIndex :
                newIndex = positionOverflow(newIndex + 1)
                if newIndex >= 26 :
                    return 1
        
        # ajoute le char encrypte correspondant a l'index determine ci-dessus
        alphabet.append(referenceAlphabet[newIndex])
        # ajoute l'index determine ci-dessus a l'array des index utilises
        arrayUsedIndex.append(newIndex)
    
    if returnIndex == False :
        return alphabet
    else :
        arrayUsedIndex = ["{:02}".format(num) for num in arrayUsedIndex]
        return arrayUsedIndex


#########################################################################
alphabet.encrypted = createKey()
#########################################################################


# Encrypte un texte(array) selon la clef precedemment definie  
def encrypt(texte, encryptedAlphabet = alphabet.encrypted, alphabet = alphabet.array) : 
    for i in range(len(texte)) :
        for y in range (26) :
            if texte[i] == alphabet[y]:
                texte[i] = encryptedAlphabet[y]
                break
    return(texte)

# Decrypte un texte crypte avec la clef 
def decrypt(encryptedText, encryptedAlphabet = alphabet.encrypted, alphabet = alphabet.array) :
    for i in range(len(encryptedText)) :
        for y in range (26) :
            if encryptedText[i] == encryptedAlphabet[y]:
                encryptedText[i] = alphabet[y]
                break
    return(encryptedText)

# Verifie si il y a plusieurs occurences d'une meme lettre dans un array, utilise pour tester l'algorithme de cryptage
def areTwoLettersTheSame(array) : 
    seen = set()
    for num in array:
        if num in seen:
            return True
        seen.add(num)
        

########################## Raccourcir la clef ############################

# Permet de changer de base 10 a base x l'input
def fromBase10(number, base) : 
    resteArray  = []
    quotient    = number
    reste       = 1

    # Conversion de base 10 a base x
    while reste != 0 :
        reste   = quotient % base
        quotient= quotient // base
        resteArray.append(reste)

    resteArray.reverse()
    
    # Transforme les valeurs superieures a 10 en lettres
    letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for i in range(len(resteArray)) :
        bufferReste = resteArray[i]
        if bufferReste >= 10 :
            bufferReste = letters[bufferReste-10]
        resteArray[i] = bufferReste  

    # Il y a souvent un 0 inutile en debut, donc autant l'enlever
    if resteArray[0] == 0 : 
        resteArray.pop(0) 

    return resteArray

# Nombre en base x en base 10
def toBase10(numberStr, base = 16) :
    intArray = []
    array = list(str(numberStr))
    array.reverse()
    output = 0

    # conversion de char en nombre si base superieure a 10
    if base >=10 :
        letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        for i in range(len(array)):
            if array[i] in letters :
                array[i] = letters.index(array[i]) + 10
            intArray.append(int(array[i]))

    # sinon conversion du char array en int array 
    else :
        for char in array:
            intArray.append(int(char))
    
    # conversion en base 10
    for i in range(len(intArray)) :
        output += intArray[i]*(base** i)
    return output


def fromBaseToBase(number, startBase, finalBase) :
    a = toBase10(number, startBase)
    return fromBase10(a, finalBase)

print(fromBaseToBase('C3B', 16, 2))
#########################################################################
#########################################################################

# print(fromBase10(intArrayToString(createKey(True)),32))

# print(
#     toBase(
#         intArrayToString(createKey(True))
#         ), 16)
# sth = encrypt(file.fileContent)
# print('\n')
# print( 'Key       : ', createKey())
# print( 'Encrypted : ', arrayToString(sth))
# print( 'Decrypted : ', arrayToString(decrypt(sth)))
# print('\n')

