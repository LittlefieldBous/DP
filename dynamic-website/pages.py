
'''
Amy Littlefield-Bousamra
10/2014
Design Patterns
Dynamic Website
'''

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
   <h1>Friedrich Johann Justin Bertuch</h1>
   <h2>German Artist/Writer 1747-1822</h2>
   <p> The origins of Bertuch's mythological creatures in literature</p>

   <p>Place a paragraph about Bertuch here.</p>

    </header>

<div class ="container">

<section>
    <div id="creatureSection">
    <div id="links">
            <nav>
            <ul>
            <li id="dragon"><a href="#dragon">The Dragon</a></li>
            <li id="satyr"><a href="#satyr">The Satyr</a></li>
            <li id="mermaid"><a href="#mermaid">The Mermaid</a></li>
            <li id="phoenix"><a href="#phoenix">The Phoenix</a></li>
            <li id="unicorn"><a href="#unicorn">The Unicorn</a></li>
            <li id="snakeman"><a href="#snakeman">The Snakeman</a></li>
            <li id="griffin"><a href="#griffen">The Griffin</a></li>
            <li id="horse"><a href="#horse">The Water Horse</a></li>
            </ul>
            </nav>
        </div>
    </div>
</section>

<section>
 <div id ="info">
 <img src="images/dragon.jpg" alt="drawing of a dragon by Bertuch">
 <table>
    <tr>
        <th>Origin:</th>
        <td>(Possible origin) Chang Qu,Chinese historian 4th Century BS</td>
    </tr>
    <tr>
        <th>Description:</th>
        <td>A gigantic reptile with lion claws, scaly skin,tail of a serpent, wings and usually can breathe fire.</td>
    </tr>

    <tr>
        <th>Literary Origin:</th>
        <td>Greek Myth: Jason and the Golden Fleece-Argonautica written by Apollonius of Rhodes around 1300 BC.</td>
    </tr>
     <tr>
        <th>Character's Name:</th>
        <td>First Dragon's character's name:Kholkikos or Colchian-that guarded the golden fleece.</td>
    </tr>
     <tr>
        <th>Best Known Dragon:</th>
        <td>Puff the Magic Dragon</td>
    </tr>
 </table>
 </div>
 </div>
 </section>

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