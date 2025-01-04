from flask import Flask, request, jsonify
from etl import preprocess_data,load_data
from model import predict_from_data
from flask import Flask, request, jsonify
from flask_cors import CORS  

# Inisialisasi aplikasi Flask
app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Welcome to the AI Prediction API!"

@app.route('/predict', methods=['POST'])
def predict():

    # Pastikan ada file dengan nama key 'file' (atau key lainnya)
    file_key = next(iter(request.files.keys()), None)
    if not file_key:
        return jsonify({'error': 'No file key provided'}), 400

    file = request.files[file_key]
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    
    try:
        # Membaca file gambar sebagai byte
        image = file.read()
        
        image_bytes = load_data(image)

        # Memproses data gambar (menggunakan TensorFlow untuk decoding dan resizing)
        image = preprocess_data(image_bytes)  # Fungsi ini untuk memproses gambar
        
        # Prediksi menggunakan model
        prediction = predict_from_data(image)
        
        return jsonify(prediction)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
