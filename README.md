# Product Category Classification

Ovaj projekat trenira mašinski model koji automatski prepoznaje kojoj kategoriji pripada proizvod na osnovu njegovog naziva. Koristi se TF-IDF obrada teksta, dodatni numerički feature-i i Logistic Regression model.

---

## 📁 Struktura projekta

```
product-classification/
│── data/
│   └── IMLP4_TASK_03-products.csv    # Dataset
│── scripts/
│   ├── train_model.py                 # Skripta za treniranje modela
│   └── predict_category.py            # Skripta za predikciju kategorije
│── models/                            # Folder sa sačuvanim modelima i vektorizatorom
│   ├── product_classifier.pkl
│   ├── tfidf_vectorizer.pkl
│   └── scaler.pkl
│── notebooks/                         # Folder za Jupyter sveske (opciono)
│── README.md                          # Dokumentacija projekta
```

---

## ⚙️ Instalacija

Pokreni u terminalu:

```bash
pip install pandas scikit-learn joblib matplotlib scipy openpyxl
```

---

## 🚀 Treniranje modela

Pokreni skriptu:

```bash
python scripts/train_model.py
```

Ako je sve dobro, videćeš:

- Accuracy i Classification Report  
- Confusion matrix grafikon  
- Poruku da su **model**, **TF-IDF vektorizator** i **scaler** sačuvani u folderu `models/`

---

## 🌮 Korišćenje modela za predikciju

Pokreni:

```bash
python scripts/predict_category.py
```

Skripta će te pitati:

```
Unesi naziv proizvoda (ili 'exit' za izlaz):
```

Primer unosa:

```
Samsung Galaxy S21 128GB
```

Odgovor će biti:

```
Predviđena kategorija: Mobile Phones
```

---

## 📍 Napomene

- Model radi samo ako folder **models/** postoji i sadrži:
  - `product_classifier.pkl`
  - `tfidf_vectorizer.pkl`
  - `scaler.pkl`
- Dodatni numerički feature-i uključuju:
  - Dužinu naziva proizvoda (`title_length`)
  - Broj reči u nazivu (`word_count`)
  - Da li naziv sadrži brojeve (`has_numbers`)
  - Broj velikih slova (`has_caps`)

---

## ✔️ Kraj projekta

Ovaj projekat obuhvata:

- Učitavanje dataset-a  
- Treniranje modela sa TF-IDF i numeričkim feature-ima  
- Čuvanje modela i vektorizatora  
- Predikcije preko terminala  
- Confusion matrix vizualizaciju  
- Jasnu README dokumentaciju

