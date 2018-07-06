# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

# Encoding categorical data
# Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 3] = labelencoder_X.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()

# Avoiding the Dummy Variable Trap
X = X[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

# Building the optional model using Backward Elimination
# =============================================================================
# import statsmodels.formula.api as sm
# X = np.append(arr=np.ones((50, 1)).astype(int), values=X, axis=1)
# X_opt = X[:, [0,1,2,3,4,5]]
# regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
# regressor_OLS.summary()
# 
# 
# X_opt = X[:, [0,1,3,4,5]]
# regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
# regressor_OLS.summary()
# 
# X_opt = X[:, [0,3,5]]
# regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
# regressor_OLS.summary()
# 
# X_opt = X[:, [0,3]]
# regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
# regressor_OLS.summary()
# =============================================================================

# Automating the optional model using Backward Elimination
import statsmodels.formula.api as sm
def backward_elimination(x, sl):
    num_vars = len(x[0])
    for i in range(0, num_vars):
        regressor_OLS = sm.OLS(y, x).fit()
        max_var = max(regressor_OLS.pvalues).astype(float)
        if max_var > sl:
            for j in range(0, num_vars - i):
                if (regressor_OLS.pvalues[j].astype(float) == max_var):
                    x = np.delete(x, j, 1)
    regressor_OLS.summary()
    return x


SL = 0.05
X_opt = X[:, [0,1,2,3,4,5]]
X_Modeled = backward_elimination(X_opt, SL)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        