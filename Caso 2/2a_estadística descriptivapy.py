import pandas as pd

# Configuración para ver TODAS las columnas y filas completas
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Cargar datos
df = pd.read_csv("https://raw.githubusercontent.com/daramireh/simonBolivarCienciaDatos/refs/heads/main/Student_Performance.csv")
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
df = df.drop_duplicates()

print("\nDESCRIPTIVO COMPLETO")
print(df.describe(include='all'))

print("\nFRECUENCIAS CATEGÓRICAS")
print(df['extracurricular_activities'].value_counts(normalize=True))

print("\nCORRELACIONES")
print(df.corr(numeric_only=True))
