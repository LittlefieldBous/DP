'''
Amy Littlefield-Bousamra
10/2014
Design Patterns
Reusable library
'''
class ResultsPage(object): #contructor method-function
    def __init__(self):
        self.__title = "Welcome!" #public title Welcome! self is = to this
        self.css = "css/styles.css"
        self.__head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>Enter your information</title>
        <link href="css/styles.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
     """
        self.body = ""
        self.__error = ''
        self.__close = """
    </body>
</html>
        """

    def print_out(self):
        all = self.__head + self.body + self.__error +  self.__close  #print out and return all sections of the html.
        return all
