'''
Amy Littlefield-Bousamra
10/2014
Design Patterns
Simple Login
'''
#use the webapp2 library

import webapp2

class MainHandler(webapp2.RequestHandler):  #declaring a class
    def get(self):  #indent here this function starts everything.
        about_button = Button()  #creating a variable
        about_button.label = "About Us"
        about_button.show_label()
        contact_button = Button()
        contact_button.label = "Contact Us"
        contact_button.show_label()
          #code goes here
class Button(object):
    def __init__(self):  #constructor set-up method self=this
        self.label = "" #public attribute
        self.__size = 60 #private attribute - two underscores
        self.color =
        #self.on_roll_over("Hello!!")

    def click(self): #is the this in javascript
        print "I've been clicked"

    def on_roll_over(self, message):
        print "You've rolled over my button" + message

    def show_label(self):
        print "My label is" + self.label
      #code goes here

  #never touch..it's what part of what makes python work within the browser
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

