'''
Amy Littlefield-Bousamra
10/2014
Design Patterns
Dynamic Website
'''

import webapp2
from data import Data, DataPage
from pages import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()   #I want to make an instance of page
        d = DataPage()

        p.css = "css/styles.css"
        self.response.write(p.print_out())  # prints it out

        #data objects
        dragon = Data()
        dragon.origin = "Chang Qu,Chinese historian 4th Century BC"
        dragon.description = "A gigantic reptile with lion claws, scaly skin,tail of a serpent, wings and usually can breathe fire"
        dragon.literary = "Greek Myth: Jason and the Golden Fleece, Argonautica written by Apollonius of Rhodes around 1300 BC."
        dragon.character = "First Dragon's character's name: Kholkikos or Colchian-that guarded the golden fleece."
        dragon.famous = "Puff the Magic Dragon"

        satyr = Data()
        satyr.origin = "Greek Mythology - Evidence in writing from Sophocles and Euripides"
        satyr.description = "Look like men but with goat hooves for feet and a goat's tail. They are known for playing pipes and being tricksters."
        satyr.literary = "Greek Myth: Cyclops, by Euripides, 5th century BC"
        satyr.character = "Greek Satyr named: Pan- Son of Hermes"
        satyr.famous = "Mr Tumnus - The Lion, The Lion, the Witch and the Wardrobe- by C.S.Lewis."

        mermaid = Data()
        mermaid.origin = "Syria - Atargatis from ancient Babylon religion"
        mermaid.description = "A woman with fish like fins for feet that lives in the sea. They usually are beautiful and lure sailors with their songs."
        mermaid.literary = " 1000 BC: The first stories appeared in ancient Assyria, where the goddess Atargatis changed into a mermaid after killing her human lover. "
        mermaid.character = "Atargatis from Syria & Greek Legend of Thessalonike said to live in the Aegean Sea"
        mermaid.famous = "The Little Mermaid - written by Hans Christian Anderson"

        phoenix = Data()
        phoenix.origin = "Egypt"
        phoenix.description = "A large bird as big as an eagle with colorful feathers. Has the ability to die in it's own fire only to be resurrected and come to life again."
        phoenix.literary = " An egyptian myth says that the Bennu(another name for the phoenix) bird burst forth from the heart of Osiris "
        phoenix.character = "The phoenix is the fire bird used as a chariot for the Hindu god Vishnu. This stry appears in the Hindu epic Ramayana."
        phoenix.famous = "Harry Potter: J.K. Rowlings has used a phoenix as a central symbol in her stories."

        unicorn = Data()
        unicorn.origin = "Mesopotamian art and myths from India and China "
        unicorn.description = "A white horse with a single horn on the top of its head"
        unicorn.literary = " 400 BC: Greek historian Ctesuas and in the bible God is said to have the strength of a unicorn. "
        unicorn.character = "Named Karkadann the unicorn was strong and magical - From Persian and Arabia mythology"
        unicorn.famous = "King Arthur and the Unicorn"


#conditional or/and loop needed but not sure where or exactly how...
'''
        if self.request.GET:
            origin = self.request.GET['origin']
            description = self.request.GET['description']
            literary = self.request.GET['literary']
            character = self.request.GET['character']
            famous = self.request.GET['famous']
        else:

            self.response.write(p.body + "<div id='wrapper'>"+ "<h3>" "Mythological Creatures" + "</h3>" + ' ' + "<div id='origin'>" + "Origin:" + self.origin + "</div>" + "<div id='description'>" + "Description:" + self.description + "</div>" + "<div id='literary'>" + "Literature:" + ' ' + self.literary + "</div>" + "<div id='character'>" + "Best Known:" + self.famous + "</div>" "</br>"  +  "</div>" + p.close)
             #this is what I want printed whe returned...I'm not sure how to do the css for this?
            self.response.write(p.head + p.body + p.close)   #prints the information on the page

'''

#do not touch
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
