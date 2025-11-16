import joblib
import os
from sklearn.preprocessing import StandardScaler

# --- 1. Putanje ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS_DIR = os.path.join(BASE_DIR, "models")

# --- 2. Učitavanje modela ---
model = joblib.load(os.path.join(MODELS_DIR, "product_classifier.pkl"))
vectorizer = joblib.load(os.path.join(MODELS_DIR, "tfidf_vectorizer.pkl"))
scaler = joblib.load(os.path.join(MODELS_DIR, "scaler.pkl"))

print("Model učitan. Unesi naziv proizvoda za predikciju kategorije.\n")

while True:
    text = input("Unesi naziv proizvoda (ili 'exit' za izlaz): ")

    if text.lower() == "exit":
        break

    # TF-IDF transformacija
    X_vec = vectorizer.transform([text])

    # Numerički feature-i
    title_length = len(text)
    word_count = len(text.split())
    has_numbers = int(any(c.isdigit() for c in text))
    has_caps = sum(1 for c in text if c.isupper())

    import numpy as np
    X_numeric = np.array([[title_length, word_count, has_numbers, has_caps]])
    X_numeric_scaled = scaler.transform(X_numeric)

    # Kombinacija TF-IDF + numeričkih feature-a
    from scipy.sparse import hstack
    X_input = hstack([X_vec, X_numeric_scaled])

    # Predikcija
    prediction = model.predict(X_input)[0]

    print(f"Predviđena kategorija: {prediction}\n")
