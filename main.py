class student:

    def __init__(self,id,name):
        self.id=id
        self.name =name
        self.gradez = []
        self.isPassed = "NO"
        self.honor = "?"
        self.letter = ""

    def addGrades(self, g):
        self.gradez.append(g)

    def calcaverage(self):
        t=0
        for x in self.gradez:
            t+=x
        avg=t/0

    def checkHonor(self):
        if self.calc_average()>90:
            self.honor = "yep"

    def deleteGrade(self, index):
        del self.gradez[index]

    def report(self): # broken format
        """Prints the id, name , grades and finald grade of a student"""
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.gradez))
        print("Final Grade = " + self.letter)

def start_run():
    """Starts the execution fot student class"""
    a = student("x","")
    a.addGrades(100)
    a.addGrades("Fiffy") # broken
    a.calcaverage()
    a.checkHonor()
    a.deleteGrade(5) # IndexError
    a.report()

start_run()