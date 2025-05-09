from flask import Flask, request, render_template, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import requests

app = Flask(__name__)

# Load the saved model
model = load_model('1.h5')  # Replace 'your_model.h5' with the path to your h5 file

# Define a function to preprocess the image
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))  # Resize the image as required by your model
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# Define a function to make predictions
def predict_image(img_path):
    try:
        img = preprocess_image(img_path)
        predictions = model.predict(img)
        return predictions
    except Exception as e:
        raise RuntimeError(f'Error during prediction: {e}')

# Define the class labels
class_labels = ['Vitamin A', 'Vitamin B', 'Vitamin C', 'Vitamin D', 'Vitamin E', 'Vitamin K']  

# Define a function to process predictions
def process_predictions(predictions, class_labels):
    try:
        predicted_index = np.argmax(predictions)
        predicted_vitamin = class_labels[predicted_index]
        confidence_score = predictions[0][predicted_index]
        return predicted_vitamin, confidence_score
    except Exception as e:
        raise RuntimeError(f'Error processing predictions: {e}')

# In-memory storage for contact form submissions
contact_submissions = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/vita')
def vita():
    return render_template('vita.html')


@app.route('/diseases')
def diseases():
    return render_template('diseases.html')



@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        # Store the submission as a dict
        contact_submissions.append({
            'name': name,
            'email': email,
            'phone': phone,
            'message': message
        })
        return render_template('contact.html', success=True)
    return render_template('contact.html')

@app.route('/data')
def data():
    return render_template('data.html', submissions=contact_submissions)

@app.route('/predict')
def index():
    return render_template('index.html')
    
@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file uploaded'
    
    file = request.files['file']
    
    if file.filename == '':
        return 'No file selected'
    
    if file:
        # Save the uploaded image temporarily with a unique filename
        img_path = 'uploaded_image.jpg'  
        file.save(img_path)
        try:
            predictions = predict_image(img_path)
            predicted_vitamin, confidence_score = process_predictions(predictions, class_labels)
            result1 = f'Predicted Vitamin: {predicted_vitamin}'
            result2 = f'Confidence Score: {confidence_score}'
        except Exception as e:
            result1 = 'Prediction Error'
            result2 = str(e)
        return render_template('index.html', resultp1=result1, resultp2=result2)



if __name__ == '__main__':
    app.run(debug=True,port=5001)
