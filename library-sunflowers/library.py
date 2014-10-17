'''
Amy Littlefield-Bousamra
10/2014
Design Patterns
Reusable Library
'''

class Sunflowers(object):
    def __init__(self):
        self__sunflower_list = []

    def addSunflower(self, s):
        self.__sunflower_list.append(s)
        print s.brand

    def compileList(self):
        output = ''
        for sunflower in self.__sunflower_list:
            output += 'Brand' + sunflower.brand + '<br />'
            return output



class SunflowerData(object): #sunflower data
    def __init__(self):   #put down attributes/data that we are collecting instances that exist for sunflower data
        self.brand = ''
        self.height = ''
        self.population = ''
        self.lbs = ''
        self__year = 0  #check for valid year

        #self.cwt = 100 will need to calculate 100lbs/lbs per acre/yield
        #self.profit = 25   #$25 for every cwt or 100lbs/pounds of sunflower seeds

        self.__sunflower_list = []
        #sunflower list array
        #have an array to hold the sunflower information
        #some way to add to the array
        #generate list of sunflowers at the end
        #calculate profit for each variety of sunflower

    #year
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

    #height
    @property
    def year(self):
        return self.height

    @year.setter
    def year(self, h):
        if h > 350:  #if the height is not valid
            print "Error, invalid height!"
            self.height = 60
        else:
            self.height = h

     #population
    @property
    def year(self):
        return self.population

    @year.setter
    def year(self, p):
        if p < 5:  #if the height is not valid
            print "Error, invalid population!"
            self.population = 17000
        else:
            self.population = p

     #lbs
    @property
    def year(self):
        return self.lbs

    @year.setter
    def year(self, l):
        if l < 500:  #if the height is not valid
            print "Error, invalid lbs per acre!"
            self.lbs = 1800
        else:
            self.lbs = l


'''
    def add_sunflower(self, s):
        self.__sunflower_list.append(s)
        print s.brand
        #<Movie Data Object >

    def compile_list(self):
        output = ''
        for sunflower in self.__sunflower_list:  #for each sunflower in our sunflower array
            output += 'Sunflower Brand: ' + sunflower.brand + 'Sunflower Height: ' + sunflower.height + 'Sunflower Population: ' + str(sunflower.population) + str(sunflower.pounds) + str(sunflower.year)
        return output

    def calc_time_span(self):
'''
        #calculate the profit based on the lbs per acre and the estimate of $25 per 100lb/cwt
'''
        yields= []
            for sunflowerin self.__sunflower_list:
            yield.append(sunflower.yields)

        #divide the l00lbs/cwt by the number of acres
        cwt = 100
        num = sunflower.yields
        num2 = 25
        profit = 100/sunflower.yields * 25
        #return the span of time
            return 'The profit earned from this sunflower variety/brand is' + profit

class SunflowerData(object):  # data object
    def __init__(self):
        self.brand = ''
        self.height = ''
        self.population = ''
        self.yields = ''
        self.__year = ''  # check for valid year


'''