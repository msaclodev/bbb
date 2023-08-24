def calculate_rectangle_area(length, width):
    area = length * width
    return area

try:
    # Taking user input for length and width
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    # Calculating the area
    area = calculate_rectangle_area(length, width)

    # Displaying the result
    print("The area of the rectangle is:", area)
except ValueError:
    print("Invalid input. Please enter valid numeric values for length and width.")
