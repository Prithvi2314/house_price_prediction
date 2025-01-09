from flask import Flask, render_template , request
import pickle
import pandas as pd 

app = Flask(__name__)

#load the trained model
model_path = 'model/house_price_model.pkl'
with open(model_path,'rb') as f:
    model = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict' , methods=['POST'])
def predict():
    if request.method == 'POST':
        #get form data
        form_data = request.form
        area = float(form_data['area'])
        bedrooms = int(form_data['bedrooms'])
        bathrooms = int(form_data['bathrooms'])
        stories = int(form_data['stories'])
        mainroad = 1 if form_data['mainroad'] == 'yes' else 0
        guestroom = 1 if form_data['guestroom'] == 'yes' else 0 
        basement = 1 if form_data['basement'] == 'yes' else 0 
        hotwaterheating = 1 if form_data['hotwaterheating'] == 'yes' else 0 
        airconditioning = 1 if form_data['airconditioning'] == 'yes' else 0 
        parking = 1 if form_data ['parking'].lower() == 'yes' else 0
        prefarea = 1 if form_data['prefarea'] == 'yes' else 0 

        #create feature vector
        features = [[area, bedrooms , bathrooms, stories , mainroad, guestroom , basement, hotwaterheating , airconditioning, parking , prefarea]]

        #predict price
        prediction = model.predict(features)
        predicted_price = round(prediction[0], 2)

        return render_template('results.html' , predicted_price = predicted_price)
    

if __name__ == '__main__':
    app.run(debug=True)