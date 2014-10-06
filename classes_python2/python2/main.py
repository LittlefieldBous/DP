
import webapp2
from pages import Page  #from package import class

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        p.body ="Miss Piggy likes Chocolate!" #modify's self.body
        self.response.write(p.print_out())


#do not touch
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
