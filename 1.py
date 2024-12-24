class file:
    #nom du fichier a changer selon les cas
    filePath = 'file.md' 
    fileString = open(filePath, 'r').read()
    fileContent = list(fileString)

class alphabet:
    str     = "abcdefghijklmnopqrstuvwxyz"
    maj     = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    array   = list(str) 

    # L'alphabet encrypte depend d'une fonction declaree plus loin qui elle meme depend de l'alphabet, donc il sera declare plus tard
    encrypted       = []
    encryptedIndex  = []

    def toSmall(string):
        output = list(string)
        for i in range(len(output)) :
            if output[i] in alphabet.maj :
                index       = alphabet.maj.index(output[i])  # Trouve l'index dans `maj`
                output[i]   = alphabet.array[index]  
        # return ''.join(output)
        return output

class numbers:
    numbers = list('1234567890') 

#########################################################################
#########################################################################
1#########################################################################

class typeConversion : 
    def stringArrayToInt(stringArray):
        string = ''
        for num in stringArray : 
            string += num
        return int(string)

    def stringArrayToString(stringArray):
        string = ''
        for num in stringArray : 
            string += num
        return string
    
    def stringArrayToIntArray(stringArray):
        intArray = []
        for num in stringArray : 
            intArray.append(int(num))
        return intArray
    
    def intArrayToStringArray(intArray):
        stringArray = []
        for num in intArray : 
            stringArray.append(str(num))
        return stringArray

    def intArrayToString(my_list, separator = ''):
        array = separator.join(map(str, my_list))
        return int(array)

    def stringToIntArray(string) : 
        output = []
        for num in list(string) :
            output.append(int(num))
        return output
            
#########################################################################

class arrayConversions : 
    def oneToTwoDigits(array) :
        array = ["{:02}".format(num) for num in array]
        return array

    def toXDigitArray(string, pas=2 ):
        # string = list(str(string))
        # string = typeConversion.strin
        array = []
        for i in range(len(string)):
            a = list(string[i])
            array.append(a)

        return array
        # return [string[i:i+pas] for i in range(0, len(string), pas)]

    def removeZerosFromArray(encryptedText):
            newArray = []
            numbers =  list('1234567890')
            
            for i in range (len(encryptedText)) : 

                if(len(encryptedText[i])) == 2 : 
                    if encryptedText[i][0] in numbers and encryptedText[i][1] in numbers :
                        newArray.append(typeConversion.stringArrayToInt([encryptedText[i][0],encryptedText[i][1]]))
                    # Faire le tri pour savoir si c'est un char special (cad espace ou apostrophe) 
                    elif encryptedText[i][0] not in numbers or encryptedText[i][1] not in numbers :
                        if encryptedText[i][0] not in numbers:
                            newArray.append(encryptedText[i][0])
                        if encryptedText[i][1] not in numbers:
                            newArray.append(encryptedText[i][1])

            return newArray

    def intStringToIntArrayWithSeparations(intString) : 
        a = list(intString)
        if len(a)%2 != 0 :
            pass
            raise("Input length must be even")  
        b=[]
        for i in range(0,len(a),2) :
            b.append(a[i:i+2])
        usableArray = arrayConversions.toXDigitArray(b)
        return arrayConversions.removeZerosFromArray(usableArray)

# Verifie si il y a plusieurs occurences d'une meme lettre dans un array, utilise pour tester l'algorithme de cryptage
def areTwoLettersTheSame(array) : 
    seen = set()
    for num in array:
        if num in seen:
            return True
        seen.add(num)
        
#########################################################################
#########################################################################

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
        # arrayUsedIndex = ["{:02}".format(num) for num in arrayUsedIndex]
        return arrayUsedIndex


#########################################################################
alphabet.encrypted = createKey()
alphabet.encryptedIndex = createKey(True)
#########################################################################

# Input : intArray array
def indexToLetter(intArray, stringIntArray, alphabet = alphabet.array) : 
    input   = []
    output  = []
    if stringIntArray :
        input = typeConversion.stringArrayToIntArray(intArray)
    else :
        input = intArray
    for i in range(len(input)):
        output.append(alphabet[input[i]])
    return output
 
# Encrypte un texte(array) selon la clef precedemment definie  
def encrypt(texte, returnIndex = False, encryptedAlphabet = alphabet.encrypted, alphabet = alphabet.array) : 
    encryptedIndex = [None] * len(texte)
    for i in range(len(texte)) :
        for y in range (26) :
            if texte[i] == alphabet[y]:
                texte[i] = encryptedAlphabet[y]
                encryptedIndex[i] = y 
                break
            if texte[i] not in alphabet:
                encryptedIndex[i] = ' '

    if returnIndex :
        return(encryptedIndex)
    else : 
        return(texte)

# Decrypte un texte crypte avec la clef 
def decrypt(encryptedText, returnIndex = False, encryptedAlphabet = alphabet.encrypted, alphabet = alphabet.array) :
    encryptedIndex = []

    for i in range(len(encryptedText)) :
        for y in range (26) :
            if encryptedText[i] == encryptedAlphabet[y]:
                encryptedText[i] = alphabet[y]
                encryptedIndex.append(y)
                break
    
    if returnIndex:
        return encryptedIndex
    else :
        return encryptedText

# Decrypte a partir d'un index
def decryptIndex(encryptedText, encryptedAlphabetIndex = alphabet.encryptedIndex, alphabet = alphabet.encrypted) :
    newArray = arrayConversions.intStringToIntArrayWithSeparations(encryptedText)
    for i in range(len(newArray)) :
        if newArray[i] != ' ' :
            for y in range (26) :
                if newArray[i] == encryptedAlphabetIndex[y]:
                    newArray[i] = alphabet[y]
                    break
    return newArray

