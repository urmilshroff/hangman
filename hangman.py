import numpy
import random

print("WELCOME TO HANGMAN!")

cars=("ferrari","lamborghini","mercedes","bugatti","koenigsegg","pagani","ford","chrysler","chevrolet","dodge") #tuple of hangman words

question=cars[random.randint(0,(len(cars)-1))] #picks a random word from tuple as the question
answer=numpy.empty(len(question),str)

def start():

    while True:
        level=int(input("Choose your level of difficulty:\n1. Baby\n2. Easy\n3. Medium\n4. Hard\n5. Impossible\n"))
        if (level>=1) and (level<=5):
            break
        else:
            print("Please enter a valid difficulty level!")
        
    temp=updater(question,answer,"aeiou",0)
    trial(question,temp,6-level) #5 attempts if you're a baby



def updater(question,answer,string,flag):
    temp=[]
    isCorrect=1 #by default it is assumed that answer is correct
    
    for i in range(len(question)):
        for j in range(len(string)):
            if (question[i]==string[j]):
                answer[i]=string[j]
                temp.append(i) #stores position of matched variables
                
        if i not in temp and flag==0: #should put underscores only the first time
            answer[i]="_"
            
    print(answer)
    madarchod=0
    for i in range(len(question)):
        if(question[i]!=answer[i]) and flag==1: #if answer is still not completely correct and should run only with user input
            madarchod=1
            return 0
            break
    
    if madarchod==0 and flag==1:
        return 1        
            
        
            
    return answer
    
    
    
def trial(question,answer,attempts):
    while attempts>0:
        temp=0
        temp=updater(question,answer,input("Enter a letter:\n"),1)
        attempts-=1
        
        if (temp==1):
            break

start()










