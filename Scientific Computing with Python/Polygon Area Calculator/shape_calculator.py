class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Set new width
    def set_width(self, width):
        self.width = width

    # Set new height
    def set_height(self, height):
        self.height = height

    # Return Area
    def get_area(self):
        return self.width * self.height

    # Return Perimeter
    def get_perimeter(self):
        return 2 * (self.width + self.height)

    # Return Diagonal
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    # Return Shape/Picture
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        shape = ''
        for i in range(self.height):
            shape += '*' * self.width + '\n'

        return shape

    # Number of times the passed in shape could fit inside the shape
    def get_amount_inside(self, shape):
        '''
        Returns the number of times the passed in shape could fit inside the shape (with no rotations)
        '''
        return self.get_area() // shape.get_area()

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'



class Square(Rectangle):
    def __init__(self, side):
        Rectangle.__init__(self, side, side)
        
    # Renew sides
    def set_side(self, side):
        self.width = side
        self.height = side

    # Renew sides
    def set_width(self, width):
        self.width = width
        self.height = width

    # Renew sides
    def set_height(self, height):
        self.height = height
        self.width = height

    def __str__(self):
        return f'Square(side={self.width})'
