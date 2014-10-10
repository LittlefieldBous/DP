'''
Amy Littlefield-Bousamra
10/2014
Design Patterns
Simple Login
I wasn't sure where to place the if else statement and couldn't figure it out in time.
'''
class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        self.response.write(print p.print_out()) #print into our browser

class Page(object):
    def __init__(self):
        self.title = "Welcome!"
        self.css = "css/styles.css"
        self.head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>{self.title}</title>
        <link href="{self.css}" rel="Stylesheet" type="text/css" />
    </head>
    <body>
     """
        self.body = """
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
        </div>
         """
        self.close = """
    </body>
</html> """

def print_out(self):
        all = self.head + self.body + self.close  #print out and return all sections of the html.
        all = all.format(**locals())
        return all
