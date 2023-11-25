from flask import Flask, request, jsonify
from tensorflow import keras
from bs4 import BeautifulSoup
import re
import tensorflow as tf
from pyngrok import ngrok

# Set the ngrok path
#ngrok.set_ngrok_path('/usr/local/bin/ngrok')

# Load the pre-trained model
model = keras.models.load_model('/Users/nyagaderrick/Developer/BI-Project/models/cvs_model.h5')

# Define preprocessing functions
def strip_html(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()

def remove_text_before_sentences(text):
    text = re.sub(r'^[A-Z]+\s*-\s*', '', text)
    return text

def remove_words_in_parentheses(text):
    return re.sub(r'\([^)]*\)', '', text)

def remove_dashes(text):
    return text.replace('-', '')

def remove_symbols(text):
    pattern = r'[^A-Za-z0-9\s]'
    return re.sub(pattern, '', text)

def denoise_text(text):
    text = strip_html(text)
    text = remove_text_before_sentences(text)
    text = remove_words_in_parentheses(text)
    text = remove_dashes(text)
    text = remove_symbols(text)
    return text

# Tokenizer settings
max_features = 20000
maxlen = 300
tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=max_features)

# Create a Flask app
app = Flask(__name__)



@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get the text from the POST request
            data = request.get_json(force=True)
            user_input = data.get('text', '')

            # Preprocess user input
            cleaned_input = denoise_text(user_input)

            # Tokenize and pad the input
            tokenizer.fit_on_texts([cleaned_input])
            sequences = tokenizer.texts_to_sequences([cleaned_input])
            input_data = tf.keras.preprocessing.sequence.pad_sequences(sequences, maxlen=maxlen)

            # Make a prediction
            predicted_probability = model.predict(input_data)
            threshold = 0.5  # Adjust the threshold as needed
            predicted_label = "True" if predicted_probability >= threshold else "False"

            # Return the prediction
            return jsonify({'probability': str(predicted_probability[0][0]), 'label': predicted_label})

        except Exception as e:
            return jsonify({'error': str(e)}), 500  # Internal Server Error

    else:
        return jsonify({'error': 'This route only accepts POST requests.'}), 400  # Bad Request

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
    public_url = ngrok.connect(addr="5001")
    print(f"* ngrok tunnel \"{public_url}\" -> \"http://127.0.0.1:5001\"")