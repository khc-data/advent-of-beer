import random
from datetime import date

year = 2023

responsibles = ["Johan"] * 7 + ["Magnus"] * 7 + ["Max"] * 7
days = len(responsibles)

random.seed(2023)

print("| Day | Responsible | Beer | Magnus score | Max score | Johan score | Untappd score | Ratebeer score |")
print("| --- | --- | --- | --- | --- | --- | --- | --- |")

for day in range(1, days + 1):
    responsible = random.choice(responsibles)

    print("| " + str(day) + " (" + date(year, 12, day).strftime("%a") + ") | " + responsible + " | <!--- Beer --> | <!--- Magnus score --> | <!--- Max score --> | <!--- Johan score --> | <!--- Untappd --> | <!--- Ratebeer --> |")

    responsibles.remove(responsible)

print("| 24 (" + date(year, 12, 24).strftime("%a") + ") | Johan | <!--- Beer --> | <!--- Magnus score --> | <!--- Max score --> | <!--- Johan score --> | <!--- Untappd --> | <!--- Ratebeer --> |")
print("| 24 (" + date(year, 12, 24).strftime("%a") + ") | Magnus | <!--- Beer --> | <!--- Magnus score --> | <!--- Max score --> | <!--- Johan score --> | <!--- Untappd --> | <!--- Ratebeer --> |")
print("| 24 (" + date(year, 12, 24).strftime("%a") + ") | Max | <!--- Beer --> | <!--- Magnus score --> | <!--- Max score --> | <!--- Johan score --> | <!--- Untappd --> | <!--- Ratebeer --> |")