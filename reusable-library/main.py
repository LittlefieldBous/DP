'''
Amy Littlefield-Bousamra
10/2014
Design Patterns
Simple Login
Reusable Library
I wasn't sure where to place the if else statement and couldn't figure it out in time.
'''

import webapp2
from library import MovieData, FavoriteMovies
from pages import Page


class MainHandler(webapp2.RequestHandler):
    def get(self):

        #page for class
        p = Page()
        lib = FavoriteMovies()  #lib object

        #movie title
        #year movie was made
        #director of film
        md1 = MovieData()
        md1.title = "The Princess Bride"
        md1.year = 1989  #calling a function
        md1.director = "Rob Reiner"
        lib.add_movie(md1)

        md2 = MovieData()
        md2.title = "Dune"
        md2.year = 1986  #calling a function
        md2.director = "David Lynch"
        lib.add_movie(md2)

        md2 = MovieData()
        md2.title = "Star Wars"
        md2.year = 1977  #calling a function
        md2.director = "George Lucas"
        lib.add_movie(md2)

        p.body = lib.compile_list() + lib.calc_time_span()
        #lib.movie_list = [md1, md2] = if it was public
        self.response.write(p.print_out())


#do not touch
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
