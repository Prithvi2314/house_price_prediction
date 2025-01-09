from preprocess import preprocess_data
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

def train_and_save_model(data_path, model_path):
    #preprocess data
    X, y = preprocess_data(data_path)
    print("preprocessing completed!")

    #split the dtaaset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)
    print("Data Split into Training and Testing sets!")

    #train the model
    model = LinearRegression()
    model.fit(X_train, y_train)
    print("Model Training completed!")

    # save the trained model to the specified path
    with open(model_path , 'wb') as f:
        pickle.dump(model, f)
    print(f"Model saved to {model_path}!")

    #evaluate the model 
    score = model.score(X_test , y_test)
    print(f"Model R^2 score: {score:.2f}")

if __name__ == "__main__":
    #define the paths
    data_path = 'data/housing.csv'
    model_path = 'model/house_price_model.pkl'

    #train and save the model
    train_and_save_model(data_path, model_path)