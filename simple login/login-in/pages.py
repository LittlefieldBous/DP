'''
Amy Littlefield-Bousamra
10/2014
Design Patterns
Simple Login
I wasn't sure where to place the if else statement and couldn't figure it out in time.
'''
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
        <form method="GET" action="">
            <label>First Name: </label><input type="text" name="f_name"  /> <br />
            <label>Last Name: </label><input type="text" name="l_name"  /> <br />
            <label>Address: </label><input type="text" name="address" /> <br />
            <label>State: </label><input type="text" name="state" /> <br />
            <label>Zip: </label><input type="text" name="zip" /> <br />
            <label>Email: </label><input type="text" name="email" /> <br />
            <label> Please verify your age: </label><input type="text" name="age" /> <br />
            <label>Please select your favorite type of wine. </label>
            <select name = "dropdown">
            <option value = "red" selected>Red</option>
            <option value = "white" selected>White</option>
            <option value = "rose" selected>Rose</option>
            <option value = "sparkling" selected>Sparkling</option>
            <option value = "dessert" selected>Dessert</option>
            </select> <br />
            <label>Would you like to receive our monthly newsletter regarding events and discounts?</label> <br />
            <input type="radio" name="subject" value="yes" /> Yes
            <input type="radio" name="subject" value="no" /> No <br />
            <p>We would love to hear from you! Please add any additional comments below.</p>
            <textarea name="content" cols="40" rows="5">
            </textarea>
             <input type="checkbox" name="member" value="on" /> Yes, I have read and agree to the terms and conditions. <br />
             <input type="submit" value="Submit" />
            </form>
         """
        self.close = """
    </body>
</html> """


