#First we create a simple menu with the three possible options
def show_menu():
    print("1. Ask Questions")
    print("2. Add a question")
    print("3. Exit Game")
    
    #Then we'll write an option variable that takes user's input
    option = input("Enter option: ")
    #Our function is going to return whathever option our user selects
    return option

print(show_menu())