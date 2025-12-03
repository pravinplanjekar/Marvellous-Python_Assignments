"""
Advertising agency sales  using classification Algiorithm
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def AdvertisementAgencyReport():
    Line = "*"*50

    dataframe = pd.read_csv("MarvellousAdvertising.csv")
    print("Dataset loaded succesfully")
    print("Dimention of dataset is : ",dataframe.shape)

    df = pd.DataFrame(dataframe)
    print(df.head())

    print("Clean the dataset")
    df.drop(columns = ['Unnamed: 0'] , inplace = True) 

    print(Line)
    print("First five records of updated dataset is : ")
    print(Line)
    print(df.head())
    print(Line)

    print("Statistical information of the dataset : ")
    print(Line)
    print(df.describe())
    print(Line)

    x = df[['TV', 'radio', 'newspaper']]
    y = df[['sales']]

    print("Independent variables are : TV, radio and newspaper ")
    print("Dependent variables are : sales")

    print("Total records in dataset : ",x.shape)

    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.5, random_state = 42)
    print("Dimensions of Training dataset : ",x_train.shape)
    print("Dimensions of Testing dataset : ",x_test.shape)
    
    model = LinearRegression()
    model.fit(x_train,y_train)

    y_pred = model.predict(x_test)

    print("\nExpected Sales :")
    print(y_test.values.flatten())

    print("\nPredicted Sales :")
    print(y_pred.flatten())

    '''
    mse = mean_squared_error(y_test,y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test,y_pred)

    print("Mean Squared Error is : ",mse)
    print("Root Mean Squared Error is : ",rmse)
    print("R Square Value : ",r2)
    '''


def main():
    AdvertisementAgencyReport()
    

if __name__ == "__main__":
    main()