# Write code below 💖


def welcome():

    print("WELCOME TO MCDONALD")
    print("1) Cheeseburger")
    print("2) Fries")
    print("3) Soda")
    print("4) Ice Cream")
    print("5) Cookie")


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


welcome()

option = int(input("What would you like to order ? : "))
get_item(option)
