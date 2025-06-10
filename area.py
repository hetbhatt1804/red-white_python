def outer_rectangle_area(length, width):
    rectangle_area = length * width
    print(f"Area of rectangle: {rectangle_area}")

    def inner_square_area(side):
        square_area = side * side
        print(f"Area of square: {square_area}")

    inner_square_area(min(length, width))

outer_rectangle_area(10, 5)
