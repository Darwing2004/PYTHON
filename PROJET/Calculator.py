from math import *

while True:
    print("==================")
    print("Area Calculator 📐")
    print("==================")

    print("1) Triangle")
    print("2) Rectangle")
    print("3) Square")
    print("4) Circle")
    print("5) Quit")

    choice = int(input("\nWhich shape: "))

    if choice == 1:
        base = float(input("\nBase: "))
        height = float(input("Height: "))
        area = (height * base) / 2

        print(f"\nThe area is {area}\n")

    elif choice == 2:
        print("\n")
        width = float(input("\nWidth : "))
        length = float(input("Lenght: "))
        area = width * length

        print(f"\nThe area is {area}\n")

    elif choice == 3:
        print("\n")
        side = float(input("\nSide: "))
        area = side**2

        print(f"\nThe area is {area}\n")

    elif choice == 4:
        print("\n")
        radius = float(input("\nRadius: "))
        area = pi * radius**2

        print(f"\nThe area is {area}\n")

    elif choice == 5:
        print("\nGoodBye !")
        break

    else:
        print("Wrong number. Please try again.\n")
