#First we create a simple menu with the three possible options
def show_menu():
    print("1. Ask Questions")
    print("2. Add a question")
    print("3. Exit Game")
    
    #Then we'll write an option variable that takes user's input
    option = input("Enter option: ")
    #Our function is going to return whathever option our user selects
    return option

#We write this to print and see that our simple menu works
#print(show_menu())

#Here we'll write our functionality to ask questions
def ask_questions():
    questions = []
    answers = []
    
    #We'll use a WITH BLOCK to work with our file
    with open("questions.txt") as file:
        lines = file.read().splitlines()
    #We don't need to close the file when using a with block
    
    for i, text in enumerate(lines):
        #If a line's number is even (divisible by 2), we'll say it's a question
        if i%2 == 0:
            questions.append(text)
        #Else (if it's odd), we'll say it's an answer
        else:
            answers.append(text)
    #This will create a list of questions and a list of anwers
    
    #After we created a function that allows us to ask questions, we create the
    #functionality that allows us to check the answers and keep score
    #We need to know the number of questions in our file (use len())
    number_of_questions = len(questions)
    
    #Then we create a variable that zips our Q&As so we don't have to run the
    #zip function every time the for loop iterates
    questions_and_answers = zip(questions, answers)
    
    #We initialise an empty variable to keep track of the score
    score = 0
    
    #We then use the zip function to put them together
    # for question, answer in zip(questions, answers):
    for question, answer in questions_and_answers:
        #This will let a user input their answer to a given question
        guess = input(question + "> ")
        #We need to check that our answer is correct
        if guess == answer:
            #If it is correct, we add 1 to our score and print some feedback
            score += 1
            print("right!")
            print(score)
        else:
            print("wrong!")
    #After the for loop has run around, we can print how many questions a user
    #answered correctly
    print("You got {0} correct out of {1}".format(score, number_of_questions))

#Here we add the functionality that allows us to take a user's question and 
#answer, and then append them to the questions.txt file
def add_question():
    print("")
    question = input("Enter a question\n> ")
    
    print("")
    print("Ok then, tell me the answer")
    answer = input("{0}\n> ".format(question))
    
    #Now that we've created the way for users to write their questions and
    #answers, we'll write a way to append them into our qustions.txt file
    
    file = open("questions.txt", "a")
    file.write(question + "\n")
    file.write(answer + "\n")
    file.close()

#Now we write the actual game loop
def game_loop():
    while True:
        option = show_menu()
        if option == "1":
            # print("You selected 'Ask Questions'")
            #After we created the functionality that lists questions and 
            #answers, zips them together, and let users input their answers,
            #we call that function here for option 1
            ask_questions()
        elif option == "2":
            # print("You selected 'Add a Question'")
            #After we created the functionality that allows users to add Q&As,
            #we call that function here so it gets trigered if they choose 2
            add_question()
        elif option == "3":
            break
        else:
            print("Invalid option")
        #After everything we'll print a blank line for aesthetic reasons
        print("")

game_loop()