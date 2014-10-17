'''
Amy Littlefield-Bousamra
10/2014
Design Patterns
Simple Login
Reusable Library
I wasn't sure where to place the if else statement and couldn't figure it out in time.
'''


import webapp2
from library import SunflowerData, Sunflowers
from pages import ResultsPage

class MainHandler(webapp2.RequestHandler):    #declaring a class
        def get(self):
            #attributes
            #1.Sunflower Variety/brand -brand
            #2.Sunflower Height per inches - height
            #3.Sunflower Population per acre -population
            #4.Sunflower Yield Pounds/lbs per acre - lbs
            #5.Crop Harvest Year - year


            sd1 = SunflowerData()
            sd1.brand = ''       # creating attributes here...
            sd1.height =  ''
            sd1.population = ''
            sd1.pounds = ''
            #calling a function
            #sd1.year = 2014
            #lib.add_sunflower(sd1)

            p = ResultsPage() #I want to make an instance
            lib = Sunflowers()
            p.format_all()
            lib.calc_profit()

            if self.request.GET: #has to be in handler
            #stores info we got from the form

                brand = self.request.GET['brand']  #needs variables to work
                height = self.request.GET['height']  #needs variables to work
                population = self.request.GET['population']
                pounds = self.request.GET['pounds']
                year = self.request.GET['year']

                self.response.write(p.body + "<div id='wrapper'>"+ "<h3>" "Sunflower Varieties Profit Calculator" + "</h3>" + ' ' + "<div id='name'>" + "Sunflower Variety/Brand:" + brand + "</div>" + "<div id='height2'>" + "Sunflower Height:" + height + "</div>" + "<div id='population2'>" + "Population per Acre:" + ' ' + population + "</div>" + "<div id='pounds2'>" + "Pounds per Acre:" + pounds + ' ' + "<div id='year2'>" + year + "</div>" "</br>" + "</div>" + p.close)
             #this is what I want printed whe returned...I'm not sure how to do the css for this?
            self.response.write(p.head + p.body + p.close)   #prints the information on the page




        #example of data objects that user could enter...
        #1.Sunflower Variety/brand -brand
        #2.Sunflower Height per inches - height
        #3.Sunflower Population per acre -population
        #4.Sunflower Yield Pounds/lbs per acre - lbs
        #5.Crop Harvest Year - year

'''
        sb1 = SunflowerData()
        sb1.brand = "Croplan 306"
        sb1.height =  64.4
        sb1.population = 19000
        sb1.yield = 2390 #calling a function
        sb1.year = 2012
        lib.add_sunflower(sb1)

        sb = SunflowerData()
        sb2.brand = "Panther"
        sb2.height = 66.3  #inches tall
        sb2.population = 18000  #plants per acre"
        sb2.yield = 2010   #pounds per acre calling a function
        sb2.year = 2012  #Harvest year
        lib.add_sunflower(sb2)

        sb = SunflowerData()
        sb2.brand = "Teton"
        sb2.height = 65.5  #inches tall
        sb2.population = 17500  #plants per acre"
        sb2.yield = 2050  #pounds per acre calling a function
        sb2.year = 2012   #Harvest year
        lib.add_sunflower(sb2)
'''

        #p.body = lib.compile_list() + lib.calc_time_span()
        #lib.sunflower_list = [md1, md2] = if it was public
        #self.response.write(p.print_out())


#do not touch
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
