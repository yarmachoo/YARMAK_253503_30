import pickle

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import Task4.Triangle as Triangle

def get_float_input(text):
    while True:
        try:
            value = float(input(text))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_angle_input(text):
    while True:
        try:
            value = float(input(text))
            if 0 < value < 180:
                return value
            else:
                print("Angle must be between 0 and 180 degrees.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def general_func():
    print("=== Triangle Builder ===")
    base = get_float_input("Enter the base of the triangle: ")
    height = get_float_input("Enter the height of the triangle: ")
    angle = get_angle_input("Enter the angle at the vertex (in degrees): ")
    color = input("Enter the color of the triangle: ")

    triangle = Triangle.Triangle(base, height, angle, color)
    area = triangle.calculate_area()
    label = input("Input label: ")
    #label = f"{triangle.get_description()} colored in {color}"

    print("\nTriangle Details:")
    print(triangle)
    print("Area of the triangle:", area)

    fig, ax = plt.subplots()
    ax.set_xlim([0, max(base, height) * 1.2])
    ax.set_ylim([0, max(base, height) * 1.2])

    triangle_coords = [(0, 0), (base, 0), (base / 2, height * 0.866)]  # Triangle coordinates
    polygon = Polygon(triangle_coords, facecolor=color, edgecolor='black')
    ax.add_patch(polygon)

    plt.text(base / 2, height * 0.866 + 0.1, label, ha='center')
    plt.title("Triangle")
    plt.xlabel("Base")
    plt.ylabel("Height")
    plt.grid(True)

    plt.savefig("graph.png")

    plt.show()
