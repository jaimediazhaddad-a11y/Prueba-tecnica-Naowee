import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression

df = pd.read_csv("https://raw.githubusercontent.com/daramireh/simonBolivarCienciaDatos/refs/heads/main/Student_Performance.csv")

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

df["extra_num"] = df["extracurricular_activities"].map({"Yes":1,"No":0})
df["low_perf"] = (df["performance_index"] < 40).astype(int)

X = df[["hours_studied","previous_scores","sleep_hours",
        "sample_question_papers_practiced","extra_num"]]

# REGRESIÓN
y_reg = df["performance_index"]
Xtr,Xts,yr_tr,yr_ts = train_test_split(X, y_reg, test_size=0.2, random_state=42)
reg = LinearRegression().fit(Xtr, yr_tr)
print("Pred. regresión:", reg.predict(Xts[:5]))

# CLASIFICACIÓN
y_clf = df["low_perf"]
Xtr2,Xts2,yc_tr,yc_ts = train_test_split(X, y_clf, test_size=0.2, random_state=42)
clf = LogisticRegression().fit(Xtr2, yc_tr)
print("Pred. clasificación:", clf.predict(Xts2[:5]))
