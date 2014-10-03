
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
job = raw_input("Enter a profession. For example nurse,fireman,web developer.")
adj2 = raw_input("Enter a number 0-4.")
color = raw_input("Enter a color")
drink = raw_input("Enter your favorite beverage")
sound2 = raw_input("Enter a sound-word. For example zap, crash, pow etc.")
phrase = raw_input("Enter a short phrase or exclamation. For example, The British are coming!")
monster = raw_input("enter a type of creatures name. For example dragon, saskatch etc.")
n = raw_input("Enter any number.")
phrase2 = raw_input("Enter a short exclamation. For example, yikes!")
name3 = raw_input("Enter a name.")
c = raw_input("Enter the name of a scary costume. For example, dracula.")
d = raw_input("Enter the name of a scary costume. For example, dracula")
n2 = raw_input("Enter any number.")

#changed into an integer FOR THE ARRAY and function
adj2 = int(adj2)
n = int(n)

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

#A Dictionary -------------
food = dict() #create dictionary object
food = {"green":"gummy worms", "blue":"eyeballs","red":"bat wings"}

#PRINT STORY--------------
print "It was a cold," + str(adj1) + " " + "Halloween night." + str(name1) + " " + "and" + str(name2) + " " + \
      "were driving around looking for a classmates Halloween party." + " " + "Hoping they would win first prize for best " \
      "costume," + " " + str(name1) + " " + "was dressed up as a" + str(costume1) + "." + "While" + " " + str(name2) + " " + \
      "thought he would compliment her outfit by dressing as a" + " " + str(costume2) + "." + " " + "Suddenly the car made a loud" + " " + \
      str(sound1)+ "!!" + str(name1) + " " + "and" + " " + str(name2) + "realized they were out of gas!" + " " + str(name1) + " " + "and" + str(name2) +  " " + \
      "grabbed their cell phones but there was no signal." + "They realized they were stuck in the middle of a" + " " + str(environment) + "." + str(name1) + \
      " " + "spotted a" + " " + str(house) + "in the distance with the lights on." + "The two friends decided to knock on the door for help." + \
      str(name1) + "knocked on the door." + "A person wearing a mask was dressed as a" + " " + adjectives[adj2] + " " + str(job) + " " + "opened the door." + \
      "hello...may I help you?" + str(name2) + " " + "replied yes, our car broke down and we wondered if we could use your phone to call for help?" + " " +\
      "Certainly replied the" + str(job) + "." + "Let me get you my phone and some" +  str(color) +  " " + food["red"] + "and" + str(drink) + "while you wait." + "The" + " " + \
      adjectives[adj2] + " " + str(job) + "disappeared into the kitchen." + " As" + str(name1) + " " + "and" + " " + str(name2) + " " +\
      "waited in the living room they stared out the window it had started to rain." "Suddenly they heard a strange" + str(sound2)+ " " + "outside." +\
      "The" + str(sound2) + " " + "grew louder...." + "They heard someone cry out!"

#While LOOP-----

'''
while loop to repeat first phrase
'''

i = 0
while i<3:
    print str(phrase)
    i = i+1

#Function to come up with height of creature..I made another function below
'''
I made another function below with a conditiona. For this I tried the calculating function with two parameters.
the user enters the number represented by n. the formula is n * 2 + 2, then I return the height of the creature from this
made up calculation. str(a) represents the number
'''

def calcArea(n,y):
    height = n * y + 2
    return height
a = calcArea(n, 2);

print "When they looked out the window they thought they saw a" + str(monster) + "!" + " " + "The creature appeared to be" + " " + str(a) + "feet tall!" +\
    "-Frightened they ran for the door but they couldn't get out." + "They both screamed out in unison..."

#For LOOP----
for i in range(0,3):
    print str(phrase2)
    i = i+1

print "Then from outside the door they heard familiar laughter." + "It was" + str(name3) + " " + "their friend!" "They had arrived at the Halloween party after all!" + \
      "as they looked around they saw a wall of mirrors and all their friends..."

#FOR LOOP with array ---
'''
since they are looking in mirrors...I used an array of friends and had it repeat with the loop.
using the index number.
'''
friends = ["Martha","Tami","Mike", "Steve"]
for i in range(0,2):
    print str(friends[0])
    print str(friends[1])
    print str(friends[2])
    print str(friends[3])
    i = i+1

#Function and if/else conditional to come up with best costume..
def halloween(c,d):
 if n2 > 10:
     return c
 else:
     return d
h = halloween(c,d);

print str(name1) + " " + "and" + str(name2) + " " +\
      "were glad to have found the party but a little disappointed when " + \
      "Steve won best costume." + "They had to admit though that he was the most horrifying" + \
       str(h) + "they had ever seen!!"