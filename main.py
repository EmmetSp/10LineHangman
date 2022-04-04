word, computerWordSplit, lettersToGuess = input("Input a word: "), [], ["e","t", "a", "o", "i", "n", "s", "h", "r", "d", "l", "c", "u", "m", "w", "f", "g", "y", "p", "b", "v", "k", "j", "x", "q", "z"]
for i in range(len(list(word))): computerWordSplit.append("_") # Create the template for the computer to fill
for i in range(len(lettersToGuess)): # Loop through every work in list, and break loop if template if complete.
    for x in range(len(list(word))): # Loop through every character in word, replacing the computers template when match is found
        if (list(word)[x].lower() == lettersToGuess[i].lower()): computerWordSplit[x] = lettersToGuess[i]
    print("Guessed Letter: " + lettersToGuess[i] + " Guess # " + str(i+1) + " - " + "".join(computerWordSplit)) # Print iteration into console.
    if ("_" not in computerWordSplit): break # If the template is completed, end the loop.
