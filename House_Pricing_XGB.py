# Imports
import pandas as pd
import numpy as np
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
import warnings

warnings.filterwarnings('ignore')

df = pd.read_csv("C:\\Users\\bavsr\\Downloads\\house-prices-advanced-regression-techniques\\train.csv")
test = pd.read_csv("C:\\Users\\bavsr\\Downloads\\house-prices-advanced-regression-techniques\\test.csv")

# Exploantary Analysis
df.shape
df.head()
df.info()
df.describe()

# Function to check for NaN values and clean DataFrame
def check_NA(
            data,
):
    df = data.copy()
    for col in df.columns:
        if df[col].isnull().sum() > 0:
            print('{} had {} null values'.format(col, df[col].isnull().sum()))
    for i in df:
        print("Cleaned df is given below")
        df = df.dropna(axis=1, how="any", thresh=None, subset=None, inplace=False)
        return df

df_work = check_NA(df)
df_work.isnull().values.any()  # Returns False therefore, there are no NaN values in our dataset
