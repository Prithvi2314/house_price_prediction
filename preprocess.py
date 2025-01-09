import pandas as pd

def preprocess_data(filepath):
    # load the dataset
    data = pd.read_csv(filepath)
    print("Dataset Loaded successfully!")
    print(data.head()) # debugging :display the first 5 rows of the dataset 


    #keep relevent features for simplicity
    features = ['area' , 'bedrooms', 'bathrooms', 'stories' , 'mainroad', 'guestroom', 'basement',
                'hotwaterheating', 'airconditioning', 'parking' , 'prefarea']
    target = 'price'


    #convert categorial features to numerical
    for col in ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea']:
        data[col] = data[col].map({'yes':1, 'no':0})

    #feature and target
    X = data[features]
    y = data[target]

    return X, y

if __name__ == "__main__":
    #test the preprocessing function
    X, y = preprocess_data('data/housing.csv')
    print("Features (x):")
    print(X.head())
    print("\nTarget (y):")
    print(y.head())
