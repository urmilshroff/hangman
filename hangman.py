import random

cars=("ferrari","lamborghini","bavarian motor works","mercedes benz","bugatti","koenigsegg","pagani","ford","chrysler","chevrolet") #tuple of hangman words

question=cars[random.randint(0,(len(cars)-1))] #picks a random word from tuple as the question
answer=[]
size=len(question)

print("WELCOME TO HANGMAN!\n")

while True:
    level=int(input("Choose your level of difficulty:\n1. Baby\n2. Easy\n3. Medium\n4. Hard\n5. Impossible\n"))
    if (level>=1) and (level<=5):
        break
    else:
        print("Please enter a valid difficulty level!")

for letter in range(len(question)):
    if (question[letter]=="a"):
        answer[letter]="a"
    elif (question[letter]=="e"):
        answer[letter]="e"
    elif (question[letter]=="i"):
        answer[letter]="i"
    elif (question[letter]=="o"):
        answer[letter]="o"
    elif (question[letter]=="u"):
        answer[letter]="u"
    else:
        answer[letter]="_"
        
    print(answer)