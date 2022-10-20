# -*- coding: utf-8 -*-
"""
NOTE THIS PROGRAM IS MEANT TO RUN WITH FINITE FIELDS
Elliptic curves are of the form y^2 = x^3 + a*x + b
This class is designed to find points on a particular elliptic curve
coefficients a & b are what defines the curve, while x & y are points on the curve
Note: This is for a discrete(finite # of points), not a continuous curve.
"""

#Impoting Field Module
import Field

class ECPoint:
    
    #checking and initializing points (x, y) on curbe (a, b)
    def __init__(self: object, x : int, y : int, a : int, b : int):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        if (self.x is None) and (self.y is None):
            return
        if self.y**2 != self.x**3 + a * self.x + b:
            raise ValueError("Point ({}, {}) is not on the elliptic curve\n\ty^3 = x^2 + {}*x + {}".format(x,y,a,b))

        
    def __repr__(self : object) -> str:
        return 'Point({}, {})_{}_{}'.format(self.x, self.y, self.a, self.b)
    
    #Redefining '==' so if values are equal it will return True regardless of memory location    
    def __eq__(self : object, other : object) -> bool:
        if (self.x == other.x) and (self.y == other.y) and (self.a == other.a) and (self.b == other.b):
            return True
        return False
    
    #inverse of '=='
    def __ne__(self : object, other : object) -> bool:
        return not (self == other)
    
    #Adding 2 points
    def __add__(self : object, other : object) -> str:
        if (self.a != other.a) or (self.b != other.b):
            raise ValueError('{} and {} are not on the same curve'.format(self, other))
        
        #For infinite points
        if self.x is None:
            return other
        if other.x is None:
            return self
        
        #case 1
        #Equation of line containing these points is vertical (point of infinite)
        if (self.x == other.x) and (self.y != other.y):
            return self.__class__(None, None, self.a, self.b)
        
        #case 2
        #if self.x != other.x
        if self.x != other.x:
            s = (other.y - self.y) / (other.x - self.x)
            x = s**2 - self.x - other.x
            y = s * (self.x - x) - self.y
            return self.__class__(x, y, self.a, self.b)
        
        #case 3
        #If points are equal, then the line containing is tangent to curve
        if (self == other) and (self.y == 0 * self.x):
            return self.__class__(None, None, self.a, self.b)
            
        if (self == other):
            s = (3 * (self.x ** 2) + self.a) / (2 * self.y)
            x = (s ** 2) - 2 * self.x
            y = s * (self.x - x) - self.y
            return self.__class__(x, y, self.a, self.b)
    
    #Multiplying point (i.e adding point to itself 'n' times)
    def __rmul__(self, coef):
        current = self
        #Initializing infinite point
        result = self.__class__(None, None, self.a, self.b)
        #While coef > 0
        while coef:
            #if (coef == 0) & true the false
            if coef & 1:
                result += current
            current += current
            #bit shift
            coef >>= 1  
        return result


#Initial points to mess around with
##Practice points for p = 223 on curve defined (a,b) = (0,7)
##  (x,y) = (47,71) and n = 21
##  (x,y) = (170, 142) and n = 42
if __name__ == "__main__":
    import matplotlib.pyplot as plt
    #prime field
    prime = 223
    #defining field elements fo elliptic curve coefficiants
    a = Field.Field(0, prime)
    b = Field.Field(7, prime)
    #defining field elements for elliptic curve point
    x = Field.Field(47, prime)
    y = Field.Field(71, prime)
    #point on the curve
    p = ECPoint(x,y,a,b)
    #X Y coordinates for plotting
    X = []
    Y = []
    #size of field for generator point (x,y) on curve (a,b)
    n = 21
    for s in range(1, n):
        result = s*p
        X.append(result.x.x)
        Y.append(result.y.x)
        print("{}*(74,71)=({},{})".format(s, result.x.x,result.y.x))
    plt.scatter(X,Y)
    plt.show()


