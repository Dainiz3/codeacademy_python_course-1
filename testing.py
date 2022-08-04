import random

sample = [1, 2, 3, None]

def get_random_from_sample(sample):
    return random.choice(sample)

print(get_random_from_sample(sample))
while get_random_from_sample(sample):
    print("did not get None")