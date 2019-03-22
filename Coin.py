# Define your Coin class here
import random


class Coin:

    def __init__(self):
        self.face = random.choice(["heads", "tails"])

    def get_face(self):
        return self.face

    def flip(self):
        self.face = random.choice(["heads", "tails"])


if __name__ == '__main__':
    coin_test = Coin()

    heads = 0
    tails = 0

    for i in range(1, 1000):
        coin_test.flip()

        if coin_test.face == "heads":
            heads = heads + 1
        else:
            tails = tails + 1

    pass
