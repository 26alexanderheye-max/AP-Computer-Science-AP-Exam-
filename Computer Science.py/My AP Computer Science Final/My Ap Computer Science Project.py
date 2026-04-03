
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

def Decision3 ():
    print("You need to find food quickly, would you like to stay at the shore, and look food that washed up" \
    "Or would you like to go into the jungle, and search for food in there?")
    decision3 = input("Type stay or jungle: ")
    if decision3 == "stay":
        print ("You decided to stay at the shore and you find a machete, and a bag of chips")
        print ("Would you like to pick up the machete, the bag of chips, or both?")
        decision4 = input ()
        if decision4 == "the machete":
            backpack.append ("machete")
        elif decision4 == "The bag of chips":
            backpack.append ("Bag of chips")
        elif decision4 == "both":
            backpack.append ("Machete")
            backpack.append ("The back of chips")

        print("Would you now like to go to the jungle")
        if decision4 == "Yes":
                Jungle ()
        elif decision4 == "no":
            print ("You made camp on the shore and slept and now you explore the jungle") 
Decision3 ()

def Decision4 ():
    print("You walk through the jungle and find a hidden Mayan temple")
    print("You can either climb up to the top of it, or enter through a doorway in the side.")
    print("Type either climb or enter")
    Mayantempledecision = input ()
    if Mayantempledecision == "climb":
        print ("You chose to climb to the top of the temple")
        print ("When you climb to the top you see a helicopter flying in the distance looking for surviors of the nearby crash")
        print ("Due to your elevation shooting a flare gun from this height would get their attention.")
    elif
        print("You walk down a narrow passageway and trip a wire causing the floor to open and you to fall down a hole to your death")
        print("Game Over. Type restart to play again.")
        answer = input() 
        if answer == "restart":
            Decision1 ()
            Decision2 ()
            Decision3 ()
            Decision4 ()





    











    