# Elliptic-Curve
Discrete Elliptic Curve Over a Finite Field

The EllipticCurve.py works with Field.py to assign prime field elements to a elliptic curve point.

Example:

import Field
import EllipticCurve
prime = 223

a = Field.Field(0, prime)
b = Field.Field(7, prime)
x = Field.Field(47, prime)
y = Field.Field(71, prime)
p = EllipticCurve.ECPoint(x,y,a,b)

print(x)
"FieldElement_223(47)"

print(x + y)
"FieldElement_223(118)"

print(p)
"Point(FieldElement_223(47), FieldElement_223(71))_FieldElement_223(0)_FieldElement_223(7)"

print(p + p)
"Point(FieldElement_223(36), FieldElement_223(111))_FieldElement_223(0)_FieldElement_223(7)"

print((3 * p)) 
"Point(FieldElement_223(15), FieldElement_223(137))_FieldElement_223(0)_FieldElement_223(7)"

print((3 * p) == (p + p + p))
True
