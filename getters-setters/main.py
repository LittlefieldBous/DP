import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #tommy's grades
        t = Transcript()
        t.grade1 = 90  #instance of the grade
        t.grade2 = 100
        t.quiz1 = 75
        t.quiz2 = 99
        t.final_grade = 99 #over-writes tommy's grade
        self.response.write("Tommy's final grade is" + str(t.final_grade))
        #print t.final_grade_getter  #final grade is private with 2 underscores

        #sally's grades
        s = Transcript()
        s.grade1 = 45
        s.grade2 = 80
        s.quiz1 = 66
        s.quiz2 = 76
        s.calc_grade() #calls the calculation method
        self.response.write("<br />Sally's final grade is" + str(s.final_grade))

class Transcript(object):
    def __init__(self):
        self.grade1 = 0 #no underscores - public
        self.grade2 = 0
        self.quiz1 = 0
        self.quiz2 = 0
        self.final_exam = 0
        self.__final_grade = 0 #two underscores - private

    def final_grade(self):
        return self.__final_grade

    @property
    def final_grade(self):
        return self.__final_grade

    @final_grade.setter
    def final_grade(self, new_final_grade):
        self.__final_grade = new_final_grade

    def calc_grade(self):
        self.__final_grade = (self.grade1 + self.grade2 + self.quiz1 + self.quiz2 + self.final_exam)/5 #accessing function called final grade -calculate final grade


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
