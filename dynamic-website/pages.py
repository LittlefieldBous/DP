
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
    <div id = "wrapper">
    <header>
            <nav id ="links">
            <ul>
            <li <a href="#dragon">The Dragon</a></li>
            <li id="satyr"><a href="#satyr">The Satyr</a></li>
            <li id="mermaid"><a href="#mermaid">The Mermaid</a></li>
            <li id="phoenix"><a href="#phoenix">The Phoenix</a></li>
            <li id="unicorn"><a href="#unicorn">The Unicorn</a></li>
            </ul>
            </nav>
             <h1>Friedrich Johann Justin Bertuch</h1>
    <h2>German Artist/Writer 1747-1822</h2>
    <img src="images/Bertuch.jpg" id ="bertuch" alt="drawing of a unicorn by Bertuch">
            <h4> The origins of Bertuch's mythological creatures in literature</h4>
    </header>
  </div>

 """
        self.close = """
        <div id = "creatures">
            <div id ="info">
        </div>
        </div>
    </body>
</html> """


    def print_out(self):
        all = self.head + self.body + self.close  #print out and return all sections of the html.
        all = all.format(**locals())
        return all

    #def print_out(self):  #create print out method
        #return self.head + self.body + self.close

class ContentPage(Page):    #its inheriting it from the page
    def __init__(self):    #contstructor function for the super class
        super(ContentPage, self).__init__()
        self._div_open= '<div method = "GET">'
        self._div_close = '</div>'
        self.__objects = []
        self._div_objects = ''

    @property
    def objects(self):
        pass

    @objects.setter
    def objects(self, arr): #2nd parameter array
        #change my private inputs variable.
        self.__objects = arr
        #sort through the mega array and create html inputs.
        for item in arr:  #for each item in array  '# on next line was : print item   #print it
            self._div_objects += item[0] + item[1] + item[2] + item[3] +  item[4] + item[5]
            #if there is a third item add ity in...otherwise... end the tag

            print self._div_objects


        #def print_out_form(self):  #use all the attributes in page print function
            #return self.head + self.body + self._table_open +self._table_objects + self._table_close + self.close
