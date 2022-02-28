import random
class Dice:
    def roll(self):
        first_num = random.randint(1, 6)
        second_num = random.randint(1, 6)
        return first_num, second_num

dice1 = Dice()
print(dice1.roll())