import pickle

dict1 = {'a': 100,
         'b': 200,
         'c': 300}

list1 = [400,
         500,
         600]

print(dict1)
print(list1)

output = open("save1.pkl", 'wb')

pickle.dump(dict1, output, pickle.HIGHEST_PROTOCOL)
pickle.dump(list1, output, pickle.HIGHEST_PROTOCOL)

output.close()
print("---------------------")

input_file = open("save1.pkl", 'rb')

dict2 = pickle.load(input_file)
list2 = pickle.load(input_file)

print(dict2)
print(list2)