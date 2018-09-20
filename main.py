import os

dictionary = []

def ClearConsole():
    os.system('cls')

def AskWord():
    question = input("Give a letter?: ")
    CheckQuestion(question)

def Start():
    ClearConsole()
    answer = input("Guessing word: ")
    AddWord(answer)


def GuessWord():
    while len(dictionary) > 0:




def AddWord(answer):
    answer = answer.lower()
    
    for letter in answer:
        dictionary.append(letter)

    GuessWord()
    


Start()





