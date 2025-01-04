import joblib

# Load model hanya sekali untuk efisiensi
MODEL_PATH = "model/SVM_model.joblib"

model = joblib.load(MODEL_PATH)
print("model berhasil di pakai")

def predict_from_data(data):    
    # Prediksi menggunakan model
    predicted_label = model.predict(data)

    return predicted_label.item()
