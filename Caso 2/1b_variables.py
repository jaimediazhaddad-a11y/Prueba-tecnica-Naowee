import pandas as pd

# Cargar dataset desde la URL
df = pd.read_csv("https://raw.githubusercontent.com/daramireh/simonBolivarCienciaDatos/refs/heads/main/Student_Performance.csv")

# Normalizar nombres de columnas (opcional pero recomendado)
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# 1. Mostrar variables
print(df.columns.tolist())

# 2. Tipos de dato
print(df.dtypes)

# 3. Valores nulos
print(df.isnull().sum())

# 4. Filas duplicadas
print(df.duplicated().sum())

# 5. Estadísticas generales
print(df.describe(include="all"))
