# Elliptic-Curve
Discrete Elliptic Curve Over a Finite Field

The EllipticCurve.py works with Field.py to assign prime field elements to a elliptic curve point.

Example:

```python
#import required libraries
import Field
import EllipticCurve
```
```python
prime = 223
#define field elements
a = Field.Field(0, prime)
b = Field.Field(7, prime) 
x = Field.Field(47, prime)
y = Field.Field(71, prime)
```
```python
#Define point on curve
# a and b define the curve
# x and y define point on curve (a,b)
p = EllipticCurve.ECPoint(x,y,a,b)
```
```python
print(x)
"FieldElement_223(47)"
```
```python
#add field elements
print(x + y)
"FieldElement_223(118)"
```
```python
print(p)
"Point(FieldElement_223(47), FieldElement_223(71))_FieldElement_223(0)_FieldElement_223(7)"
```
```python
#add points on curve
print(p + p)
"Point(FieldElement_223(36), FieldElement_223(111))_FieldElement_223(0)_FieldElement_223(7)"
```
```python
#point multiplication
print((3 * p)) 
"Point(FieldElement_223(15), FieldElement_223(137))_FieldElement_223(0)_FieldElement_223(7)"
```
```python
print((3 * p) == (p + p + p))
True
```
