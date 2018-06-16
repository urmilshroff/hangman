import random

cars=("Ferrari","Lamborghini","Bavarian Motor Works","Mercedes Benz","Bugatti","Koenigsegg","Pagani","Ford","Chrysler","Chevrolet") #tuple of hangman words

print(cars[random.randint(0,(len(cars)-1))]) #prints a random car from the tuple