import numpy
import random

print("WELCOME TO HANGMAN!")

cars=("ferrari","lamborghini","bavarian motor works","mercedes benz","bugatti","koenigsegg","pagani","ford","chrysler","chevrolet") #tuple of hangman words

question=cars[random.randint(0,(len(cars)-1))] #picks a random word from tuple as the question
answer=numpy.empty(len(question),str)

def start():

    '''while True:
        level=int(input("Choose your level of difficulty:\n1. Baby\n2. Easy\n3. Medium\n4. Hard\n5. Impossible\n"))
        if (level>=1) and (level<=5):
            break
        else:
            print("Please enter a valid difficulty level!")'''
        
    temp=updater(question,answer,"aeiou",0)
    trial(question,temp)

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
    return answer
    
def trial(question,answer):
    temp=updater(question,answer,input("Enter a letter:\n"),1)

start()




