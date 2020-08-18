# -*- coding: utf-8 -*-

import random
import nltk
from bot_config import BOT_CONFIG




def GetIntent(text):
    for intent, intentData in BOT_CONFIG['intents'].items():
        for example in intentData['examples']:
            editDistance = nltk.edit_distance(text.upper(), example.upper())
            if editDistance/len(example) < 0.40:
                return intent
    return

def GetResponeByIntent(intent):
    phrases = BOT_CONFIG['intents'][intent]['responces']
    return random.choice(phrases)

def GetGenerativeResponce(text):
    # TODO
    return 

def GetFailurePhrase():
    phrases = BOT_CONFIG['failurePhrases']
    return random.choice(phrases)

def PushResponce(text):
    """Ответная реплика"""
    # NLU
    intent = GetIntent(text)
    
    # Generate responce
    if intent:
        return GetResponeByIntent(intent)
    
    # Use generative model
    
    responce = GetGenerativeResponce(text)
    if responce:
        return responce
    
    # Stub
    
    return GetFailurePhrase()


while (True):
    text = input()
    print(PushResponce(text))