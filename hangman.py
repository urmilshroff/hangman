import numpy
import random

cars=("ferrari","lamborghini","bavarian motor works","mercedes benz","bugatti","koenigsegg","pagani","ford","chrysler","chevrolet") #tuple of hangman words

question=cars[random.randint(0,(len(cars)-1))] #picks a random word from tuple as the question
size=len(question)
answer=numpy.empty(size,str)
vowels="aeiou"



def start():
    print("WELCOME TO HANGMAN!\n")

    '''while True:
        level=int(input("Choose your level of difficulty:\n1. Baby\n2. Easy\n3. Medium\n4. Hard\n5. Impossible\n"))
        if (level>=1) and (level<=5):
            break
        else:
            print("Please enter a valid difficulty level!")'''

def wtf(question,string,answer):
    temp=[]
    
    for i in range(len(question)):
        for j in range(len(string)):
            if (question[i]==string[j]):
                answer[i]=string[j]
                temp.append(i) #stores position of matched variables
    print("Matched positions are",temp)   
    
    for i in range(len(question)):
        if i not in temp:
            answer[i]="_"
    
    print(question,answer)
    

wtf(question,vowels,answer)

# for letter in range(len(answer)): #question and answer have same length
#     if (answer[letter]=="_"):
#         print("It happened in position {}".format(letter))








