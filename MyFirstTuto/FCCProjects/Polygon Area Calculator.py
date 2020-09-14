from __future__ import annotations

class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.height = height
        self.width = width

    def set_width(self, width: float) -> None:
        self.width = width

    def set_height(self, height: float) -> None:
        self.height = height

    def get_area(self) -> float:
        return self.width * self.height

    def get_perimeter(self) -> float:
        return self.height * 2 + self.width * 2

    def get_diagonal(self) -> float:
        return (self.height ** 2 + self.width ** 2 ) ** .5

    #   Every row is created using List Comprehension, then use join() to join them using \n. Lastly it requires a
    #   newline at last row as well so add that
    def get_picture(self) -> str:
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        return '\n'.join( [ '*' * self.width for i in range(self.height) ] ) + '\n'

    #   Just see how many of child fit inside parent vertically and horizontally, then multiply them together
    #   It is assumed no rotations are included
    def get_amount_inside(self, polygon: Rectangle) -> int:
        fitHeight = self.height // polygon.height
        fitWidth = self.width // polygon.width
        return fitHeight * fitWidth

    #   Use instance.__class__.__name__ to get the class name
    def __str__(self):
        return '{}(width={}, height={})'.format( self.__class__.__name__, self.width, self.height )


class Square(Rectangle):
    def __init__(self, side: float) -> None:
        super().__init__(side, side)

    def set_side(self, side: float) -> None:
        self.height = side
        self.width = side

    def set_width(self, side: float) -> None:
        self.set_side(side)
    def set_height(self, side: float) -> None:
        self.set_side(side)

    def __str__(self) -> str:
        return '{}(side={})'.format( self.__class__.__name__, self.width )
