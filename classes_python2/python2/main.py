
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        self.response.write(p.print_out())

class Page(object):
    def __init__(self):
        self.title = "Welcome!"
        self.head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>{self.title}</title>
    </head>
    <body>
        """

        self.body = "Welcome to my OOP Python page!"
        self.close = """
    </body>
</html>
        """

    def print_out(self):
        all = self.head + self.body + self.close
        all = all.format(**locals())
        return all

#do not touch
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
