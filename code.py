import random

def odd_at_least_once():
    for i in range(3):
        if random.randint(1, 6) % 2 == 1:
            return True
    return False

num_trials = 1000000
num_successes = 0

for i in range(num_trials):
    if odd_at_least_once():
        num_successes += 1

print("Probability of getting odd at least once:", num_successes/num_trials)
