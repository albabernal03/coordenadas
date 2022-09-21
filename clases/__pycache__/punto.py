from math import sqrt

#para comprobar que los valores introducidos son numericos
def es_numero(valor):
    return isinstance(valor, (int,float))

class Punto():
  
    def __init__(self,x=0,y=0):
        if es_numero(x) and es_numero(y):
            self.x=x
            self.y=y
        else:
            raise TypeError('x e y deben ser valores numéricos')

    def __str__(self): #convertimos para que tenga el siguiente formato
        return "({},{})".format(self.x,self.y)
        #return"("+str(self.x)+","+str(self.y)+")"
        #otra opcion es ponerlo de la siguiente forma "({},{})".format(self.x,self.y)
    
    def cuadrante(self):
        if self.x > 0 and self.y> 0:
            print('{} pertenece al primer cuadrante'.format(self))
        elif self.x < 0 and self.y > 0:
             print('{} pertenece al segundo cuadrante'.format(self))
        elif self.x < 0 and self.y < 0:
             print('{} pertenece al tercer cuadrante'.format(self))
        elif self.x > 0 and self.y < 0:
            print('{} pertenece al cuarto cuadrante'.format(self))

    def vector(self,p):
        print("El vector entre {} y {} es ({}, {})".format(self, p, p.x - self.x, p.y - self.y) )
    
    def distancia(self, p):
        d = math.sqrt ( (p.coordenada_X - self.coordenada_X)**2 + (p.coordenada_Y - self.coordenada_Y)**2 )
        print("La distancia entre los puntos {} y {} es {}".format(self, p, d))
 
class Rectangulo:
    def __init__(self, pInicial=Punto(), pFinal=Punto()):
        self.pInicial = pInicial
        self.pFinal = pFinal
 
    def base(self):
        print("La base del rectángulo es {}".format( self.vBase ) )
 
    def altura(self):
        print("La altura del rectángulo es {}".format( self.vAltura ) )
 
    def area(self):
        print("El área del rectángulo es {}".format( self.vArea ) )
 
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
 
 
 
A = Punto(2,3)
B = Punto(5,5)
C = Punto(-3, -1)
D = Punto(0,0)
 
A.cuadrante()
C.cuadrante()
D.cuadrante()
 
A.vector(B)
B.vector(A)
 
 
 
A.distancia(B)
B.distancia(A)
 
A.distancia(D)
B.distancia(D)
C.distancia(D)
 
R = Rectangulo(A, B)
R.base()
R.altura()
R.area()