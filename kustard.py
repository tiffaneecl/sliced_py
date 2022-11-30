import string
from datetime import datetime
import random

def getDayTooth():
    dayTooth = str(datetime.now())[8:10]
    jack = random.randint(1,int(dayTooth) - 14)
    jill = random.randint(3,int(dayTooth) - 14)
    try:
        tooth = '00'+string.ascii_uppercase[jack]+string.ascii_uppercase[jill]+'00'
    except:
        tooth = '00ZZZZ00'

    chop = int(len(tooth)/2)

    return [tooth,tooth[chop*-1:],tooth[:chop]]

def encodeMe(inCodeMe,addit=64,multipass=2):
    splitter = getDayTooth()
    if multipass == 0:
        multipass = addit
    keyback = '-'.join(splitter)+'-'+str(addit)+'KEY'+str(multipass)
    regular_place = {}

    for pl,letter in enumerate(string.ascii_lowercase):
        regular_place[letter] = pl+1

    backBlock = []
    for ea in inCodeMe:
        try:
            backBlock.append((regular_place[ea]+addit)*multipass)
        except:
            backBlock.append(ea)
            
    block = ''
    for b in backBlock:
        block+=splitter[1]+str(b)+splitter[2]

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
