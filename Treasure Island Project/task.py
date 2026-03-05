from asyncio import wait

print(r'''
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
a = input('You\'re at a cross road, Where do you want to go?\nType "left" or "right"?').lower()
if a == "right" or a == "Right" or not a == "left":
    print("Fall into a hole\nGame Over.")
if a == "left" :
    b = input('You\'ve come to a lake. There is an island in the middle of the lake.\nType "wait" to wait for a boat. Type "swim" to swim across.').lower()
    if b == "swim" or not b == "wait":
        print("Attacked by trout.\nGame Over.")
    if b == "wait" :
        c = input("You arrive at the island unharmed. This is a house with 3 doors.\nOne red one yellow one blue. WHich colour do you choose?").lower()
        if c == "red":
            print("Burned by fire.\nGame Over.")
        elif c == "yellow":
            print("You win!")
        elif c == "blue":
            print("Eaten by beasts.\nGame Over.")
        else:
            print("Game Over")


