print(""" _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 """)
print("Welcome to the Treasure Island")
answer = input("Do you want to enter the maze to find the treasure? Y or N ")
if answer == "Y":
    door = input("You enter a room and you find 2 doors. Do you want to go left or right? L or R")
    if door == "L":
        strip = input("Good choice! You find a mysterious bottle. Do you want to drink it or leave the room? Y or N")
        if strip == "Y":
            print("YOU JUST GOT POISONED. YOU DIED!")
        elif strip == "N":
            print("COWARD!")
    if door == "R":
        print("CONGRATULATIONS You found the treasure chest. You open it and the mighty treasure.")
else:
    print("COWARD!")
        
