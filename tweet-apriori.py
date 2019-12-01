import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori

# importing data file
tweet_data = pd.read_csv("/Users/tonili/Desktop/446 - Tweet Data.csv", header=None)
# getting sample of data
print(tweet_data.head())

# data pre-processing
records = []
for i in range(0, 468):
    records.append([str(tweet_data.values[i, j]) for j in range(0, 9)])

# association rules
association_rules = apriori(records, min_support=0.001, min_confidence=0.7, min_lift=2, min_length=2)
association_results = list(association_rules)

# viewing results
#print(len(association_results))
#print(association_results[0])

for x in range(32):
    print(association_results[x])

# for item in association_results:
#     # first index of the inner list
#     # Contains base item and add item
#     pair = item[0]
#     items = [x for x in pair]
#     print("Rule: " + items[0] + " -> " + items[1])
#
#     # second index of the inner list
#     print("Support: " + str(item[1]))
#
#     # third index of the list located at 0th
#     # of the third index of the inner list
#
#     print("Confidence: " + str(item[2][0][2]))
#     print("Lift: " + str(item[2][0][3]))
#     print("=====================================")
