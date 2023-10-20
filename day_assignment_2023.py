import random

responsibles = ["Johan"] * 8 + ["Magnus"] * 8 + ["Max"] * 8
days = 24

random.seed(2023)

for day in range(1, days + 1):
    responsible = random.choice(responsibles)

    print("| " + str(day) + " | " + responsible + " | | | |")

    responsibles.remove(responsible)
