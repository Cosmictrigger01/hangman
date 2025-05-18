from random import randint

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

def mainloop():
    wordlist = ["apple", "banana", "tornado", "shark", "golfball", "gocart"]
    
    dif = {
        "easy": 3,
        "medium": 2,
        "hard": 1
    }

    word = wordlist[randint(0, len(wordlist) - 1)].lower()
    guesses = 8

    print("Welcome to Hangman!")

    dif_choice = input("Choose your difficulty (Easy: 3 Tips / Medium: 2 Tips / Hard: 1 Tip): ").lower()
    while dif_choice not in dif:
        dif_choice = input("Invalid input. Try again (Easy: 3 Tips / Medium: 2 Tips / Hard: 1 Tip): ").lower()

    known_chars = create_known_chars(word, dif[dif_choice])
    print(f"You have {guesses} tries!")
    
    already_tried = []
    while True:
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
        
        if guesses == 0:
            print(f"Oh no you used up all your guessed, the correct word was {word}")
            break
        elif is_solved(known_chars):
            print(f"Congrats, you solved it! The correct word is {word}")
            break

mainloop()