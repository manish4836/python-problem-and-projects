import random

def dice_roll(num_rolls):
    result = []
    for _ in range(num_rolls):
        roll = random.randint(1,6)
        result.append(roll)
    return tuple(result)
print(dice_roll(6))