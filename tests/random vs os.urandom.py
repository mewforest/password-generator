import random

random.seed(1)
print(random.randint(1, 50))
# print(random.choice('abcdef12345'))

rnd = random.SystemRandom()
print(rnd.randint(1, 50))




