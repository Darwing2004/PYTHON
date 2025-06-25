# Write code below 💖


class Restaurant:
    name = ""
    category = ""
    rating = 0.0
    delivery = False


bobs_burgers = Restaurant()
bobs_burgers.name = "Bob's Burgers"
bobs_burgers.category = "American Diner"
bobs_burgers.rating = 4.7
bobs_burgers.delivery = False

Dada_Diner = Restaurant()
Dada_Diner.name = "Dada's Diner"
Dada_Diner.category = "American Diner"
Dada_Diner.rating = 4.9
Dada_Diner.delivery = True

Kevin_Wok = Restaurant()
Kevin_Wok.name = "Kevin's Wok"
Kevin_Wok.category = "Chineese Wok"
Kevin_Wok.rating = 4.6
Kevin_Wok.delivery = True

print(vars(bobs_burgers))
print(vars(Dada_Diner))
print(vars(Kevin_Wok))
