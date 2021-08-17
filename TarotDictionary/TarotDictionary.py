import numpy as np

tarot = { 1: "The Magician", 2:	"The High Priestess", 3: "The Empress", 4: "The Emperor", 5: "The Hierophant", 6: "The Lovers", 7: "The Chariot", 8: "Strength", 9:	"The Hermit", 10: "Wheel of Fortune", 11: "Justice", 12: "The Hanged Man", 13: "Death", 14:	"Temperance", 15: "The Devil", 16: "The Tower", 17:	"The Star", 18: "The Moon", 19: "The Sun", 20: "Judgement", 21: "The World", 22: "The Fool"}

spread = {}

# following loop updates the available card list each turn
# and creates needed dictionary entries, while removing used cards
for each in ['past', 'present', 'future']:
    cards_left = list(tarot.keys())

    # numpy.random.choice() will be the most suitable option to choose the card. It takes a list of numbers and returns a random choice from that list.
    spread[each] = tarot.pop(np.random.choice(cards_left))

for key, value in spread.items():
    print("Your {} is the {} card.".format(key, value))