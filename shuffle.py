import random
from traceback import print_exception
SUIT = ["H","C","S","D"]
RANK = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
stock_deck = [(r + s) for s in SUIT for r in RANK]
stock_deck.extend(stock_deck)
random.shuffle(stock_deck)
print("Playing 10 Cards")
for i in range(10):
	print(stock_deck[i][0], "of", stock_deck[i][1])
	