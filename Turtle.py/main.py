import math
import turtle

# ============================
#   CALCULATION FUNCTIONS
# ============================

def area_rectangle(l, w):
    return l * w

def perimeter_rectangle(l, w):
    return 2 * (l + w)

def area_circle(r):
    return math.pi * r * r

def circumference(r):
    return 2 * math.pi * r

def area_triangle(b, h):
    return 0.5 * b * h

def perimeter_triangle(a, b, c):
    return a + b + c


# ============================
#   DRAWING FUNCTIONS
# ============================

def draw_rectangle(t, l, w):
    t.penup()
    t.goto(-l/2, -w/2)
    t.pendown()
    for _ in range(2):
        t.forward(l)
        t.left(90)
        t.forward(w)
        t.left(90)
    t.write("Rectangle", font=("Arial", 12, "bold"))

def draw_circle(t, r):
    t.penup()
    t.goto(0, -r)
    t.pendown()
    t.circle(r)
    t.penup()
    t.goto(0, r)
    t.write("Circle", font=("Arial", 12, "bold"))

def draw_triangle(t, side):
    t.penup()
    t.goto(-side/2, -side/2)
    t.pendown()
    for _ in range(3):
        t.forward(side)
        t.left(120)
    t.write("Triangle", font=("Arial", 12, "bold"))


# ============================
#          MENU LOOP
# ============================

def main():
    t = turtle.Turtle()
    t.speed(3)

    while True:
        print("\nGeometry Calculator")
        print("1. Rectangle")
        print("2. Circle")
        print("3. Triangle")
        print("4. Quit")

        choice = input("Choice: ")

        t.clear()

        if choice == "1":  # Rectangle
            l = float(input("Enter length: "))
            w = float(input("Enter width: "))

            a = area_rectangle(l, w)
            p = perimeter_rectangle(l, w)

            print("Area:", round(a, 2))
            print("Perimeter:", round(p, 2))

            draw_rectangle(t, l, w)

        elif choice == "2":  # Circle
            r = float(input("Enter radius: "))

            a = area_circle(r)
            c = circumference(r)

            print("Area:", round(a, 2))
            print("Circumference:", round(c, 2))

            draw_circle(t, r)

        elif choice == "3":  # Triangle (equilateral for drawing)
            side = float(input("Enter side length: "))
            height = (math.sqrt(3) / 2) * side

            a = area_triangle(side, height)
            p = perimeter_triangle(side, side, side)

            print("Area:", round(a, 2))
            print("Perimeter:", round(p, 2))

            draw_triangle(t, side)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

    turtle.done()


# RUN PROGRAM
main()
