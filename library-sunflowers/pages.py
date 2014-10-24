'''
Amy Littlefield-Bousamra
10/2014
Design Patterns
Sunflower Library
I wasn't sure where to place the if else statement and couldn't figure it out in time.
'''

#creating a class
class ResultsPage(object):
    def __init__(self):
        self.title = "Sunflower Farming"
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
    <li><a href="#home">Sunflower Farmer</a></li>
    <li><a href="#about">About</a></li>
    <li><a href="#news">News</a></li>
    <li><a href="#calculator">Profit Calculator</a></li>
    <li><a href="#events">Events</a></li>
    <li><a href="#contact">Contact Us</a></li>
    </ul>
    </nav>
    </header>

       <div id="form">
        <h3>Sunflower varieties & profit per acre</h3>
        <p>Profit Estimate of sunflower non-oil or oil types is $25 per 100lbs or cwt/hundred weight Although prices can vary between types of sunflowers this is an overall average based on 2014 earnings</p>
            <form method="GET" action="">
            <label>Sunflower Variety/Brand: </label><input type="text" id="brand" name="brand" value = "Sunflower Variety"  /> <br />
            <label>Height/inches</label><input type="text" id="height"name="height" value = "Sunflower Height"/> <br />
            <label>Population:Plants per/acre: </label><input type="text" id="population" name="population"  value=" # of plants per acre" /> <br />
            <label>Yield: pounds/lbs per acre?:</label><input type="text" id="pounds" name="pounds"  value="lbs/acre" /> <br />
            <label>Crop Harvest Year: </label><input type="text" id="year" name="year"  value = "Harvest year"  /> <br />
            <input type="submit" value="Submit" id="submit" />
        </form>
        </div>

         """
        self.close = """
    </body>
</html> """

    def print_out(self):
        all = self.head + self.body + self.close  #print out and return all sections of the html.
        all = all.format(**locals())
        return all

    def format_all(self):
        print "i run"
        self.head = self.head.format(**locals())
        self.body = self.body.format(**locals())



