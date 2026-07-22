# Breast-Cancer-Prediction-Logistic-regression-model
# 🩺 Breast Cancer Prediction using Logistic Regression

## 📌 Project Overview

Breast Cancer Prediction is a Machine Learning classification project developed using the **Breast Cancer Wisconsin (Diagnostic)** dataset. The objective is to predict whether a breast tumor is **Malignant (Cancerous)** or **Benign (Non-Cancerous)** based on cell nuclei measurements extracted from Fine Needle Aspirate (FNA) images.

The project follows a complete Machine Learning workflow, including data preprocessing, exploratory data analysis (EDA), feature engineering, model building, evaluation, and deployment using Streamlit.

---

# 🎯 Problem Statement

Develop a Machine Learning model capable of accurately classifying breast tumors as **Malignant** or **Benign** using diagnostic measurements. Early prediction can assist healthcare professionals in making timely clinical decisions.

---

# 📂 Dataset Information

* **Dataset:** Breast Cancer Wisconsin (Diagnostic)
* **Source:** Kaggle
* **Rows:** 569
* **Columns:** 33
* **Target Variable:** `diagnosis`

  * **M = Malignant**
  * **B = Benign**

---

# 🛠 Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn
* Streamlit
* Pickle

---

# 📊 Project Workflow

1. Import Libraries
2. Load Dataset
3. Data Understanding
4. Data Cleaning
5. Exploratory Data Analysis (EDA)
6. Outlier Handling using IQR Clipping
7. Feature Selection
8. Feature Scaling using StandardScaler
9. Train-Test Split
10. Logistic Regression Model
11. Model Evaluation
12. Cross Validation
13. Predict New Data
14. Save Model using Pickle
15. Deploy using Streamlit

---

# 📈 Exploratory Data Analysis

The following analyses were performed:

* Histograms
* Boxplots
* Scatterplots
* Count Plot
* Correlation Heatmap

Key observations:

* Dataset contains no missing values except the empty `Unnamed: 32` column.
* Strong correlations exist among radius, perimeter, and area-related features.
* Benign cases are slightly more frequent than Malignant cases.
* Several features clearly separate the two classes.

---

# ⚙ Data Preprocessing

* Removed `id` column
* Removed `Unnamed: 32`
* Checked duplicate values
* Applied IQR Clipping to reduce outlier influence
* Encoded diagnosis

  * M → 1
  * B → 0
* Selected highly correlated features
* Applied StandardScaler

---

# 🤖 Machine Learning Model

**Algorithm Used**

* Logistic Regression

### Why Logistic Regression?

* Suitable for Binary Classification
* Fast Training
* Easy to Interpret
* Excellent Performance on Medical Classification Problems

---

# 📊 Model Performance

| Metric            | Score  |
| ----------------- | ------ |
| Training Accuracy | 95%    |
| Testing Accuracy  | 98%    |
| Precision         | 1.00   |
| Recall            | 0.94   |
| F1 Score          | 0.97   |
| ROC-AUC           | 0.9999 |

Cross Validation Accuracy:

* **5-Fold Cross Validation Mean Accuracy:** **95%**

---

# 📉 Evaluation Techniques

* Accuracy Score
* Precision Score
* Recall Score
* F1 Score
* Confusion Matrix
* ROC Curve
* AUC Score
* Cross Validation

---

# 💾 Saved Files

The project saves:

* `model.pkl`
* `scaler.pkl`
* `features.pkl`

These files are used by the Streamlit application for prediction.

---

# 🌐 Streamlit Deployment

The Streamlit application allows users to:

* Enter feature values
* Scale input automatically
* Predict whether the tumor is Malignant or Benign
* Display prediction confidence

---

# 📁 Repository Structure

```

Breast-Cancer-Prediction

│

├── Breast\\\_Cancer\\\_Prediction\\\_Logistic\\\_Regression.ipynb

├── Breast\\\_Cancer\\\_Prediction\\\_Documentation.pdf

├── app.py

├── model.pkl

├── scaler.pkl

├── features.pkl

├── requirements.txt

├── README.md

└── data.csv

```

---

# 🚀 How to Run

Clone the repository:

```bash

git clone https://github.com/yourusername/Breast-Cancer-Prediction.git

```

Install dependencies:

```bash

pip install -r requirements.txt

```

Run the Streamlit application:

```bash

streamlit run app.py

```

---

# 📌 Future Improvements

* Compare multiple Machine Learning algorithms
* Hyperparameter Optimization
* Deep Learning implementation
* Cloud Deployment
* Explainable AI using SHAP or LIME

---

# 👩‍💻 Author

**Mukthapuram Prasanthi**

B.Tech (Information Technology)

Machine Learning & Data Science Enthusiast

---

⭐ If you found this project useful, consider giving it a **Star** on GitHub.
