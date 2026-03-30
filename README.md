## ⚽ Football Goal Predictor (AI Mini-Project)

---

## 📝 Project Overview

This is my first Machine Learning Project for my Fundamentals in AI & ML Course.
I built an AI Shot Predictor that calculates the probability if a football player will score a goal or miss based on certain match conditions.

It uses Logistic Regression to handle the math behind the scenes.

---

## 🎯 Why I Built This?

I wanted to see how ML models work and how they can be applied to sports.

In real matches, players make split-second decisions. This tool helps visualize the probability of a goal by looking at:

* Distance from the goal
* Shooting angle
* Defender pressure

---

## 🛠️ Tech Stack & Concepts

* **Language:** Python 3.x

* **Libraries:**

  * Pandas (for data handling)
  * Scikit-Learn (for ML model)
  * NumPy

* **Math Concept:**

  * Logistic Regression (binary classification: Goal vs No Goal)

* **Logic:**

  * Basic if-else branching for explanation module

---

## 📂 Files in this Folder

* `main.py` → Main Python code
* `dataset.csv` → Training dataset (manually created)
* `README.md` → Project documentation

---

## 🚀 How to Run (Setup)

1. Make sure Python is installed
2. Install required libraries:

```bash
pip install pandas scikit-learn
```

3. Run the program:

```bash
python main.py
```

---

## 🎮 How It Works (User Flow)

After running the code, you will be asked for:

* Distance (e.g., 10 meters)
* Angle (e.g., 45 degrees)
* Pressure (0 = low, 1 = medium, 2 = high)

---

## 📌 Example Output

```
Result: GOAL ⚽  
Probability: 82%  
Difficulty: Easy Chance 🟢  

Reasoning:  
Since you are close to the goal, the chance is very high!
```

---

## 📊 About the Dataset

Since I couldn't find a small enough dataset, I manually generated `dataset.csv` with 50+ rows based on football logic, such as:

* If distance > 30m → Goal = 0
* Better angle → Higher chance
* Higher pressure → Lower chance

This helped train the model to understand patterns.

---

## 🚧 Challenges I Faced

* Importing CSV file issues (fixed by correcting file path)
* Understanding difference between `predict` and `predict_proba`
* Formatting output properly in terminal

---

## 🔮 Future Plans

* [ ] Add GUI using Tkinter
* [ ] Use real-world dataset (e.g., EPL data)
* [ ] Try other ML models like Decision Trees

---

## 👨‍💻 Submission Details

* **Name:** Aanjneya Singh
* **Branch:** B.Tech CSE AI & ML - 1st Year
* **Roll No:** 25BAI10885
