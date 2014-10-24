'''
Amy Littlefield-Bousamra
10/2014
Design Patterns
Data-Object
'''
#use the webapp2 library

import webapp2

class MainHandler(webapp2.RequestHandler):  #declaring a class
    def get(self):  #indent here this function starts everything.


        luke = Character()
        luke.name = "Luke Skywalker"
        luke.profession = "Jedi Knight"
        luke.age = 26
        luke.home_planet = "Tattooine"

        leia = Character()
        leia.name = "Princess Leia"
        leia.profession = "Princess"
        leia.age = luke.age
        leia.home_planet = "Alderan"

        yoda = Character()
        yoda.name = "Master Yoda"
        yoda.profession = "Jedi Knight"
        yoda.age = 762
        yoda.home_planet = "Dagobah"

        chars = [luke, leia, yoda]
        print chars[1].profession #1 is leia 0 is luke

class Character(object):
    def __init__(self): #constructor function
        self.name = ""  #name of character
        self.profession = ""
        self.age = 0
        self.home_planet = ""

def click(self): #self is the this in javascript
        print "I've been clicked"



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

