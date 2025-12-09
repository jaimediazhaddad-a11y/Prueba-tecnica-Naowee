import pandas as pd
from scipy.stats import ttest_ind

# Cargar datos
df = pd.read_csv("https://raw.githubusercontent.com/daramireh/simonBolivarCienciaDatos/refs/heads/main/Student_Performance.csv")
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
df = df.drop_duplicates()

# Separar grupos
yes = df[df["extracurricular_activities"] == "Yes"]["performance_index"]
no = df[df["extracurricular_activities"] == "No"]["performance_index"]

# Descriptivo por grupo
print("Media Yes:", yes.mean(), " - std Yes:", yes.std(), " - n Yes:", yes.count())
print("Media No:", no.mean(), " - std No:", no.std(), " - n No:", no.count())

stat, p_value = ttest_ind(yes, no, equal_var=False)

print("Estadístico t:", stat)
print("p-valor:", p_value)
