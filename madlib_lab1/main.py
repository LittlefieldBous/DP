
'''
Amy Littlefield-Bousamra
Design Patterns for Programming
Instructor: Rebecca Carroll
Full Sail Univeristy
10/2014
'''

#WELCOME TO THE GAME --------
response = raw_input("Welcome to the game Halloween Eve! Please enter your name.")
print "Hello, " + str(response) + "!" + " Please answer the following questions to play!"

#QUESTIONS/STRINGS------

adj1 = raw_input("enter an adjective.")
name1 = raw_input("Enter a female name.")
name2 = raw_input("Enter a male name.")
costume1 = raw_input("Enter a Halloween costume.")
costume2 = raw_input("Enter a noun.")
sound1 = raw_input("Enter a sound-word. For example zap, crash, pow etc.")
num1 = raw_input("Enter a number 1-5.")
x = raw_input("Enter a number 1-4.")
job = raw_input("Enter a profession. For example nurse,fireman,web developer")
adj2 = raw_input("Enter a number 0-4.")

#changed into an integer FOR THE ARRAY
adj2 = int(adj2)

#CONDITIONAL-----------
'''
This conditional chooses the environment.
uses int to change it into a number from a string
'''

if int(num1) == 5:
    environment = "desert"
elif int(num1) == 4:
    environment = "forest"
elif int(num1) == 3:
 environment = "swamp"
elif int(num1) == 2:
 environment = "corn field"
else:
    environment = "No-wheres-ville"

#Conditional with logical operator
'''
This conditional chooses the house.
'''

if int(x) > 8 and int(x) < 10:
    house = "mansion"
elif int(x) > 6 and int(x) < 8:
    house = "a log cabin"
elif int(x) > 4 and int(x) < 6:
    house = "dilapidated victorian home"
elif int(x) > 2 and int(x) < 5:
    house = "large colonial house"
else:
    house = "scary looking manor"

#AN ARRAY --------------------
'''
This array is used for describing the person at the door.
After I had the user put in the input I had to switch the answer to an integer.
'''

adjectives =["scary", "funny", "silly", "deranged"]
adjectives.append("zombified")


#PRINT STORY--------------
print "It was a cold," + str(adj1) + " " + "Halloween night." + str(name1) + " " + "and" + " " + str(name2) + " " + \
      "were driving around looking for a classmates Halloween party." + " " + "Hoping they would win first prize for best " \
      "costume," + " " + str(name1) + " " + "was dressed up as a" + " " +  str(costume1) + "." + " " + "While" + " " + str(name2) + " " + \
      "thought he would compliment her outfit by dressing as a" + " " + str(costume2) + "." + " " + "Suddenly the car made a loud" + " " + \
      str(sound1)+ " " + str(name1) + " " + "and" + " " + str(name2) + "realized they were out of gas!" + " " + str(name1) + " " + "and" + str(name2) +  " " + \
      "grabbed their cell phones but there was no signal." + "They realized they were stuck in the middle of a" + " " + str(environment) + "." + str(name1) + \
      " " + "spotted a" + " " + str(house) + "in the distance with the lights on." + "The two friends decided to knock on the door for help." + \
      str(name1) + "knocked on the door." + "A person wearing a mask was dressed as a" + adjectives[adj2] + str(job) +  "opened the door." + \
      "hello...may I help you?" + str(name2) + " " + "replied yes, our car broke down and we wondered if we could use your phone to call for help?" + " " +\
      "Cerainly replied the" + str(job) + "."











