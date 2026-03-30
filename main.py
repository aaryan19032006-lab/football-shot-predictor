import pandas as pd
from sklearn.linear_model import LogisticRegresison

# 1st step:- Load dataset
df = pd.read_csv("dataset.csv")

# 2nd step:- Introducing features and target
X = df[["distance", "angle", "pressure"]]
y = df["goal"]

# 3rd step:- Train model
model = LogisticRegression()
model.fit(X, y)

# 4th step:- Show accuracy
print("\nModel Accuracy:", round(model.score(X, y), 2))

# 5th step:- User input
print("\n--- Football Shot Success Predictor ---")

distance = float(input("Enter distance from goal (in meters): "))
angle = float(input("Enter angle (in degrees): "))
pressure = int(input("Enter pressure (0 = low, 1 = medium, 2 = high): "))

# 6th step:- Prediction
input_data = pd.DataFrame([[distance, angle, pressure]],
                          columns=["distance", "angle", "pressure"])

prediction = model.predict(input_data)
probability = model.predict_proba(input_data)[0][1]

# 7th step:- Difficulty classification
if probability > 0.7:
    difficulty = "Easy Chance 🟢"
elif probability > 0.4:
    difficulty = "Medium Chance 🟡"
else:
    difficulty = "Difficult Chance 🔴"

# 8th step:-Explanation logic
reasons = []

if distance > 20:
    reasons.append("Long distance reduced scoring chance")
else:
    reasons.append("Close distance improved scoring chance")

if angle > 40:
    reasons.append("Good angle increased scoring chance")
else:
    reasons.append("Narrow angle reduced scoring chance")

if pressure == 2:
    reasons.append("High defender pressure made scoring harder")
elif pressure == 1:
    reasons.append("Moderate pressure slightly affected the shot")
else:
    reasons.append("Low pressure improved scoring chance")

# 9th step:- Output
print("\n--- Result ---")
print("Prediction:", "GOAL ⚽" if prediction[0] == 1 else "MISS ❌")
print("Probability of scoring:", round(probability, 2))
print("Difficulty:", difficulty)

print("\nExplanation:")
for r in reasons:
    print("-", r)





