import math

# Remember your math classes on 3D vectors?
#
# dot product of two 3D vector is simply the SUM of PRODUCT of respective components
#   (x1 * x2) + (y1 * y2) + (z1 * z2)
#
# Cross product is more complicated. Remember the covering row and column technique.
# Search google on how to do it.
#
# Absolute is just like pythagoras theorem.
#
# Anyway, this problem simply test your implementation skills on Classes and math module

class Points():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, other):
        return Points( other.x - self.x, other.y - self.y, other.z - self.z)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        x = Points.determinant( self.y, self.z, other.y, other.z )
        y = Points.determinant( self.x, self.z, other.x, other.z )
        z = Points.determinant( self.x, self.y, other.x, other.y )
        return Points(x,y,z)

    def absolute(self):
        return  (self.x ** 2 + self.y ** 2 + self.z ** 2 ) ** 0.5

    @staticmethod
    def determinant(a, b, c, d):
        return a*d - b*c


if __name__ == '__main__':
    points = [ [ map(int, input().split() ) ] for i in range(4) ]
    A, B, C, D = [ Points(*p) for p in points ]

    X = (B - A).cross(C - B)
    Y = (C - B).cross(D - C)

    cosPhi = X.dot(Y) / ( X.absolute() * Y.absolute() )
    print( f'{math.degrees( math.acos(phi) ):.2f}' )

