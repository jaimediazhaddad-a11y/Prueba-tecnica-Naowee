import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, recall_score, f1_score

df = pd.read_csv("https://raw.githubusercontent.com/daramireh/simonBolivarCienciaDatos/refs/heads/main/Student_Performance.csv")
df.columns = df.columns.str.lower().str.replace(" ", "_")
df["extra_num"] = df["extracurricular_activities"].map({"Yes":1,"No":0})
df["low_perf"] = (df["performance_index"] < 40).astype(int)

X = df[["hours_studied","previous_scores","sleep_hours",
        "sample_question_papers_practiced","extra_num"]]
y = df["low_perf"]

sc = StandardScaler()
X_scaled = sc.fit_transform(X)

Xtr, Xts, ytr, yts = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

models = {
    "Logistic": LogisticRegression(),
    "RandomForest": RandomForestClassifier(),
    "GradientBoosting": GradientBoostingClassifier()
}

for name, model in models.items():
    model.fit(Xtr, ytr)
    pred = model.predict(Xts)
    print(name,
          "Accuracy:", accuracy_score(yts, pred),
          "Recall:", recall_score(yts, pred),
          "F1:", f1_score(yts, pred))
