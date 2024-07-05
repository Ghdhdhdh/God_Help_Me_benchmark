import importlib
import os
from benchmarks import fibonacci, Sieve_of_Eratosthenes
from decimal import Decimal, getcontext
getcontext().prec = 10


modules = [fibonacci, Sieve_of_Eratosthenes]

def sum(li:list):
    final = 0
    for num in li:
        final += num
    return final
score = {}
for module in modules:
    scores = []
    for i in range(200):
        scores.append(module.benchmark())
    score[module.__name__] = (sum(scores) / len(scores))

final_score = 1

for key, value in score.items():
    final_score *= value

print(f"Your final score is {round(final_score*100000000, 1)}")

for key, value in score.items():
    print(f"You scored {value} in {key}")