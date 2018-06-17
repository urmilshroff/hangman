import random

cars=("ferrari","lamborghini","bavarian motor works","mercedes benz","bugatti","koenigsegg","pagani","ford","chrysler","chevrolet") #tuple of hangman words

question=cars[random.randint(0,(len(cars)-1))] #picks a random word from tuple as the question
answer=[]
size=len(question)

print("WELCOME TO HANGMAN!\n")

'''while True:
    level=int(input("Choose your level of difficulty:\n1. Baby\n2. Easy\n3. Medium\n4. Hard\n5. Impossible\n"))
    if (level>=1) and (level<=5):
        break
    else:
        print("Please enter a valid difficulty level!")'''


for letter in range(len(question)):
    if (question[letter]=="a"):
        answer.append("a")
    elif (question[letter]=="e"):
        answer.append("e")
    elif (question[letter]=="i"):
        answer.append("i")
    elif (question[letter]=="o"):
        answer.append("o")
    elif (question[letter]=="u"):
        answer.append("u")
    else:
        answer.append("_")
        

for letter in range(len(answer)): #question and answer have same length
    if (answer[letter]=="_"):
        print("It happened in position {}".format(letter))













