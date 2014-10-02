print "hello world!"

#if condition:
#one lined comments
'''
Doc strings
'''

#python3 print(first_name)
first_name = "Kermit"
last_name ="Frog"
#print first_name

#response = raw_input("Enter your name...")
#print "hello, ", response

birth_year = 1971
current_year = 2014
age = current_year - birth_year
#print age

#age = age + 3
#age +=3

print "you are " + str(age) + " years old"

#int(var)

#conditional statements uses indention.

#if(conditional){ (javascript conditional)
    #//stuff to do
#}

#python way to do a conditional
#if conditional:
    #stuff to do
#budget 100 no cool shoes for me
budget = 200

if budget > 100:
    brand = "nike"
    print "Yay! we can buy cool " + brand + " shoes!"
#else if in python
elif budget >50:
    print "We can at least get some generic sneakers."
    pass
else:
    #print"No cool shoes for me."
    pass

print "hi"


characters =["amy", "sadie", "court", "carlos"]
characters.append("mom")
print characters
print characters[1] #use index numbers 0-3 to get a name


movies = dict() #create dictionary object
movies = {"Star Wars":"Darth Vader", "Narnia":"Lucy"}
print movies["Star Wars"]

#loops

#while loop
#i = 0
#while i<9:
    #print "The count is", i
    #i = i+1

#for loop for a specific number os times----

#for i in range(0,9):
     #print "The count is", i
     #i = i+1


#FOR EACH LOOP ----

#prints out list
rappers = ["Tupac", "nas", "biggie smalls"]
for r in rappers:
    #print "One of the best rappers is" + r
    pass


#FUNCTIONS---------------------

#X = 2 #scope

#def calcArea(h, w):
    #area = h * w
    #return area + x

#passing variables
#a = calcArea(20, 40);
#print a
#print "My area is " + str(a) + "sqft"
#print a




#how to put variables into a larger string

#weight = 200
#height = 63
#message = '''
#Your height is {height} and your weight is {weight}

#message = message.format(**locals())
#print message

#locals method takes the variables and puts it in
# the same place of the {} variables identified

title = "Contact Us"
body = "You can contact us at contact@us.com"
message = '''
<!DOCTYPE HTML>
<html>
    <head>
     <title>{title}</title>
    </head>
    <body>
    {body}
    </body>
</html>







