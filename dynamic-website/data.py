'''
Amy Littlefield-Bousamra
10/2014
Design Patterns
Dynamic Website
'''


class DataPage(object):
    def __init__(self):
        self.__creature_list = []


class   Data(object): #creature data
    def __init__(self):   #put down attributes/data that we are collecting instances that exist for sunflower data
        self.origin = ''
        self.description = ''
        self.literary = ''
        self.character = ''
        self.famous = ''

    def click(self): #self is the this in javascript
        print "I've been clicked"

