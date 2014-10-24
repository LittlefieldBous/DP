'''
Amy Littlefield-Bousamra
10/2014
Design Patterns
Dynamic Website
'''


class Creatures(object):  #class dataPage
    def __init__(self):
        self.__creature_list = []  #set creature list
        #creature list array
        #have an array to hold the creature information
        #some way to add to the array
        #generate list of creatures at the end


    def add_creature(self, s):  #add creatures
        self.__creature_list.append(s)
        print s.title
        print s.image
        print s.origin
        print s.description
        print s.literary
        print s.character
        print s.famous  #data objects


    def compile_list(self):
        output = ''
        for creature in self.__creature_list:
            output +=   '<h4>' + 'Title:' + '</h4>' + creature.title + '<h4>' + '<img>' + creature.image + '>' + '<br>' + 'Origin:' + '</h4>' + creature.origin + '<br>'+ 'Description:' + creature.description + '</td>'+ '<td>' 'Literary:' + creature.literary +  '</td>' + '<td>' +"Characters:" + creature.character + '</td>' + '<td>'+ "Best Known:" + creature.famous + '</td>'
        return output


class Data(object): #creature data
    def __init__(self):   #put down attributes/data that we are collecting instances that exist for sunflower data
        self.title = ''
        self.image = ''
        self.origin = ''
        self.description = ''
        self.literary = ''
        self.character = ''
        self.famous = ''

    def click(self): #self is the this in javascript
        print "I've been clicked"
