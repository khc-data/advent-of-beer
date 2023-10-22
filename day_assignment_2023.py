import random

responsibles = ["Johan"] * 7 + ["Magnus"] * 7 + ["Max"] * 7
days = len(responsibles)

random.seed(2023)

print("| Day | Responsible | Beer | Untappd score | Ratebeer score |")
print("| --- | --- | --- | --- | --- |")

for day in range(1, days + 1):
    responsible = random.choice(responsibles)

    print("| " + str(day) + " | " + responsible + " | | | |")

    responsibles.remove(responsible)

print("| " + str(22) + " | Johan | | | |")
print("| " + str(23) + " | Magnus | | | |")
print("| " + str(24) + " | Max | | | |")