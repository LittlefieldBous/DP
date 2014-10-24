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
'''
class   Data(object): #creature data
    def __init__(self):   #put down attributes/data that we are collecting instances that exist for sunflower data
        self.origin = ''
        self.description = ''
        self.literary = ''
        self.character = ''
        self.famous = ''
'''

#do not touch
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
