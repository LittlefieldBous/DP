
import webapp2
from pages import Page
#from data import Data

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()   #I want to make an instance of page
        p.li = [['home'],['boy'],['girl'],['nature'],['animals']]
        p.css = "css/styles.css"
        #d = Data()

        #d.home = self.request.GET['home']
        #d.boy = self.request.GET['boy']
        #d.girl = self.request.GET['girl']
        #d.nature = self.request.GET['nature']
        #d.animals = self.request.GET['animals']
        self.response.write(p.print_out())

        #self.response.write(p.print_out())
        #self.response.write('Hello world!')
        #if self.request.GET: #has to be in handler
            #stores info we got from the form

            #home = self.request.GET['home']  #needs variables to work
            #boy = self.request.GET['boy]  #needs variables to work
            #girl = self.request.GET['girl']
            #sports = self.request.GET['sports']
            #seasonal = self.request.GET['seasonal']
            #contact = self.request.GET['contact']
            #self.response.write(p.head + ' ' + p.body + p.close)
        #else:
            #self.response.write(p.head + p.body + p.close) #prints the information on the page
""
#do not touch
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
