class Page(object):  #borrowing stuff from the object class
    def __init__(self):
        self.title = "Welcome!" #private
        self.css = "css/styles.css" #private
        self._head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>{self.title}</title>
        <link href="{self.css}" rel="Stylesheet" type="text/css" />
    </head>
   <body>
     """
        self._body = """

    <header>
   <h1>Amy Frances Designs</h1>
   <h2>Fabric and Print Design</h2>

   <p>Place a paragraph about designer here.</p>

    </header>

    <div class ="container">
          <nav>
    <ul class="nav">
    <li id="home"><a href="#home">Home Decor</a>
    <br>
    <p>Home Decor Fabric</p></li>
    <img src="images/treesquare.png" class="homeDecor">
    <img src="images/greensquare.png" class="homeDecor">
    <img src="images/birdie.png" class="homeDecor">
    <img src="images/roundtree.png" class="homeDecor">
    <img src="images/whitestem.png" class="homeDecor">
    </li>
    <li id="boy"><a href="#boy">Boy Prints</a>
    <br>
    <p>Fabrics for Boys</p>
    <img src="images/bluefish.png" class="boys">
    <img src="images/greenfish.png" class="boys">
    <img src="images/orangefish.png" class="boys">
    <img src="images/frogs.png" class="boys">
    <img src="images/snowboarder.png" class="boys">
    </li>
    <li id="girl"><a href="#girl">Girl Prints</a>
    <br>
    <p>Fabrics for Girls</p>
    <img src="images/bf2flight.png" class="girls">
    <img src="images/bfborder2.png" class="girls">
    <img src="images/duoballet.png" class="girls">
    <img src="images/smballet.png" class="girls">
    <img src="images/pinkfish.png" class="girls">
    <img src="images/ladygolfer.png" class="girls">
    </li>
    <li id="nature"><a href="#nature">Nature Prints</a>
    <br>
    <p>Nature Prints</p>
    <img src="images/camp.png" class="nature">
    <img src="images/forest.png" class="nature">
    <img src="images/curltree.png" class="nature">
    <img src="images/moontree.png" class="nature">
    </li>
    <li id ="animals"><a href="#animals">Animals</a>
    <br>
     <p>Animal Prints</p>
    <img src="images/valentine.png" class="animals">
    <img src="images/circus.png" class="animals">
    <img src="images/racoon.png" class="animals">
    <img src="images/penguin.png" class="animals">
    <img src="images/colorbird.png" class="animals">
    </li>
    <li id ="contact"><a href="#contact">Contact</a>
    <br>
    <p>This is where the contact information goes!</p>
    </li>
    </ul>
    </nav>

  </div>
   """
        self._close = """
    </body>
</html> """

    def print_out(self):  #create print out method
        return self._head + self._body + self._close

class ContentPage(Page):    #its inheriting it from the page
    def __init__(self):    #contstructor function for the super class
        super(ContentPage, self).__init__()
        self._ul_open= '<ul method = "GET">'
        self._ul_close = '</ul>'
        self.__li = []
        self._ul_li = ''

    @property
    def inputs(self):
        pass

    @inputs.setter
    def li(self, arr):  #change my private list variable
        self.__li = arr
        #sort through the array and create html lists based on the info there
        for item in arr:
            self._form_inputs += '<li id=" "' + item[1]
            if len(item)>4:
                self._ul_li += '" />'

            print self._ul_li
    def print_out_li(self):
        return self._head + self._body + self._ul_open + self._ul_li + self._ul_close + self._close