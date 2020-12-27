import random

name = input("Welcome to the Hangman Game. Please type your name. ")
print("Hello, " + name, "." " In this Hangman Game the concept is fruits. Good Luck. Let's play! ")

fruit_list = ['apple', 'orange', 'grape', 'mango', 'banana', 'cherry', 'kiwi']

secret_word = random.choice(fruit_list)

print(str(len(secret_word)) + " is the number of letters in the wanted word.")

answer = 0
counter = 0

while answer == 0 and counter < 5:
    guess = input("Guess the fruit!: ").lower()
    if guess != secret_word:
        counter += 1
        if counter == 1:
            print(' Wrong answer! You set the scaffold! Be careful.')
        elif counter == 2:
            print('Wrong answer! My head on the scaffold!')
        elif counter == 3:
            print('Wrong answer! My body on the scaffold!')
        elif counter == 4:
            print('Wrong answer! Oh my lovely arms. NO!! You have only one chance, save my legs!')
        elif counter == 5:
            print('I love you all. You lost the game and I died.')

    else:
        answer = 1
        print("YOU SAVED MY LIFE. YOU WIN THE GAME.")

# zehra evrensel
# zehra.evrensel2017@gtu.edu.tr
