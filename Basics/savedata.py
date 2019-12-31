import pickle
from player import Player

items = ["axe", "sword", "gun"]

my_object = Player(1, "Jeff", 100.00, items)
print(my_object)

with open("save2.pkl", 'wb') as outfile:
    pickle.dump(my_object, outfile, pickle.HIGHEST_PROTOCOL)

print("---------------------")

new_object = None

with open("save2.pkl", 'rb') as infile:
    new_object = pickle.load(infile)

print(new_object)