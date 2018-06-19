import numpy
import random

print("\n********** Welcome to HANGMAN by Urmil Shroff! **********\n")

cars=("ferrari","lamborghini","porsche","tesla","mercedes","jaguar","audi","bugatti","bentley","volkswagen","ford","chrysler","chevrolet","dodge","lexus","volvo","toyota","hyundai","honda","nissan","tata") #tuple of hangman words

question=cars[random.randint(0,(len(cars)-1))] #picks a random word from tuple as the question
answer=numpy.empty(len(question),str)

def start():

    while True:
        level=int(input("Choose your level of difficulty:\n1. Baby\n2. Easy\n3. Medium\n4. Hard\n5. Impossible\n"))
        
        if level>=1 and level<=5:
            break
            
        elif level==69:
            print("\nCheater! Here's a list of all the cars:",cars)
            level=1
            break
            
        else:
            print("\nError, please enter a valid difficulty level!\n")
            
    if level==5:
        print("\nWARNING: humanly impossible!")
        
    consonantAnswer=updater(question,answer,"aeiou",0)
    attempt(question,consonantAnswer,11-(level*2))



def updater(question,answer,string,caller):
    temp=[]
    isCorrect=True #by default it is assumed that answer is correct
    
    for i in range(len(question)):
        for j in range(len(string)):
            if question[i]==string[j]:
                answer[i]=string[j]
                temp.append(i) #stores position of matched variables
                
        if i not in temp and caller==0: #should put underscores only if start() calls it
            answer[i]="_"
            
    print("\nThe car so far:",answer)
            
    for i in range(len(question)):
        if question[i]!=answer[i] and caller==1: #if answer is still not completely correct and attempt() calls it
            isCorrect=False
            return False
            break
            
    if isCorrect and caller==1: #if answer is clean
        return True
            
    return answer



def attempt(question,answer,attempts):
    tries=1
    totalAttempts=attempts

    while attempts>0:
        isCorrect=updater(question,answer,input("Enter a letter to complete the car! Attempt {} of {}:\n".format(tries,totalAttempts)),1) #last parameter means attempt() is calling it
        attempts-=1
        tries+=1
        
        if isCorrect:
            print("\nCongratulations, you guessed the car in {} tries!\n".format(tries-1))
            break
            
    if isCorrect==False: #if while loop ends and no correct guess was made
        print("\nOops, you ran out of attempts! The correct answer was {}.\n".format(question))

start()