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

🚀 Quickstart 

1. Clone the RepositoryBashgit clone [https://github.com/YOUR_USERNAME/height-prediction-ml.git](https://github.com/YOUR_USERNAME/height-prediction-ml.git)
cd height-prediction-ml

2. Create and Activate Virtual EnvironmentOn Linux / macOS:Bashpython3 -m venv venv
source venv/bin/activate
On Windows (Command Prompt / PowerShell):DOSpython -m venv venv
venv\Scripts\activate

3. Install DependenciesBashpip install -r requirements.txt

4. Run Model TrainingBashpython train.py

5. Test Interactive PredictionBashpython predict.py
📊 Model Evaluation MetricsMean Absolute Error (MAE): Measures average distance between predicted height and actual height.$R^2$ Score: Measures proportion of variance explained by weight.🛠️ Built WithPython 3Pandas & NumPy — Data manipulationScikit-Learn — Machine learning algorithm and metrics

---

<Sequence>
  <Step subtitle="Initialize Git repo and activate python venv" title="Set Up Local Git Repository and Environment">

Run these terminal commands step-by-step:

```bash

# 1. Initialize local git repository
git init

# 2. Create virtual environment named 'venv'
python -m venv venv

# 3. Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# 4. Install dependencies and create requirements file
pip install numpy pandas scikit-learn joblib
pip freeze > requirements.txt

# 1. Add files to Git tracking
git add .

# 2. Make initial commit
git commit -m "feat: initial commit for height prediction regression model"

# 3. Rename branch to main
git branch -M main

# 4. Link to your empty GitHub repository (Replace URL with your repo URL)
git remote add origin https://github.com/YOUR_USERNAME/height-prediction-ml.git

# 5. Push code to GitHub
git push -u origin main