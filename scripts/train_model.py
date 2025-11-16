import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay
import joblib
import os
from scipy.sparse import hstack
import matplotlib.pyplot as plt

# --- 1. Učitavanje podataka ---
DATA_PATH = r"C:\Users\Dragas\Downloads\moj task\IMLP4_TASK_03-products.csv"
df = pd.read_csv(DATA_PATH)

# Čišćenje imena kolona
df.columns = df.columns.str.strip()
df = df.rename(columns={
    " Category Label": "Category Label",
    " Listing Date  ": "Listing Date"
})

# Ukloni redove gde nema Product Title ili Category Label
df = df.dropna(subset=["Product Title", "Category Label"])

# --- 2. Feature engineering ---
# Tekstualni feature
X_text = df["Product Title"]

# Dodatni numerički feature-i
df['title_length'] = df['Product Title'].apply(len)
df['word_count'] = df['Product Title'].apply(lambda x: len(str(x).split()))
df['has_numbers'] = df['Product Title'].apply(lambda x: int(any(char.isdigit() for char in str(x))))
df['has_caps'] = df['Product Title'].apply(lambda x: sum(1 for c in str(x) if c.isupper()))

X_numeric = df[['title_length','word_count','has_numbers','has_caps']].values

# --- 3. TF-IDF vektorizacija ---
vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1,2), max_features=10000)
X_vec = vectorizer.fit_transform(X_text)

# Kombinujemo TF-IDF i numeričke feature-e
X = hstack([X_vec, X_numeric])
y = df['Category Label']

# --- 4. Train-test split ---
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- 5. Model ---
model = LogisticRegression(max_iter=500)
model.fit(X_train, y_train)

# --- 6. Evaluacija ---
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Confusion matrix
cm = confusion_matrix(y_test, y_pred, labels=model.classes_)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
disp.plot(xticks_rotation='vertical', cmap=plt.cm.Blues)
plt.tight_layout()
plt.show()

# --- 7. Čuvanje modela ---
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/product_classifier.pkl")
joblib.dump(vectorizer, "models/tfidf_vectorizer.pkl")

print("\nModel i TF-IDF vektorizator su sačuvani u folderu 'models'.")
