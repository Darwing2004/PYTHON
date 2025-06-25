# Write code below 💖


def welcome():
    while True:
        print("WELCOME TO MCDONALD")
        print("1) Cheeseburger")
        print("2) Fries")
        print("3) Soda")
        print("4) Ice Cream")
        print("5) Cookie")
        print("6) Quit")

        choice = int(input("Your choice : "))

        if choice == 6:
            print("GoodBye !")
            break

        if choice > 6:
            print("Wrong Answer !")

        return choice


def get_item(choice):
    if choice == 1:
        print("Your order a Cheeseburger !")
    elif choice == 2:
        print("You order some Fries !")
    elif choice == 3:
        print("You order a Soda !")
    elif choice == 4:
        print("You order a Ice cream !")
    elif choice == 5:
        print("You order a Cookie !")
    else:
        print("This item doen't existe...")


choice = welcome()
get_item(choice)
