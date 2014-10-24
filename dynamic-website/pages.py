
'''
Amy Littlefield-Bousamra
10/2014
Design Patterns
Dynamic Website
'''

class Page(object):  #borrowing stuff from the object class
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
 <table method="GET" action=">
    <tr id="origin">
        <th>Origin:</th>
        <td>(Possible origin) Chang Qu,Chinese historian 4th Century BC</td>
    </tr>
    <tr id ="description">
        <th>Description:</th>
        <td>A gigantic reptile with lion claws, scaly skin,tail of a serpent, wings and usually can breathe fire.</td>
    </tr>

    <tr id ="literary">
        <th>Literary Origin:</th>
        <td>Greek Myth: Jason and the Golden Fleece-Argonautica written by Apollonius of Rhodes around 1300 BC.</td>
    </tr>
     <tr id ="character">
        <th>Character's Name:</th>
        <td>First Dragon's character's name:Kholkikos or Colchian-that guarded the golden fleece.</td>
    </tr>
      <tr id ="famous">
        <th>Best Known Dragon:</th>
        <td>Puff the Magic Dragon</td>
    </tr>
 </table>
 </div>
 </div>
 </section>

</div>
   """
        self.close = """
    </body>
</html> """

    def print_out(self):
        all = self.head + self.body +  self.close  #print out and return all sections of the html.
        return all



'''
    def print_out(self):  #create print out method
        return self.head + self.body + self.close

class ContentPage(Page):    #its inheriting it from the page
    def __init__(self):    #contstructor function for the super class
        super(ContentPage, self).__init__()
        self._table_open= '<table method = "GET">'
        self._table_close = '</table>'
        self.__objects = []
        self._table_objects = ''

    @property
    def objects(self):
        pass

    @objects.setter
    def objects(self, arr): #2nd parameter array
        #change my private inputs variable.
        self.__objects = arr
        #sort through the mega array and create html inputs.
        for item in arr:  #for each item in array  '# on next line was : print item   #print it
            self._table_objects += '<td id="origin">' + item[0] + '</td>' + '<td id="description">' + item[1] + '</td>'+'<td id="description">' + item[2] + '</td>' + '<td id="literary">' + item[3] + '</td>' + '<td id="character">' + item[4] + '</td>'+ '<td id="famous">' + item[5] + '</td>'
            #if there is a third item add ity in...otherwise... end the tag
            if len(item) > 4:
                self._table_objects += 'placeholder"' + item[2]+'" />'
            #otherwise ..end the tag
            else:
                self._table_objects += '" />'

            print self._table_objects


    def print_out_form(self):  #use all the attributes in page print function
        return self.head + self.body + self._table_open +self._table_objects + self._table_close + self._close

'''