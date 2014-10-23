class Page(object):  #borrowing stuff from the object class
    def __init__(self):
        self._title = "Welcome!" #private
        self._css = "css/styles.css" #private
        self._head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>{self._title}</title>
        <link href="{self._css}" rel="Stylesheet" type="text/css" />
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

    <section>
    <div id="links">
    <nav>
    <ul>
    <li id="home"><a href="?fabric=homeDecor">Home Decor</a></li>
    <li id="boy"><a href="#boy">Boy Prints</a></li>
    <li id="girl"><a href="#girl">Girl Prints</a></li>
    <li id="nature"><a href="#nature">Nature Prints</a></li>
    <li id ="animals"><a href="#animals">Animals</a>
    </li>
    </ul>
    </nav>
    </div>

  <div class ="info" data-id="home">
    <h2>Home Decor Fabric</h2>
    <br>
            <h4>Tree Blue Square</h4>
            <img src="images/treesquare.png" class="homeDecor">

            <h4>Tree Green Square</h4>
            <img src="images/greensquare.png" class="homeDecor">

            <h4>White Bird</h4>
            <img src="images/birdie.png" class="homeDecor">

            <h4>Round Tree 01</h4>
            <img src="images/roundtree.png" class="homeDecor">

            <h4>Round Tree 02</h4>
            <img src="images/whitestem.png" class="homeDecor">
    </div>

    <div class ="info" data-id="boy">
    <h2>Fabric Prints for boys</h2>
    <br>
            <h4>Blue Fish</h4>
             <img src="images/bluefish.png" class="boys">

            <h4>Green Fish</h4>
            <img src="images/greenfish.png" class="boys">

            <h4>Fish Orange</h4>
            <img src="images/orangefish.png" class="boys">

            <h4>Frogs!</h4>
            <img src="images/frogs.png" class="boys">

            <h4>Snow Boarder</h4>
             <img src="images/snowboarder.png" class="boys">
    </div>


    <div class ="info" data-id="girl">
    <h2>Fabric Prints for Girls</h2>
    <br>
            <h4>Butterfly Flight 02</h4>
            <img src="images/bf2flight.png" class="girls">

            <h4>Butterfly Border</h4>
            <img src="images/bfborder2.png" class="girls">

            <h4>Ballet Duo</h4>
            <img src="images/duoballet.png" class="girls">

            <h4>Ballerinas</h4>
            <img src="images/smballet.png" class="girls">

            <h4>Pink Fish</h4>
            <img src="images/pinkfish.png" class="girls">

             <h4>Golfer Girl</h4>
            <img src="images/ladygolfer.png" class="girls">
    </div>

    <div class ="info" data-id="nature">
    <h2>Nature Prints</h2>
    <br>
            <h4>Camping</h4>
            <img src="images/camp.png" class="nature">

            <h4>Camping 02/basic repeat</h4>
            <img src="images/rcamp.png" class="nature">

            <h4>Curly Tree</h4>
            <img src="images/curltree.png" class="nature">

            <h4>Moon Tree</h4>
            <img src="images/moontree.png" class="nature">

      </div>
           <div class ="info" data-id="animals">
    <h2>Animal Prints</h2>
    <br>
            <h4>Elephant Heart</h4>
            <img src="images/valentine.png" class="animals">

            <h4>Elephant Circus Heart</h4>
            <img src="images/circus.png" class="animals">

            <h4>Racoons!</h4>
            <img src="images/racoon.png" class="animals">

            <h4>Penguin</h4>
            <img src="images/penguin.png" class="animals">

            <h4>Colorful Bird</h4>
            <img src="images/colorbird.png" class="animals">
            </div>

    </div>
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
            self._ul_li_ += '<li id="home"' + item[0]
            if len(item)>4:
                self._ul_li += '" />'

            print self._ul_li

    #POLYMORPHISM
    def print_out_li(self):
        return self._head + self._body + self._ul_open + self._ul_li + self._ul_close + self._close