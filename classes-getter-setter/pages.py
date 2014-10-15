class Page(object):
    def __init__(self):
        self.__title = "Welcome!" #private
        self.__css = "css/styles.css" #private
        self.head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>{self.title}</title>
        <link href="{self.css}" rel="Stylesheet" type="text/css" />
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

    @property
    def title(self):
        return

    @title.setter
    def title(self, new_title):
        self.__title = new_title

        @property
        def css(self):
            pass

        @css.setter
        def css(self, new_css_file):
            self.__css = new_css_file