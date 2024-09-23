
import math
# Prompt the user to enter a radius; the user may enter a number with decimals (double).
# Display an error if the user enters invalid data and asks the user again for a radius.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_diameter(self):
        return self.radius * 2

    def calculate_circumference(self):
        return 2 * math.pi * self.radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

    def grow(self):
        self.radius *= 2

    def get_radius(self):
        return self.radius


def get_radius_from_user():
    while True:
        try:
            radius = float(input("Enter the radius of the circle: "))
            if radius < 0:
                print("Radius cannot be negative. Please enter a valid radius.")
                continue
            return radius
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    radius = get_radius_from_user()
    circle = Circle(radius)

    while True:
        print(f"\nDiameter: {circle.calculate_diameter():.2f}")
        print(f"Circumference: {circle.calculate_circumference():.2f}")
        print(f"Area: {circle.calculate_area():.2f}")

        grow_response = input("Should the circle grow? (yes/no): ").strip().lower()
        if grow_response == 'yes':
            circle.grow()
        elif grow_response == 'no':
            print(f"Goodbye! The final radius of the circle is: {circle.get_radius():.2f}")
            break
        else:
            print("Invalid response. Please answer 'yes' or 'no'.")

if __name__ == "__main__":
    main()
