import pandas as pd
import numpy as np
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression


columns = ['tweet','military','healthcare','immigration','climate','gun control', 'economy','taxes',
                           'education','foreign policy','Normalized Polarity']


data_set = pd.read_csv('/Users/tanushrees/Documents/School/3B/MSCI446/input.csv')

#print(data_set.describe())

# Assign data from first 8 columns to X variable, dont include tweet
X = data_set.iloc[0:476, 1:10]

# Assign data from last column to y variable
y = data_set.iloc[0:476, 10]

# convert data frame to array
X_array = X.values
y_array = y.values

# set up kfold parameters, k=10
kf = KFold(n_splits=10,random_state=42 ,shuffle=True)


regressor = LinearRegression()

error = []
intercept = []
coef = []
score = []


# cross validation, add results to arrays
for train_index, test_index in kf.split(X_array):

    X_train, X_test = X_array[train_index], X_array[test_index]
    y_train, y_test = y_array[train_index], y_array[test_index]

    # train the model on each fold
    regressor.fit(X_train, y_train)
    error.append(regressor.score(X_test, y_test))
    score.append(regressor.score(X_test, y_test))
    intercept.append(regressor.intercept_)
    coef.append(regressor.coef_)


# error, interceot and coefficient values are the average of each of the k folds
avg_error = np.mean(error)
avg_intercept = np.mean(intercept)
avg_score = np.mean(score)

sum_coef = [0,0,0,0,0,0,0,0,0]
# calculate the average coefficient for each feature
for i in coef:
    for j in range(9):
        if j == 0:
            sum_coef[j] = sum_coef[j] + i[j]
        elif j == 1:
            sum_coef[j] = sum_coef[j] + i[j]
        elif j == 2:
            sum_coef[j] = sum_coef[j] + i[j]
        elif j == 3:
            sum_coef[j] = sum_coef[j] + i[j]
        elif j == 4:
            sum_coef[j] = sum_coef[j] + i[j]
        elif j == 5:
            sum_coef[j] = sum_coef[j] + i[j]
        elif j == 6:
            sum_coef[j] = sum_coef[j] + i[j]
        elif j == 7:
            sum_coef[j] = sum_coef[j] + i[j]
        elif j == 8:
            sum_coef[j] = sum_coef[j] + i[j]

# average of the coefficients
avg_coef = [x / 10 for x in sum_coef]

print (avg_intercept)
print (avg_coef)