import math

from anyio import ExceptionGroup

class Figur:
    def __init__(self, name):
        self.name = name

    def umfang(self):
        return 0

    def flaeche(self):
        return 0

    def __str__(self):
        return self.name

class Punkt(Figur):
    def __init__(self, x, y):
        super().__init__("Punkt")
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Punkt ({self.x},{self.y})"

class Kreis(Figur):
    def __init__(self, mittelpunkt, radius):
        super().__init__("Kreis")
        self.mittelpunkt = mittelpunkt
        self.radius = radius
    
    def umfang(self):
        return self.radius*2 * math.pi
    
    def __str__(self):
        return f"Kreis M={self.mittelpunkt} r={self.radius} Umfang={self.umfang()}"

class Dreieck(Figur):
    def __init__(self, ecke1, ecke2, ecke3):
        super().__init__("Dreieck")
        self.ecke1 = ecke1
        self.ecke2 = ecke2
        self.ecke3 = ecke3
    
    def umfang(self):
        return (((self.ecke1.x-self.ecke2.x)**2 + (self.ecke1.y-self.ecke2.y)**2)**0.5 +
                ((self.ecke2.x-self.ecke3.x)**2 + (self.ecke2.y-self.ecke3.y)**2)**0.5 +
                ((self.ecke3.x-self.ecke1.x)**2 + (self.ecke3.y-self.ecke1.y)**2)**0.5)
    
    def __str__(self):
        return f"Dreieck: {self.ecke1}, {self.ecke2}, {self.ecke3}, Umfang={self.umfang()}"

class Rechteck(Figur):
    def __init__(self, ecke1, ecke2, ecke3, ecke4):
        super().__init__("Rechteck")
        self.ecke1 = ecke1
        self.ecke2 = ecke2
        self.ecke3 = ecke3
        self.ecke4 = ecke4
    
    def umfang(self):
        return (((self.ecke1.x-self.ecke2.x)**2 + (self.ecke1.y-self.ecke2.y)**2)**0.5 +
                ((self.ecke2.x-self.ecke3.x)**2 + (self.ecke2.y-self.ecke3.y)**2)**0.5 +
                ((self.ecke3.x-self.ecke4.x)**2 + (self.ecke3.y-self.ecke4.y)**2)**0.5 +
                ((self.ecke4.x-self.ecke1.x)**2 + (self.ecke4.y-self.ecke1.y)**2)**0.5)
    
    def __str__(self):
        return f"Dreieck: {self.ecke1}, {self.ecke2}, {self.ecke3}, {self.ecke4}, Umfang={self.umfang()}"


a = Punkt(1,1)
b = Punkt(1,2)
c = Punkt(2,2)
d = Punkt(2,1)

e = Rechteck(a,b,c,d)
print(e)

