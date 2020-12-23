from random import randint

choice = ["stone","paper","scissor"]

computer_selection = choice[randint(0,2)]

c = True
while c == True:
    player = input("what is your choice stone,paper or scissor:")
    if player == computer_selection:
        print("tie")
    elif player == ("stone"):
        if computer_selection == ("scissor"):
            print("hey there you won, computer selects scissor.so,stone smaches scissor")
            break
        else:
            print("hey there you lose,computer selects paper.so, paper covers stone")
            break
    elif player == ("paper"):
        if computer_selection == ("scissor"):
            print("hey there you lose, computer selects scissor.so, scissor cuts paper")
            break
        else:
            print("hey there you won, computer selects stone.so, paper covers stone")
            break
    elif player ==("scissor"):
        if computer_selection ==("stone"):
            print("hey there you lose computer selects stone.so, stone smaches scissor")
            break
        else:
            print("hey there you won,computer selects paper.so scissor cuts paper")
            break
    else:
        print("enter a valid word!!!")
        break
        
