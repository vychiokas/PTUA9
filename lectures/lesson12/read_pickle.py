import pickle

with open("abc.pkl", "rb") as pickle_in:
    nauja_a = pickle.load(pickle_in)
    nauja_b = pickle.load(pickle_in)
    nauja_c = pickle.load(pickle_in)

print(nauja_a)
print(nauja_b)
print(nauja_c)

# 10
# 7
# 23