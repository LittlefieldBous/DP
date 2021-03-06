'''
Amy Littlefield-Bousamra
10/2014
Design Patterns
Dynamic Website
'''

import webapp2
from data import Data, Creatures  #importing Datapage
from pages import Page, ContentPage   #importing pages.py

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = ContentPage()   #I want to make an instance of page
        info = Creatures()  #data object instance
        p.css = "css/styles.css"


        #data objects
        #dragon d = data
        d1 = Data()
        d1.title = 'The Dragon'
        d1.image = '<img src="images/dragon.jpg" alt="drawing of a dragon by Bertuch">'
        d1.origin = "Chang Qu,Chinese historian 4th Century BC"
        d1.description = "A gigantic reptile with lion claws, scaly skin,tail of a serpent, wings and usually can breathe fire"
        d1.literary = "Greek Myth: Jason and the Golden Fleece, Argonautica written by Apollonius of Rhodes around 1300 BC."
        d1.character = "First Dragon's character's name: Kholkikos or Colchian-that guarded the golden fleece."
        d1.famous = "Puff the Magic Dragon"
        info.add_creature(d1)

        d2 = Data()
        d2.title = 'The Satyr'
        d2.image = '<img src="images/satyr.jpg" alt="drawing of a satyr by Bertuch">'
        d2.origin = "Greek Mythology - Evidence in writing from Sophocles and Euripides"
        d2.description = "Look like men but with goat hooves for feet and a goat's tail. They are known for playing pipes and being tricksters."
        d2.literary = "Greek Myth: Cyclops, by Euripides, 5th century BC"
        d2.character = "Greek Satyr named: Pan- Son of Hermes"
        d2.famous = "Mr Tumnus - The Lion, The Lion, the Witch and the Wardrobe- by C.S.Lewis."
        info.add_creature(d2)

        d3 = Data()
        d3.title = 'The Mermaid'
        d3.image = '<img src="images/mermaid.jpg" alt="drawing of a mermaid by Bertuch">'
        d3.origin = "Syria - Atargatis from ancient Babylon religion"
        d3.description = "A woman with fish like fins for feet that lives in the sea. They usually are beautiful and lure sailors with their songs."
        d3.literary = " 1000 BC: The first stories appeared in ancient Assyria, where the goddess Atargatis changed into a mermaid after killing her human lover. "
        d3.character = "Atargatis from Syria & Greek Legend of Thessalonike said to live in the Aegean Sea"
        d3.famous = "The Little Mermaid - written by Hans Christian Anderson"
        info.add_creature(d3)

        d4 = Data()
        d4.title = 'The Phoenix'
        d4.image = '<img src="images/phoenix.jpg" alt="drawing of a phoenix by Bertuch">'
        d4.origin = "Egypt"
        d4.description = "A large bird as big as an eagle with colorful feathers. Has the ability to die in it's own fire only to be resurrected and come to life again."
        d4.literary = " An egyptian myth says that the Bennu(another name for the phoenix) bird burst forth from the heart of Osiris "
        d4.character = "The phoenix is the fire bird used as a chariot for the Hindu god Vishnu. This stry appears in the Hindu epic Ramayana."
        d4.famous = "Harry Potter: J.K. Rowlings has used a phoenix as a central symbol in her stories."
        info.add_creature(d4)

        d5 = Data()
        d5.title = 'The Unicorn'
        d5.image = '<img src="images/unicorn.jpg" alt="drawing of a unicorn by Bertuch">'
        d5.origin = "Mesopotamian art and myths from India and China "
        d5.description = "A white horse with a single horn on the top of its head"
        d5.literary = " 400 BC: Greek historian Ctesuas and in the bible God is said to have the strength of a unicorn. "
        d5.character = "Named Karkadann the unicorn was strong and magical - From Persian and Arabia mythology"
        d5.famous = "King Arthur and the Unicorn"
        info.add_creature(d5)

        p.close = info.compile_list()
        #self.response.write(p.head + p.body + p.data + p.close)
        self.response.write(p.print_out())
        #self.response.write(self.head + self.body + self.close)
        #info.creature_list = [d1, d2, d3, d4, d5] #if it was public

        # prints it out
        #conditional or/and loop needed but not sure where or exactly how...

            #if id = "dragon"
            #return Data(d5)


#do not touch
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
