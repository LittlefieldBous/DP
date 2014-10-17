'''
Amy Littlefield-Bousamra
10/2014
Design Patterns
Reusable Library
'''
class Sunflowers(object):
    def __init__(self):
        self.__sunflower_list = []


    def add_Sunflower(self, s):
        self.__sunflower_list.append(s)
        print s.brand
        print s.pounds

    '''
    def compile_list(self):
        output = ''
        for sunflower in self.__sunflower_list:
            output += 'Brand:' + sunflower.brand + 'Year:' + str(sunflower.year) + 'Pounds Per Acre' + sunflower.pounds + "#Sunflowers per Acre" + sunflower.population
    '''

    def calc_profit(self):
        pounds = 1500  # not certain how to get number sunflower.pounds self.pounds
        cwt = 100
        price = 25
        profit = pounds/cwt * price
        print profit

class SunflowerData(object): #sunflower data
    def __init__(self):   #put down attributes/data that we are collecting instances that exist for sunflower data
            self.brand = ''
            self.height = ''
            self.population = ''
            self.pounds = ''
            self.__year = 0  #check for valid year

        #self.cwt = 100 will need to calculate 100lbs/lbs per acre/yield
        #self.profit = 25   #$25 for every cwt or 100lbs/pounds of sunflower seeds

        #self.__sunflower_list = []
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

    '''
    #height
    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, h):
        if h > 350:  #if the height is not valid
            print "Error, invalid height!"
            self.height = 60
        else:
            self.height = h

     #population
    @property
    def population(self):
        return self.population

    @population.setter
    def population(self, p):
        if p < 5:  #if the height is not valid
            print "Error, invalid population!"
            self.population = 17000
        else:
            self.population = p


    @property
    def pounds(self):
        return self.pounds

    @pounds.setter
    def year(self, l):
        if l < 500:  #if the height is not valid
            print "Error, invalid lbs per acre!"
            self.pounds = 1800
        else:
            self.pounds = l

'''
