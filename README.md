# Product Category Classification

Ovaj projekat trenira mašinski model koji automatski prepoznaje kojoj kategoriji pripada proizvod na osnovu njegovog naziva. Koristi se TF-IDF obrada teksta i Logistic Regression model.

---

## 📁 Struktura projekta

product-classification/
│── data/
│ └── IMLP4_TASK_03-products.csv # Dataset
│── scripts/
│ ├── train_model.py # Skripta za treniranje modela
│ └── predict_category.py # Skripta za predikciju kategorije
│── models/ # Folder sa sačuvanim modelima
│── notebooks/ # Folder za Jupyter sveske
│── README.md # Dokumentacija projekta



## ⚙️ Instalacija

Pokreni u terminalu:

```bash
pip install pandas scikit-learn joblib openpyxl
```

---

## 🚀 Treniranje modela

Pokreni komandno:

```bash
python train_model.py
```

Ako je sve dobro, videćeš:

- Classification Report
- Poruku da su model i TF-IDF vektorizator sačuvani u folderu `models/`

---

## 🔮 Korišćenje modela za predikciju

Pokreni:

```bash
python predict_category.py
```

Skripta će te pitati:

```
Unesi naziv proizvoda:
```

Ti uneseš npr.:

```
Samsung Galaxy S21 128GB
```

A skripta odgovara:

```
Predviđena kategorija: Mobile Phones
```

---

## 📌 Napomena

Model radi samo ako folder **models/** postoji i sadrži:

- `model.pkl`
- `vectorizer.pkl`

Ove fajlove automatski pravi `train_model.py`.

---

## ✔️ Kraj projekta

Ovaj projekat ispunjava sve zahteve:

- Učitavanje dataset-a  
- Treniranje modela  
- Čuvanje modela  
- Učitavanje modela  
- Predikcije preko terminala  
- README dokumentacija  

