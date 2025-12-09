import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

df = pd.read_csv("https://raw.githubusercontent.com/daramireh/simonBolivarCienciaDatos/refs/heads/main/Student_Performance.csv")
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
df = df.drop_duplicates()

df["extra_num"] = df["extracurricular_activities"].map({"Yes":1, "No":0})

features = ["hours_studied", "previous_scores", "sleep_hours",
            "sample_question_papers_practiced", "extra_num"]

# Escalar
scaler = StandardScaler()
X = scaler.fit_transform(df[features])

# 3 grupos de Clusters
kmeans = KMeans(n_clusters=3, random_state=42)
df["cluster"] = kmeans.fit_predict(X)

clusters_all = df.groupby("cluster")[features + ["performance_index"]].mean()
print(clusters_all)
