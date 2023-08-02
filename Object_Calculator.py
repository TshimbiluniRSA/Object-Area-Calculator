import math 

def Circle_Area(radius):
    return math.pi* radius * radius

def Square_Area(side):
    return side * side

def Rectangle_Area(length, width):
    return length * width

def Rhombus_Area(diagonal1, diagonal2):
    return (diagonal1 * diagonal2) / 2

def Trapezium_Area(base1, base2, height):
    return ((base1 + base2) * height) / 2

def Hexagon_Area(side):
    return (3 * math.sqrt(3) * side * side) / 2

def main():
    
    print("Welcome to the area calculator!")

    while True:
        print("\nSelect a shape:")
        print("1. Circle")
        print("2. Square")
        print("3. Rectangle")
        print("4. Rhombus")
        print("5. Trapezium")
        print("6. Hexagon")
        print("0. Exit")
        
        choice = input("Enter the number corresponding to your choice: ")

        if choice == "0":
            print("Exiting the application. Goodbye!")
            break
        elif choice == "1":
            radius = float(input("Enter the radius of the circle: "))
            area = Circle_Area(radius)
        elif choice == "2":
            side = float(input("Enter the side length of the square: "))
            area = Square_Area(side)   
        elif choice == "3":
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            area = Rectangle_Area(length, width)
        elif choice == "4":
            diagonal1 = float(input("Enter the first diagonal length of the rhombus: "))
            diagonal2 = float(input("Enter the second diagonal length of the rhombus: "))
            area = Rhombus_Area(diagonal1, diagonal2)
        elif choice == "5":
            base1 = float(input("Enter the length of the first base of the trapezium: "))
            base2 = float(input("Enter the length of the second base of the trapezium: "))
            height = float(input("Enter the height of the trapezium: "))
            area = Trapezium_Area(base1, base2, height)
        elif choice == "6":
            side = float(input("Enter the side length of the hexagon: "))
            area = Hexagon_Area(side)
        else:
            print("Invalid choice. Please select a valid option.")
            continue

        print(f"The area of the selected shape is: {area:.2f}")

if __name__ == "__main__":
    main()




