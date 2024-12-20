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
def charArrayToString(array) :
    outputString = ''
    for i in range(len(array)) : 
        outputString += array[i]
    return outputString 

# Encrypte l'index des lettres grace a une fonction mathematique, a changer si souhaite
def transformY(x) :
    return round((5 * (x ** 2 ))/3 + 15)

# Assigne un nombre entre 1 et 26 a un nombre superieur a 26 
def positionOverflow(place, nbMax = 26) :
    a = place // nbMax
    b = place - a * nbMax
    return b 

# Cree un alphabet encrypte - donc la clef selon la fonction transformY
def createKey(referenceAlphabet = alphabet.array ):
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
    
    return alphabet


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
        

#########################################################################
#########################################################################


sth = encrypt(file.fileContent)
print('\n')
print( 'Key       : ', createKey())
print( 'Encrypted : ', charArrayToString(sth))
print( 'Decrypted : ', charArrayToString(decrypt(sth)))
print('\n')

