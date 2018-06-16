import random

cars=("Ferrari","Lamborghini","Bavarian Motor Works","Mercedes Benz","Bugatti","Koenigsegg","Pagani","Ford","Chrysler","Chevrolet") #tuple of hangman words

word=cars[random.randint(0,(len(cars)-1))] #picks a random word from tuple as the question