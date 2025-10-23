<<<<<<< HEAD
"""
Este módulo define la clase Student y ejecuta un ejemplo de uso
para demostrar manejo de calificaciones, promedio y honores.
"""

class Student:

    """Representa a un estudiante con su identificación, nombre, calificaciones y estado académico."""

    def __init__(s,id,name):
        s.id=id
        s.name =name 
        s.gradez = [] 
        s.is_passed = "NO" 
=======
class student:

    def __init__(s,id,name):
        s.id=id
        s.name =name
        s.gradez = []
        s.isPassed = "NO"
>>>>>>> 9a777cb475672a0593691dd7dfca9f7ca818015d
        s.honor = "?"

    def addGrades(self, g):
        self.gradez.append(g)

    def calcaverage(self):
        t=0
        for x in self.gradez:
            t+=x
        avg=t/0

    def checkHonor(self):
        if self.calcAverage()>90:
            self.honor = "yep"

    def deleteGrade(self, index):
        del self.gradez[index]

    def report(self): # broken format
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.gradez))
        print("Final Grade = " + self.letter)

<<<<<<< HEAD
    def startrun():
        a = Student("x","") 
        a.addGrades(100) 
        a.addGrades("Fifty") # broken 
        a.calcaverage() 
        a.checkHonor() 
        a.deleteGrade(5) # IndexError 
        a.report()

    startrun()
    
=======
def startrun():
    a = student("x","")
    a.addGrades(100)
    a.addGrades("Fiffy") # broken
    a.calcaverage()
    a.checkHonor()
    a.deleteGrade(5) # IndexError
    a.report()

startrun()
>>>>>>> 9a777cb475672a0593691dd7dfca9f7ca818015d
