
def introduction():
    print("Hello user! Please enter your name.")
    playername = input()
    print(f"Hello {playername}, you were on a plane when the pilot fell asleep and your plane crashed into a lake in a rural Mexican jungle.")
    print(f"You were the only survivor of the crash and all you have is your empty backpack. In order to survive you need to take immediate action.")
    print("The jungle that you landed in is extremely dangerous so you will have to be very smart with the choices you make.")

introduction()

backpack = [] 

def Decision1():
    print("You can either stay on the plane and try find useful items for the jungle or you can swim to the shore.")
    print("Type stay to stay on the plane or type swim to swim to shore.")
    decision1 = input()
    if decision1 == "stay":
        print("You decided to stay and search the plane for items.")
        print("You found a flare gun and a water bottle.")
        print("You decide to take the the water bottle, do you also want to take the flare gun?")
        decision2= input()
        if decision2 == "Yes":
            backpack.append("flare gun")
            backpack.append("water bottle")
            print("You decided to take both the flare gun and the water bottle.")
        elif decision2 == "No":
            backpack.append("water bottle")
            print("You only took the water bottle.")
            print("Now you start your swim to shore.")

    elif decision1 == "swim":
        print("You decided to swim to shore.")
        
Decision1()


def Decision2():
    print("You are extremely thirsty after the swim to shore, do you want to drink then water in your water bottle?")
    decision2 = input("Type yes or no): ")
    if decision2 == "yes":
        print ("You decided to drink the water and feel refreshed.")
    elif decision2 == "no":
        print("You decided not to drink the water and die of thirst.")
        print("Game Over. Type restart to play again.")
        answer = input() 
        if answer == "restart":
            introduction()
            Decision1() 
            Decision2()

Decision2 ()
    











    