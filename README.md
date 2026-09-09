# 📏 Height Prediction using Simple Linear Regression

A beginner-friendly Supervised Machine Learning project that predicts a person's height (in cm) based on their weight (in kg) using **Simple Linear Regression** implemented with `scikit-learn`.

---

## 📌 Problem Overview

* **Task Type:** Supervised Learning — Simple Linear Regression
* **Input Feature ($X$):** Weight in kilograms (`Weight_kg`)
* **Target Output ($y$):** Height in centimeters (`Height_cm`)
* **Core Equation Learned:** $\text{Height} = (w \cdot \text{Weight}) + b$

---

## 📁 Repository Structure

```text
.
├── .gitignore         # Ignored files (virtual envs, cache)
├── requirements.txt   # Python dependencies
├── train.py           # Script to train and evaluate the model
├── predict.py         # Script to take real-time interactive user input
└── README.md          # Project documentation