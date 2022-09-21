

import Punto
import Rectangulo

if __name__ == '__main__':
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
