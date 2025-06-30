import random


def play(playing):
    while playing == True:
        symboles = ["🍒", "🍇", "🍉", "7️⃣ "]

        result = random.choices(symboles, k=3)

        print(" | ".join(result))

        tout_est_7 = True

        for symbole in result:
            if symbole != "7️⃣":
                tout_est_7 = False
                break

        if tout_est_7:
            print("Jackpot! 💰")
        else:
            print("Thanks for playing!")

        choice = input("Do you want to play again ? (Y for Yes | N for No) : ")

        if choice == "N":
            playing = False


playing = True

play(playing)
