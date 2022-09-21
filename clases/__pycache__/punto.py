from math import sqrt
import math

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
        
        # otra forma es ponerlo de la siguiente forma: return"("+str(self.x)+","+str(self.y)+")"
    
    
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
        d = math.sqrt ( (p.x - self.x)**2 + (p.y - self.y)**2 )
        print("La distancia entre los puntos {} y {} es {}".format(self, p, d))
 


 
