import random
import os
import time

def clear():
    os.system("clear")

# Set of Instruction for Rock-Paper-Scissors
def rps_instructions():
    print()
    print("Instructions for Rock-Paper-Scissors: ")
    print()
    print("Rock crushes Scissors")
    print("Scissors cuts Paper")
    print("Paper covers Rock")
    print()

# Set of Instructions for Rock-Paper-Scissors-Lizard-Spock
def rpsls_instructions():
    print()
    print("Instructions for Rock-Paper-Scissors: ")
    print()
    print("Instructions for Rock-Paper-Scissors: ")
    print()
    print("Rock crushes Scissors")
    print("Scissors cuts Paper")
    print("Paper covers Rock")
    print("Rock crushes Lizard")
    print("Lizard poisons Spock")
    print("Spock smashes Scissors")
    print("Scissors decapitates Lizard")
    print("Lizard eats Papers")
    print("Paper disproves Spock")
    print("Spock vaporizes Rock")
    print("Rock crushes Scissors")
    print()

# Game for Rock-Paper-Scissors
def rps():
    global rps_table
    global game_map
    global name

    # Global Loop for each Game of Rock-Paper-Scissors
    while True:
        print("---------------------------------------")
        print("\t\tMenu")
        print("---------------------------------------")
        print("Enter \"Help\" for instructions")
        print("Enter \"Rock\",\"Paper\",\"Scissors\" to play")
        print("Enter \"Exit\" to Quit")
        print("---------------------------------------")

        print()

        # Player Input
        inp= input("Enter your move: ")
        if inp.lower()=="help":
            clear()
            rps_instructions()
            continue
        elif inp.lower()=="exit":
            clear()
            break
        elif inp.lower()=="rock":
            player_move=0
        elif inp.lower()=="paper":
            player_move=1
        elif inp.lower()=="scissor":
            player_move=2
        else:
            
            print("Wrong Input!!")
            rps_instructions()
            continue
        print("Computer making a move...")
        print()
        time.sleep(2)
        
        # Get the Computer move randomly
        comp_move=random.randint(0,2)

        # Print the computer move
        print("Computer chooses", game_map[comp_move].upper())

        # Find the winner of the match
        winner=rps_table[player_move][comp_move]

        # Declare the winner
        if winner==player_move:
            print(name,"WINS")
        elif winner==comp_move:
            print("Computer WINS")
        else:
            print("Tie Game")

        print()
        time.sleep(2)
        clear()

# Game for Rock-Paper-Scissors-Lizard-Spock
def rpsls():
    global rpsls_table
    global game_map
    global name

    # Global Loop for each game of  Rock-Paper-Scissors-Lizard-Spock
    while True:
        print("---------------------------------------")
        print("\t\tMenu")
        print("---------------------------------------")
        print("Enter \"Help\" for instructions")
        print("Enter \"Rock\",\"Paper\",\"Scissors\",\"Lizard\",\"Spock\" to play")
        print("Enter \"Exit\" to Quit")
        print("---------------------------------------")

        print()

        # Player Input for rpsls
        inp= input("Enter your move: ")
        if inp.lower()=="help":
            clear()
            rpsls_instructions()
            continue
        elif inp.lower()=="exit":
            clear()
            break
        elif inp.lower()=="rock":
            player_move=0
        elif inp.lower()=="paper":
            player_move=1
        elif inp.lower()=="scissor":
            player_move=2
        elif inp.lower()=="lizard":
            player_move=3
        elif inp.lower()=="spock":
            player_move=4
        else:
            clear()
            print("Wrong Input!!")
            rpsls_instructions()
            continue
        print("Computer making a move...")
        comp_move=random.randint(0,4)
        print()
        time.sleep(2)

         # Print the computer move
        print("Computer chooses", game_map[comp_move].upper())

        # Find the winner of the match
        winner=rpsls_table[player_move][comp_move]

        # Declare the winner
        if winner==player_move:
            print(name,"WINS")
        elif winner==comp_move:
            print("Computer WINS")
        else:
            print("Tie Game")

        print()
        time.sleep(2)
        clear()

# The main function
if __name__=='__main__':
    # The mappping between moves and numbers
    game_map={0:"Rock", 1:"Paper", 2:"Scissor", 3:"Lizard", 4:"Spock"}

    # Win-Lose matrix for traditional game 
    rps_table=[[-1,1,0],[1,-1,2],[0,2,-1]]

    # Win-Lose matrix for new version for the game
    rpsls_table=[[-1,1,0,0,4],[1,-1,2,3,1],[0,2,-1,2,4],[0,3,2,-1,3],[4,1,4,3,-1]]

    name=input("Enter  your name: ")

    # The game loop
    while True:
        # The game menu
        print()
        print("Let's Play...")
        print("Which version of Rock-Paper-Scissors?")
        print("Enter 1 to play Rock-Paper-Scissors")
        print("Enter 2 to play Rock-Paper-Scissors-Lizard-Spock")
        print("Enter 3 to Quit")
        print()

        # Try block to handle the player choice
        try:
            choice=int(input("Enter your choice= "))
        except ValueError:
            clear()
            print("Wrong Choice")
            continue
        # Play the traditional version of the game
        if choice==1:
            rps()

        # Play the new version of the game
        if choice==2:
            rpsls()

        # Quit the game loop
        elif choice==3:
            breakpoint
        # Other wrong input
        else:
            clear()
            print("Wrong choice. Read instructions carefully. ")
        
    









































   
