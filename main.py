import importlib
import os
from benchmarks import fibonacci, Sieve_of_Eratosthenes
from decimal import Decimal, getcontext
getcontext().prec = 10


modules = [fibonacci, Sieve_of_Eratosthenes]


score = {}
for module in modules:
    score[module.__name__] = module.benchmark()

final_score = 1

for key, value in score.items():
    final_score *= value

print(f"Your final score is {final_score}")

for key, value in score.items():
    print(f"You scored {value:.1000000f} in {key}")