#########################################################################
########################## Conversions de base ##########################

class baseConversion : 
    # Permet de changer de base 10 a base x l'input
    def fromBase10(number, base) :      
        number      = int(number) 
        resteArray  = []
        quotient    = number
        reste       = 0

        # Conversion de base 10 a base x
        while quotient != 0 :
            reste   = quotient % base
            quotient= quotient // base
            resteArray.append(reste)

        resteArray.reverse()
        
        # Transforme les valeurs superieures a 10 en lettres
        if base >= 10 : 
            letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            for i in range(len(resteArray)) :
                bufferReste = resteArray[i]
                if bufferReste >= 10 :
                    bufferReste = letters[bufferReste-10]
                resteArray[i] = bufferReste  

        # Il y a souvent un 0 inutile en debut, donc autant l'enlever
        # if resteArray[0] == 0 : 
        #     resteArray.pop(0) 

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

    # Convertit un nombre d'une base a une autre [max base 32]
    def fromBaseToBase(number, startBase, finalBase) :
        number  = str(number)
        a       = baseConversion.toBase10(number, startBase)
        return baseConversion.fromBase10(a, finalBase)

class baseConversionFromStr : 
    # Permet de changer de base 10 a base x l'input
    def fromBase10(number, base) :      
        number      = typeConversion.stringArrayToIntArray(list(number)) 

        # Prendre les 0 au debut pour les reinjecter plus tard dans l'output
        zeroBuffer  = []
        for i in range(len(number)):
            if int(number[i]) != 0:
                for y in range(i):
                    number.pop(0)
                break
            zeroBuffer.append(number[i])
        number = int(typeConversion.intArrayToString(number))

        resteArray  = []
        quotient    = number
        reste       = 0

        # Conversion de base 10 a base x
        while quotient != 0 :
            reste   = quotient % base
            quotient= quotient // base
            resteArray.append(reste)

        resteArray.reverse()
        
        # Transforme les valeurs superieures a 10 en lettres
        if base >= 10 : 
            letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            for i in range(len(resteArray)) :
                bufferReste = resteArray[i]
                if bufferReste >= 10 :
                    bufferReste = letters[bufferReste-10]
                resteArray[i] = bufferReste  

        # Il y a souvent un 0 inutile en debut, donc autant l'enlever
        # if resteArray[0] == 0 : 
        #     resteArray.pop(0) 

        # Combiner les zeros d'origine avec le nombre converti en 1 seul str
        zeros = ''
        output = ''
        for elem in resteArray:
            output+=str(elem)
        for elem in zeroBuffer:
            zeros+=str(elem)

        return zeros+output

    # Nombre en base x en base 10
    def toBase10(numberStr, base = 16) :
        intArray = []
        array = list(str(numberStr))
        output = 0

        if numberStr == '0':
            return 0 

        # Prendre les 0 au debut pour les reinjecter plus tard dans l'output
        zeroBuffer  = []
        for i in range(len(array)):
            if array[i] != '0':
                for y in range(i):
                    array.pop(0)
                break
            zeroBuffer.append(array[i])

        array.reverse()

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

        zeroBuffer = typeConversion.stringArrayToString(zeroBuffer)
        return zeroBuffer + str(output)

    # Convertit un nombre d'une base a une autre [max base 32]
    def fromBaseToBase(number, startBase, finalBase) :
        number  = str(number)
        a       = baseConversion.toBase10(number, startBase)
        return baseConversion.fromBase10(a, finalBase)

#########################################################################
#################### Raccourcir le message chiffre ######################

# input sous cette forme : [input=] typeConversion.stringArrayToString(arrayConversions.oneToTwoDigits(encrypt(file.fileContent, True)))
def raccourcirMessageChiffre(array, base = 16):
    inputBuffer = array.split(" ") 
    input=[]
    # element_to_insert = " "
    # input = [item for pair in zip(input, [element_to_insert] * len(input)) for item in pair][:-1]
    for i in range(len(inputBuffer)):
        input.append(inputBuffer[i])
        input.append(' ')

    # print(input,'\n\n')

    output = [':'] * len(input)
    for i in range(len(input)):
        if input[i] != '' and input[i] != ' 'and input[i] != ':':
            output[i] = baseConversionFromStr.fromBase10(input[i], base)
        if input[i] == '0' :
            # print('??') 
            output[i] = '0'
    # print(output,"\n\n")
    a = []
    b = []
    for i in range(len(output)):
        for y in range(len(output[i])):
            b.append(str(output[i][y]))

    a = typeConversion.stringArrayToString(b)        
    return a

# inverse de la fonction ci-dessus
def rallongerMessageChiffre(array, base = 16):
    input = array.split(":") 
    element_to_insert = " "
    input = [item for pair in zip(input, [element_to_insert] * len(input)) for item in pair][:-1]

    output = [' '] * len(input)
    for i in range(len(input)):
        if input[i] != '' and input[i] != ' ':
            output[i] = baseConversionFromStr.toBase10(input[i], base)
    a = []
    b = []
    for i in range(len(output)):
        b.append(str(output[i]))
    a = typeConversion.stringArrayToString(b)        

    return a

#########################################################################
############################## Best of ##################################

class finalCrypt:
    def encrypt(texteStr):
        texteStr = alphabet.toSmall(texteStr)
        return raccourcirMessageChiffre(typeConversion.stringArrayToString(arrayConversions.oneToTwoDigits((encrypt(texteStr, True)))))

    def decrypt(texteStr):
        return typeConversion.stringArrayToString(decryptIndex(rallongerMessageChiffre(texteStr)))

#########################################################################
#########################################################################

b = finalCrypt.encrypt(file.fileContent)
print(b, "\n\n")
print(finalCrypt.decrypt(b))

