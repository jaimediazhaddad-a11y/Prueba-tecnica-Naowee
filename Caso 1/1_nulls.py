import pandas as pd

wc = pd.read_csv("https://raw.githubusercontent.com/daramireh/simonBolivarCienciaDatos/refs/heads/main/world_cup_women.csv")
matches = pd.read_csv("https://raw.githubusercontent.com/daramireh/simonBolivarCienciaDatos/refs/heads/main/matches_1991_2023.csv")

# NNOTMALIZAR COLUMNAS
wc.columns = wc.columns.str.lower().str.replace(" ", "_")
matches.columns = matches.columns.str.lower().str.replace(" ", "_")

# ANÁLISIS WC
print("\nWC ")
print("\nVariables:")
print(wc.columns.tolist())

print("\nTipos de datos:")
print(wc.dtypes)

print("\nValores nulos:")
print(wc.isna().sum())

print("\nFilas duplicadas:", wc.duplicated().sum())

# ANÁLISIS MATCHES
print("\nMATCHES")
print("\nVariables:")
print(matches.columns.tolist())

print("\nTipos de datos:")
print(matches.dtypes)

print("\nValores nulos:")
print(matches.isna().sum())

print("\nFilas duplicadas:", matches.duplicated().sum())
