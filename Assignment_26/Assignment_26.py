"""
Play predictor using KNN Algiorithm
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def MarvelousPlayPredictor():
    dataframe = pd.read_csv("PlayPredictor.csv")
    print("Dataset loaded succesfully")
    print("Dimention of dataset is : ",dataframe.shape)


    df = pd.DataFrame(dataframe)

    print("Dataset before encoding is : ")
    print(df)

    le_weather = LabelEncoder()
    le_temp = LabelEncoder()

    df["Wether"] = le_weather.fit_transform(df["Wether"])
    df["Temperature"] = le_temp.fit_transform(df["Temperature"])

    df["Play"] = df["Play"].map({'Yes' : 1, 'No' : 0})

    print("dataset after Label Encoding is : ")
    print(df)

    X = df.drop("Play", axis='columns')
    Y = df["Play"]



    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X, Y)

    print("\nTest Data : ")

    Wether = input("Enter wether(Sunny/Rainy/Overcast) : ")
    Temperature = input("Enter Temperature (Hot / Mild / Cool) : ")

    

    
    W = le_weather.transform([Wether])[0]
    T = le_temp.transform([Temperature])[0]

    test_sample = [[W, T]]
    predicted = model.predict(test_sample)[0]

    print("\nPrediction: Play? : ", "Yes" if predicted == 1 else "No")

    #Accuracy
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.5, random_state = 42)

    
    for K in range(1, 6, 2):   # K = 1,3,5,7
        model = KNeighborsClassifier(n_neighbors=K)
        model.fit(X_train, Y_train)
        pred = model.predict(X_test)
        acc = accuracy_score(Y_test, pred)

        print(f"Accuracy for K = {K} : {acc * 100:.2f}%")




def main():
    MarvelousPlayPredictor()
    

if __name__ == "__main__":
    main()