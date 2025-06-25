# Write code below 💖
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print("Q1) Do you like Dawn or Dusk?")
print("1) Dawn")
print("2) Dusk")
answer = int(input("Answer :"))

if answer == 1:
    Gryffindor = Gryffindor + 1
    Ravenclaw = Ravenclaw + 1
elif answer == 2:
    Hufflepuff = Hufflepuff + 1
    Slytherin = Slytherin + 1
else:
    print("Wrong input.")

print("Q2) When I'm dead, I want people to remember me as:")
print("1) The God")
print("2) The Great")
print("The Wise")
print("The Bold")
answer2 = int(input("Answer : "))

if answer2 == 1:
    Hufflepuff = Hufflepuff + 2
elif answer2 == 2:
    Slytherin = Slytherin + 2
elif answer2 == 3:
    Ravenclaw = Ravenclaw + 2
elif answer2 == 4:
    Gryffindor = Gryffindor + 2
else:
    print("Wrong input.")

print("Q3) Which kind of instrument most pleases your ear?")
print("1) Violon")
print("2) The trumpet")
print("3) The piano")
print("4) The drum")
answer3 = int(input("Answer :"))

if answer3 == 1:
    Slytherin = Slytherin + 4
elif answer3 == 2:
    Hufflepuff = Hufflepuff + 4
elif answer3 == 3:
    Ravenclaw = Ravenclaw + 4
elif answer3 == 4:
    Gryffindor = Gryffindor + 4
else:
    print("Wrong input.")


print("Result :")
print(f"Gryffondor : {Gryffindor} point(s)")
print(f"Slytherin : {Slytherin} point(s)")
print(f"Hufflepuff : {Hufflepuff} point(s)")
print(f"Ravenclaw : {Ravenclaw} point(s)")
