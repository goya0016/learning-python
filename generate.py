import random

#chooses a random option from the list
coin = random.choice(['heads','tails'])
# print (coin)

#chooses random number between the provided range
number = random.randint(1,10)
# print(number)

cards = ['spades','hearts','clubs','diamond']
#suffles the order of the entries in list
random.shuffle(cards)

for card in cards:
    print(card)




