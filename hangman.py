from random import randint
from json import load, dump

def hangman_display(word, known_chars):
    for i,j in enumerate(word):
        if known_chars[i] == 1:
            print(j, end=" ")
        else:
            print("_", end=" ")

def create_known_chars(word, number):
    known_chars = []
    for i in word:
        known_chars.append(0)
    
    while known_chars.count(1) < number:
        known_chars[randint(0, len(known_chars) - 1)] = 1
    return known_chars

def is_solved(known_chars):
    for i in known_chars:
        if i == 0:
            return False
    return True

def open_scoreboard():
    try:
        with open("scoreboard.json") as scoreboard:
            return load(scoreboard)
    except:
        return {}

def display_scoreboard():
    scoreboard = open_scoreboard()
    if scoreboard == {}:
        print()
        print("Empty Scoreboard!")
        print()
    else:
        print()
        print("Scoreboard")
        print("--------------")
        counter = 1 
        while scoreboard != {}:
            keys_list = list(scoreboard)
            biggest = keys_list[0]
            for name in scoreboard:
                if scoreboard[name] > scoreboard[biggest]:
                    biggest = name

            print(f"{counter}. {biggest}: {scoreboard[biggest]}")
            scoreboard.pop(biggest)
            counter += 1
        print("--------------")
        print()

def write_scoreboard(name, score):
    scoreboard = open_scoreboard()
    scoreboard[name] = score
    with open("scoreboard.json", "w") as newboard:
        dump(scoreboard, newboard)


def mainloop(name, score):
    wordlist = ["pineapple", "mountain", "science", "goat", "newspaper", "highway", "extraterrestrial"]
    
    dif = {
        "easy": 3,
        "medium": 2,
        "hard": 1
    }

    word = wordlist[randint(0, len(wordlist) - 1)].lower()
    guesses = 8

    print(f"Welcome to Hangman, {name}!")

    dif_choice = input("Choose your difficulty (Easy: 3 Tips / Medium: 2 Tips / Hard: 1 Tip): ").lower()
    while dif_choice not in dif:
        dif_choice = input("Invalid input. Try again (Easy: 3 Tips / Medium: 2 Tips / Hard: 1 Tip): ").lower()

    known_chars = create_known_chars(word, dif[dif_choice])
    print(f"You have {guesses} tries!")
    
    already_tried = []
    while True:

        if guesses == 0:
            print(f"Oh no you used up all your guesses, the correct word was {word}")
            print(f"Wanna play again? ")
            return 0
        elif is_solved(known_chars):
            print(f"Congrats, you solved it! The correct word is {word}")
            print("Wanna play again? ")
            score += 1 
            return score

        hangman_display(word, known_chars)

        guess = input("Please guess a character!: ").lower()
        while guess in already_tried:
            guess = input("You already tried that character, try again!: ").lower()
        already_tried.append(guess)

        if guess in word:
            for i, c in enumerate(word):
                if guess == c:
                    known_chars[i] = 1
        else:
            guesses -= 1
            print(f"Char not found in word! {guesses} tries left!")

def menu():
    score = 0
    name = input("Please enter your name: ")
    while True:
        choice = input("Choose an option: \n -------------- \n 1. Play Hangman \n 2. Show Scoreboard \n 3. Exit \n")

        if choice == "1":
            score = mainloop(name, score)
        elif choice == "2":
            display_scoreboard()
        elif choice == "3":
            if score > 0 and name:
                write_scoreboard(name, score)
            break
        else:
            print("Invalid input.")

menu()
