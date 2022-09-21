from punto import Punto

class Rectangulo:
    def __init__(self, pInicial=Punto(), pFinal=Punto()):
        self.pInicial = pInicial
        self.pFinal = pFinal
 
        self.vBase = abs(self.pFinal.x - self.pInicial.x)
        self.vAltura = abs(self.pFinal.y - self.pInicial.y)
        self.vArea = self.vBase * self.vAltura
 
    def base(self):
        print("La base del rectángulo es {}".format( self.vBase ) )
 
    def altura(self):
        print("La altura del rectángulo es {}".format( self.vAltura ) )
 
    def area(self):
        print("El área del rectángulo es {}".format( self.vArea ) )
 
 