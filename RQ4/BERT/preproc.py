import pandas as pd
test = pd.read_csv("refactored_test.csv")
train = pd.read_csv("refactored_train.csv")
print("test")
print(test.head())
print(len(test.index))
print("train")
print(train.head())
print(len(train.index))
