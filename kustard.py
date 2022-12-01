##
##  _              _                _ 
## | |            | |              | |
## | | ___   _ ___| |_ __ _ _ __ __| |
## | |/ / | | / __| __/ _` | '__/ _` |
## |   <| |_| \__ \ || (_| | | | (_| |
## |_|\_\\__,_|___/\__\__,_|_|  \__,_|
##                                    
##
##  version 0.0.1 (beta)
##
# author: tiffanee c. lang (tlang@geoservd.com)
# creation date: 2022-12-01
# update date: 2022-12-01
# document: kustard.py (https://github.com/tiffaneecl/sliced_py/blob/master/kustard.py)
# descriptiom: modular masking of simple text
# purpose: to excercise crytographic concepts and standard of work for pythonic solutions
#
#
#   text of interest:
#   b\978-0-393-86745-9
#   t\Cryptography_the_Key_to_Digital_Security
#   a\keith_martin
#   p\count_250
#
#
# ----- imported libraries of choice ----- #
# string - [STANDARD] library for character based look ups and orderings (https://docs.python.org/3/library/string.html)
#
# datettime - [STANDARD] library for handling datetime objects including now() and strftime() (https://docs.python.org/3/library/datetime.html)
#
# random - [STANDARD] library for generating dice rolls (random integers).
# !! - Warning The pseudo-random generators of this module should not be used for security purposes. For security or cryptographic uses, see the secrets module.
#
#
# other credits:
# banner art: https://patorjk.com/software/taag
#
#

import string
from datetime import datetime
import random

def vanilla():
    strGetDayVal = str(datetime.now().strftime('%d'))
    strJack,strJill = string.ascii_uppercase[int(random.randint(1,14))],string.ascii_uppercase[int(random.randint(15,25))]
    strBread = str(random.randint(0,9))*2
    
    try:
        outMask = '{0}{1}{0}'.format(strBread,strJack+strJill)
    except:
        outMask = '00ZZZZ00'
        

    intStrMiddle = int(len(outMask)/2)

    return [outMask,outMask[intStrMiddle*-1:],outMask[:intStrMiddle]]

#def whitehouse():
    # use a presidential lookup schema to scramble a topping

#def eupac():
    # pronounced Oo-PAHWK like tupac lol
    # use unix epoch lookup schema to scramble a topping


def encodeMe(inCodeMe,topping=vanilla(),intAddit=int(64),intMultipass=int(2)):
    # encodeMe is meant to mask a plaintxt input using the toppics selected
    # by the user
    keyTopping = vanilla()
    

    # intMultipass acts as a divisor, cannot be zero (0)
    # In the event that the user is an idiot or forgetful, change it to their
    # intAddit value
    # But wait -- what if the user really is testing your nerves?
    # Add one to it!
    
    if intMultipass == 0 or intAddit == 0:
        if intAddit == 0:
            intAddit+= 1
        else:
            intMultipass = intAddit
    
    keyback = '-'.join(keyTopping)+'-'+str(intAddit)+'KEY'+str(intMultipass)
    # prepare the key for decoding
    
    dictAlphabet = {}
    for intPlace,letter in enumerate(string.ascii_lowercase):
        dictAlphabet[letter] = intPlace+1
    # create a dictionary object for the lowercase letters to reference in
    # the mix up make 1:1 comparision a = 1, b = 2, c = 3,...

    backBlock = []
    for ea in inCodeMe:
    # for each letter in the incoming message translate its original letter number
    # to a new number following the intAddit and intMultipass values
    #
    # In the event that character doesn't have a corresponding number
    # translate it as is.
        try:
            backBlock.append((dictAlphabet[ea]+intAddit)*intMultipass)
        except:
            backBlock.append(ea)

            
    block = ''
    for b in backBlock:
        block+=keyTopping[1]+str(b)+keyTopping[2]
    # for each newly translated character, sandwich, delimit, back into a string using the
    # selected toppings

    # return to the user the masked block and a key to get it back
    return block,keyback


def decodeMe(inCodeMe,shiv):
    keyMe = shiv.split('-')
    breaker = inCodeMe.split(keyMe[0])

    transcript = []
    for ea in breaker:
        transcript.append(ea.replace(keyMe[1],'[ BEGIN ] ').replace(keyMe[2],' [ END ]'))

    outStr = ''
    for ea in transcript:
        try:
            character = int(ea.replace('[ BEGIN ] ','').replace(' [ END ]',''))
            character = int(character/int(keyMe[3].split('KEY')[1]))
            character = int(character-int(keyMe[3].split('KEY')[0]))
            character = character-1
            outStr+=string.ascii_lowercase[character]
        except:
            character = str(ea.replace('[ BEGIN ] ','').replace(' [ END ]',''))
            outStr+=character
            
    return outStr
