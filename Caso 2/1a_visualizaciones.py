import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("https://raw.githubusercontent.com/daramireh/simonBolivarCienciaDatos/refs/heads/main/Student_Performance.csv")
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
df = df.drop_duplicates()

sns.set(style="whitegrid")


# 1. Hours Studied vs Performance
plt.figure(figsize=(6,4))
sns.regplot(data=df, x='hours_studied', y='performance_index', scatter_kws={'alpha':0.3})
plt.title("Hours Studied vs Performance Index (Tendencia)")
plt.show()

# 2. Previous Scores vs Performance
plt.figure(figsize=(6,4))
sns.regplot(data=df, x='previous_scores', y='performance_index', scatter_kws={'alpha':0.3}, color='green')
plt.title("Previous Scores vs Performance Index (Tendencia)")
plt.show()

# 3. Sleep Hours vs Performance
plt.figure(figsize=(6,4))
sns.regplot(data=df, x='sleep_hours', y='performance_index', scatter_kws={'alpha':0.3}, color='orange')
plt.title("Sleep Hours vs Performance Index (Tendencia)")
plt.show()

# 4. Sample Papers Practiced vs Performance
plt.figure(figsize=(6,4))
sns.regplot(data=df, x='sample_question_papers_practiced', y='performance_index', scatter_kws={'alpha':0.3}, color='red')
plt.title("Sample Question Papers Practiced vs Performance Index (Tendencia)")
plt.show()

# 5. Extracurricular Activities vs Performance
plt.figure(figsize=(6,4))
sns.boxplot(data=df, x='extracurricular_activities', y='performance_index', palette='Set2')
plt.title("Extracurricular Activities vs Performance Index")
plt.show()

# Convertir Yes/No a 1/0 para incluirlo en la correlación
df['extracurricular_activities_num'] = df['extracurricular_activities'].map({'Yes': 1, 'No': 0})

# Selección de variables numéricas (todas)
numeric_df = df[['hours_studied',
                 'previous_scores',
                 'sleep_hours',
                 'sample_question_papers_practiced',
                 'extracurricular_activities_num',
                 'performance_index']]

# Correlaciones
corr = numeric_df.corr()

plt.figure(figsize=(10,6))
sns.heatmap(corr, annot=True, cmap="Blues", linewidths=.5, fmt=".2f")
plt.title("Heatmap de Correlación entre Todas las Variables")
plt.show()

sns.pairplot(numeric_df, diag_kind="kde")
plt.suptitle("Matriz de Dispersión - Todas las Variables")
plt.show()

plt.figure(figsize=(6,4))
sns.violinplot(data=df, x='extracurricular_activities', y='performance_index', palette="Set2")
plt.title("Distribución del Performance Index por Actividades Extracurriculares")
plt.show()

sns.jointplot(
    data=df, 
    x="previous_scores", 
    y="performance_index", 
    kind="reg", 
    height=6, 
    scatter_kws={'alpha':0.3}
)
