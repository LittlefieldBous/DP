response = raw_input("Welcome to the game Halloween Eve! Please enter your name.")
print "Hello, " + str(response) + "!" + " Please answer the following questions to play!"

adj1 = raw_input("enter an adjective.")
name1 = raw_input("Enter a female name.")
name2 = raw_input("Enter a male name.")
costume1 = raw_input("Enter a Halloween costume.")
costume2 = raw_input("Enter a noun.")
sound1 = raw_input("Enter a sound-word. For example zap, crash, pow etc.")
num1 = raw_input("Enter a number 1-5.")

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

print "It was a cold," + str(adj1) + " " + "Halloween night." + " " + str(name1) + " " + "and" + str(name2) + " " + \
      "were driving around looking for a classmates Halloween party." "Hoping they would win first prize for best " \
      "costume," + " " + str(name1) + " " + "was dressed up as a" + " " +  str(costume1) + "." "While" + " " + str(name2) + " " + \
      "thought he would compliment her outfit by dressing as a" + " " + str(costume2) + "." + "Suddenly the car made a loud" + " " + \
      str(sound1)+ " " + str(name1) + "and" + str(name2) + "realized they were out of gas!" + " " + str(name1) + " " + "and" + str(name2) + \
      "grabbed their cell phones but there was no signal." + "They realized they were stuck in the middle of a" + " " + str(environment) + "."





