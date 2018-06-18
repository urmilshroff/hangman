import numpy
import random

print("WELCOME TO HANGMAN!")

cars=("ferrari","lamborghini","mercedes","bugatti","koenigsegg","pagani","ford","chrysler","chevrolet","dodge") #tuple of hangman words

question=cars[random.randint(0,(len(cars)-1))] #picks a random word from tuple as the question
answer=numpy.empty(len(question),str)

def start():

    while True:
        level=int(input("Choose your level of difficulty:\n1. Baby\n2. Easy\n3. Medium\n4. Hard\n5. Impossible\n"))
        if level>=1 and level<=5:
            break
        else:
            print("Please enter a valid difficulty level!")
        
    consonantAnswer=updater(question,answer,"aeiou",0)
    attempt(question,consonantAnswer,6-level) #5 attempts if you're a baby



def updater(question,answer,string,caller):
    temp=[]
    isCorrect=1 #by default it is assumed that answer is correct
    
    for i in range(len(question)):
        for j in range(len(string)):
            if question[i]==string[j]:
                answer[i]=string[j]
                temp.append(i) #stores position of matched variables
                
        if i not in temp and caller==0: #should put underscores only if start() calls it
            answer[i]="_"
            
    for i in range(len(question)):
        if question[i]!=answer[i] and caller==1: #if answer is still not completely correct and attempt() calls it
            isCorrect=0 #set to False i.e. isWrong==True
            return 0
            break
            
    if isCorrect==1 and caller==1: #if answer is clean
        return 1
            
    return answer
    
    
    
def attempt(question,answer,attempts):

    while attempts>0:
        isCorrect=updater(question,answer,input("Enter a letter:\n"),1) #last parameter means attempt() is calling it
        attempts-=1
        
        if isCorrect==1:
            print("Congratulations, your guess of {} is correct!".format(question))
            break
            
    if isCorrect==0: #if while loop ends and no correct guess was made
        print("Oops, you ran out of attempts! The correct answer was {}.".format(question))

start()