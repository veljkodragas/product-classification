import joblib

# Učitavanje modela
model = joblib.load("models/product_classifier.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

print("Model učitan. Unesi naziv proizvoda za predikciju kategorije.\n")

while True:
    text = input("Unesi naziv proizvoda (ili 'exit' za izlaz): ")

    if text.lower() == "exit":
        break

    X_vec = vectorizer.transform([text])
    prediction = model.predict(X_vec)[0]

    print(f"Predicted Category: {prediction}\n")
