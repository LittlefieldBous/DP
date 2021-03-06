'''
Amy Littlefield-Bousamra
10/2014
Design Patterns
Simple Login
'''
#use the webapp2 library

import webapp2
from pages import Page  #from package import the page Class
#could also write import pages

class MainHandler(webapp2.RequestHandler):  #declaring a class
    def get(self):  #indent here. This function starts everything. below is html5 within the python there is a page head, body and close definied by '''.

        #data objects
        gilligan = Member()
        gilligan.f_name = "Gilligan"
        gilligan.l_name = "Jones"
        gilligan.address = "406 Island View Drive"
        gilligan.state = "Hawaii"
        gilligan.zip = "92643"
        gilligan.email = "gilligan@live.com"

        skipper = Member()
        skipper.f_name = "The Skipper"
        skipper.l_name = "T. O'Toole"
        skipper.address = "407 Island View Drive"
        skipper.state = "Hawaii"
        skipper.zip = "92643"
        skipper.email = "skipper@live.com"

        maryann = Member()
        maryann.f_name = "Mary Ann"
        maryann.l_name = "Matthews"
        maryann.address = "412 Island View Drive"
        maryann.state = "Hawaii"
        maryann.zip = "92643"
        maryann.email = "skipper@live.com"

        #html
        page_head = '''<!DOCTYPE HTML>
<html>
    <head>
        <title>simple form</title>
        <link rel="stylesheet" href="css/styles.css">
    </head>
    <body> '''
        page_body = '''

        <header>
         <nav>
    <ul class="nav">
    <li><a href="#home">Veronica's Vineyards</a></li>
    <li><a href="#about">About</a></li>
    <li><a href="#tasting">Tasting Room</a></li>
    <li><a href="#wines">Our Wines</a></li>
    <li><a href="#events">Events</a></li>
    <li><a href="#visit">Visit Us</a></li>
    </ul>
    </nav>
    </header>

        <div id="theform">
        <h3>Sign-Up Below & Join Our Wine Club!</h3>
        <form method="GET" action="">
            <label>First Name: </label><input type="text" name="f_name" value = "First Name"  /> <br />
            <label>Last Name: </label><input type="text" name="l_name" value = "Last Name"/> <br />
            <label>Address: </label><input type="text" name="address" value="Address" id="address" /> <br />
            <label>State: </label><input type="text" name="state" value="State" id="state" /> <br />
            <label>Zip: </label><input type="text" name="zip" value="Zip" id="zip" /> <br />
            <label>Email: </label><input type="text" name="email" value="Email" id="email" /> <br />
            <h4>Please select your favorite type of wine.</h4>
            <select name = "dropdown" id="select">
            <option value = "rose" selected>Rose</option>
            <option value = "sparkling" selected>Sparkling</option>
            <option value = "dessert" selected>Dessert</option>
            <option value = "white" selected>White</option>
            <option value = "red" selected>Red</option>
            </select> <br /> <br />
            <h4>Would you like to receive our monthly newsletter regarding events and discounts?</h4>
           <label class="radio">No<input  type="radio" name="subject" value="No"/></label><label class="radio">Yes<input type="radio" name="subject" value="Yes" /></label><br/>
           <div id="textarea">
           <h4>We would love to hear from you! Please add any additional comments below.</h4><textarea name="content" cols="40" rows="5">
            </textarea>
            </div>

            <div class="clearfix"></div>

            <div id"terms">
          <input type="checkbox" name="terms" id="checkbox"/>Yes, Sign Me Up!
            </div>

            <br />
             <input type="submit" value="Submit" id="submit" />
        </div>'''
        page_close = '''
        </form>
    </body>
</html> '''
        #get information
        if self.request.GET:
            #stores info we got from the form

            f_name = self.request.GET['f_name']  #needs variables to work
            l_name = self.request.GET['l_name']  #needs variables to work
            address = self.request.GET['address']
            state = self.request.GET['state']
            zip = self.request.GET['zip']
            email = self.request.GET['email']
            content = self.request.GET['content']
            terms = self.request.GET['terms']
            dropdown = self.request.GET['terms']
            #print the information
            self.response.write(page_head + ' ' + f_name + l_name + ' ' + address + ' ' + state + ' ' + zip + ' ' + email + page_close)  #this is what I want printed whe returned...I'm not sure how to do the css for this?
        else:
            self.response.write(page_head + page_body + page_close) #prints the information on the page

        #data objects print
        mems = [gilligan, skipper, maryann]
        print mems[1].f_name
        print mems[1].l_name
        print mems[1].address
        print mems[1].state
        print mems[1].zip
        print mems[1].email

#data objects class example.
class Member(object):
    def __init__(self):
        self.f_name = ""
        self.l_name = ""
        self.address = ""
        self.state = ""
        self.zip = ""
        self.email = ""

#never touch..it's what part of what makes python work within the browser
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
