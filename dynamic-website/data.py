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

        if self.request.GET:
            origin = self.request.GET['origin']
            description = self.request.GET['description']
            literary = self.request.GET['literary']
            character = self.request.GET['character']
            famous = self.request.GET['famous']
        else:

         self.response.write(p.body + "<div id='wrapper'>"+ "<h3>" "Mythological Creatures" + "</h3>" + ' ' + "<div id='name'>" + "Sunflower Variety/Brand:" + brand + "</div>" + "<div id='height2'>" + "Sunflower Height:" + height + "</div>" + "<div id='population2'>" + "Population per Acre:" + ' ' + population + "</div>" + "<div id='pounds2'>" + "Pounds per Acre:" + pounds + ' ' + "<div id='year2'>" + year + "</div>" "</br>"  +  "</div>" + p.close)
             #this is what I want printed whe repturned...I'm not sure how to do the css for this?
            self.response.write(p.head + p.body + p.close)   #prints the information on the page
