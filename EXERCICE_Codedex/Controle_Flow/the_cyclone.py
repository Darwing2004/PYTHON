# Write code below 💖

height = int(input("What's your height ? : "))
credits = int(input("How many credits do you have ? : "))

if height > 137 and credits > 10:
    print("Enjoy the ride!")
elif height < 137 and credits > 10:
    print("You are not tall enough.")
elif height > 137 and credits < 10:
    print("You don't have enough credits.")
else:
    print("You are not tall enough and you don't have enough credits.")
