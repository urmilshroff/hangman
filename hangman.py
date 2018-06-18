import numpy
import random

print("WELCOME TO HANGMAN!")

<<<<<<< HEAD
cars=("ferrari","lamborghini","mercedes","bugatti","koenigsegg","pagani","ford","chrysler","chevrolet","dodge") #tuple of hangman words
=======
cars=("ferrari","lamborghini","bavarian motor works","mercedes benz","bugatti","koenigsegg","pagani","ford","chrysler","chevrolet") #tuple of hangman words
>>>>>>> parent of e12d330... Goodnight

question=cars[random.randint(0,(len(cars)-1))] #picks a random word from tuple as the question
answer=numpy.empty(len(question),str)

def start():

    while True:
        level=int(input("Choose your level of difficulty:\n1. Baby\n2. Easy\n3. Medium\n4. Hard\n5. Impossible\n"))
        if (level>=1) and (level<=5):
            temp=updater(question,answer,"aeiou",0)
            trial(question,temp,6-level) #try to replace temp with updater() call
            break
        else:
            print("Please enter a valid difficulty level!")
        

def updater(question,answer,string,flag):
    temp=[]
    
    for i in range(len(question)):
        for j in range(len(string)):
            if (question[i]==string[j]):
                answer[i]=string[j]
                temp.append(i) #stores position of matched variables
                
        if i not in temp and flag==0: #should put underscores only the first time
            answer[i]="_"

    print("Q & A at this stage is",question,answer)

    for i in range(len(question)):
        if(question[i]!=answer[i]):
            return 0
            break

    return 1

    
<<<<<<< HEAD

def trial(question,answer,attempts):
    while attempts>0:
        print("Attempt number",attempts)
        breaker=updater(question,answer,input("Enter a letter:\n"),1)
        attempts-=1
        if (breaker==1):
            break

    print("Game over")
=======
def trial(question,answer):
    while "_" not in answer:
        temp=updater(question,answer,input("Enter a letter:\n"),1)

start()



>>>>>>> parent of e12d330... Goodnight

