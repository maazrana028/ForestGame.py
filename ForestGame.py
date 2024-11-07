### Print a Welcome message 
print("Welcome to the Haunted forest!")
print("You are a young journalist who has just arrived in the forest, "
  "investigating mysterious noises and disappearances in this forest")
print("The forest is truly old with tall trees and strange noises," " that comes from a far but seems to be moving closer")
print("Do you dare to enter?")

### Prompt user for a choice
enterChoice = input("> ")

if(enterChoice == "Yes"):
  print("As you walk the path you see an old camp site")
  print("Do you want to go investigate the site for any clues?")

elif(enterChoice == "No"):
  print("You decide to leave and exit the game.") 

investigateChoice = input("> ")

if(investigateChoice == "Yes"):
  print("You walk up to the camp site and see everything has been left behind")
  print("Looks like the people left everything and ran away.") 
  print("but did someone or something scared them or did they left on their own accord?")
  print("Do you want to search further?")
elif(investigateChoice == "No"): 
  print("You decide to leave and exit the game.")
  print("You decide to walk further into the forest")
  print("Then you hear the most heart wrenching roar from behind you that scares you")
  print("Do you want to run to your car or hide in one of the tents?")

else:  
  print("Invalid Choice. Please enter Yes or No.")
searchChoice = input("> ")
if(searchChoice =="Yes"):
  print("You found bloody clothes and a gun")
  print("You hear a scary roar coming again from within the forest, coming closer!")
  print("Do you want to Run or Hide?") 

elif(searchChoice == "No"):
  print("You decide to leave and exit the game.")
  print("Thank you for playing!")
else:
  print("Invalid Choice. Please enter Yes or No") 

runChoice = input("> ")

if(runChoice == "Run"):
  print("You run towards your car and hop in and drive away")
  
elif(runChoice == "Hide"):
  print("You hide in one of the tents and wait while your heart pounces")
  print("While looking around you hear heavy footsteps of a massive creature, "
  "on all fours")
  print("Do you want to face the creature or stay inside?")
else: 
  print("Invalid Choice. Please enter Run or Hide.")

creatureChoice = input("> ")

if(creatureChoice == "Face"):
  print("You decide to face the creature, but when you see its face you get too scared, " "and wake up from your dream")
  
elif(creatureChoice == "Stay"):
  print("The creature smells you and rips the tents apart and kills you, " "and you wake up from your dream")

else:
  print("Invalid choice. Please enter Face or Stay")
  