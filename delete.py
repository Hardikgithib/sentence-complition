import pickle

with open('vocab.pkl', 'rb') as f:
    x = pickle.load(f)

print(x)