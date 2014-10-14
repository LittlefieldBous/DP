'''
Amy Littlefield-Bousamra
10/2014
Design Patterns
Simple Login
'''
#use the webapp2 library

import webapp2
from pages import Page   #from package import the Class

class MainHandler(webapp2.RequestHandler):  #declaring a class
    def get(self):  #indent here. This function starts everything. below is html5 within the python there is a page head, body and close definied by '''.
        p = Page() #I want to make an instance
        p.format_all()
        if self.request.GET: #has to be in handler
            #stores info we got from the form

            f_name = self.request.GET['f_name']  #needs variables to work
            l_name = self.request.GET['l_name']  #needs variables to work
            address = self.request.GET['address']
            state = self.request.GET['state']
            zip = self.request.GET['zip']
            email = self.request.GET['email']
            p.email = email
            content = self.request.GET['content']
            #terms = self.request.GET['terms']
            #dropdown = self.request.GET['terms']
            self.response.write(p.head + ' ' + p.body + "<div id='wrapper'>"+ "<h3>" "Congratulations on becoming a member of Veronica Vineyards!" + "</h3>" + ' ' + "<div id='name'>" + f_name + ' ' + l_name + "</div>" + "<div id='contact'>" + address + "</div>" + "<div id='state_zip'>" + ' ' + state + ' ' + zip + "</div>" + ' ' + "</br>" + "Look for your email confirmation at:" + ' ' + email + ' ' + "If errors occurred or you would like to update your address please contact us at veronicavineyards@outlook.com" + "</div>" + p.close)  #this is what I want printed whe returned...I'm not sure how to do the css for this?
        else:
            self.response.write(p.head + p.body + p.close) #prints the information on the page
""

#never touch..it's what part of what makes python work within the browser
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
