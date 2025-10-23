"""
Este módulo define la clase Student y ejecuta un ejemplo de uso
para demostrar manejo de calificaciones, promedio y honores.
"""

class Student:

    """Representa a un estudiante con su identificación, nombre, calificaciones y estado académico."""

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
        self.avg=t/len(self.gradez)

    def check_honor(self):
        
        """
        Determines if the student qualifies for honors.

        Honor status is set to 'yep' if the average grade 
        (calculated by calcaverage) is greater than 90.
        """
        if self.calc_average()>90:
            self.honor = "yep"

    def deleteGrade(self, index):
        """
        Deletes the grade at the specified index from the student's list of grades.
        
        Handles IndexError if the index is out of the list's bounds.
        """
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
