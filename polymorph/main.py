
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()  #create instance of form page
        p.inputs = [['first_name', 'text', 'First Name'], ['last_name', 'text', 'Last Name'], ['Submit', 'submit']]
        self.response.write(p.print_out())

class Page(object):  #borrowing stuff from the object class
    def __init__(self):
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title></title>
    </head>
    <body> '''

        self._body = 'Filler'  #body attribute
        self._close = '''
    </body>
</hmtl> '''

    def print_out(self):   #create a print out method
        return self._head + self._body + self._close


class FormPage(Page):   #its inheriting it from page
    def __init__(self): #constructer function for the super class
        super(FormPage, self).__init__()    # option 2: Page.__init__()
        self._form_open = '<form method = "GET">'
        self._form_close = '</form>'
        self.__inputs = []  #to store information
        self._form_inputs = ''
        #<input type = "text" value = "" name = "first_name" placeholder ="First Name" />
        # ['first_name', 'text', 'First Name']   #value, type placeholder
        #<input type = "text" value = "" name="last_name" placeholder ="Last Name" />
        #<input type = "submit" value ="Submit" />

    # a way to access inputs
    @property
    def inputs(self):
        pass

    @inputs.setter
    def inputs(self, arr): #2nd parameter array
        #change my private inputs variable.
        self.__inputs = arr
        #sort through the mega array and create html inputs.
        for item in arr:  #for each item in array  '# on next line was : print item   #print it
            self._form_inputs += '<input type="' +  item[1] + '" name=" ' + item[0]
            #if there is a third item add ity in...otherwise... end the tag
            if len(item) > 2:
                self._form_inputs += 'placeholder"' + item[2]+'" />'
            #otherwise ..end the tag
            else:
                self._form_inputs += '" />'

        print self._form_inputs

#POLYMORPHISM ALERT ---method override
    def print_out_form(self):  #use all the attributes in page print function
        return self._head + self._body + self._form_open +self._form_inputs + self._form_close + self._close

#do not touch
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
