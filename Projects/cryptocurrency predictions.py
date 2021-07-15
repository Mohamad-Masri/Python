import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#import matplotlib


df = pd.read_csv('ETH.csv')

projection = 14

df['Prediction'] = df[['Close']].shift(-projection)

#print(df.head(5))
print(df)
