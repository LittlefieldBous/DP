'''
Amy Littlefield-Bousamra
10/2014
Design Patterns
Reusable Library
'''
class FavoriteMovies(object):
    def __init__(self):
        self.__movie_list = []
        #movie list array
        #have an array to hold the movie information
        #some way to add to the array
        #generate list of movies at the end
        #calculate time span between movies

    def add_movie(self, m):
        self.__movie_list.append(m)
        print m.title
        #<Movie Data Object >

    def compile_list(self):
        output = ''
        for movie in self.__movie_list:  #for each movie in our movie array
            output += 'Title: ' + movie.title + '(' + str(movie.year) + ') Directed by: ' +  movie.director + '<br />'
        return output

    def calc_time_span(self):
        '''calculate the time in between movies
        '''
        years = []
        for movie in self.__movie_list:
            years.append(movie.year)

        #sort years from low to high
        years.sort()

        #subtract the low year from the high year
        num = len(years) - 1
        span = years[num] - years[0]
        #return the span of time
        return 'The span between films entered is' + str(span)

class MovieData(object):  # data object
    def __init__(self):
        self.title = ''
        self.__year = 0   # check for valid year
        self.director = ''

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, y):
        if y > 2014:  #if the date is not valid
            print "Error, invalid date!"
            self.__year = 2014
        else:
            self.__year = y

