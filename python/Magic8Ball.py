from random import randint
import os

#List of Answers
answers = ['Yes!', 'No!', 'Think carefully about it.', 'I am not sure...', 'Go with your feeling.', 'Ask again later.', 'You wish.', 'In your dreams.', 'Absolutely!', 'You bet!', 'Hard no.']
question = ""

while (1 == 1):
    os.system('cls')
    print ("The Magic 8 Ball")
    print ("================")
    question = input("Ask me a question! Or type 'quit' to stop: ")
    if (question == "quit"):
        print("Goodbye")
        break
    print("")
    selection = randint(0,len(answers)-1)
    print(answers[selection])    
    print("")
    input("Press Enter to continue...")

