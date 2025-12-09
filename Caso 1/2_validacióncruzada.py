import pandas as pd

wc = pd.read_csv("https://raw.githubusercontent.com/daramireh/simonBolivarCienciaDatos/refs/heads/main/world_cup_women.csv")
matches = pd.read_csv("https://raw.githubusercontent.com/daramireh/simonBolivarCienciaDatos/refs/heads/main/matches_1991_2023.csv")

# NORMALIZAR COLUMNAS
wc.columns = wc.columns.str.strip().str.lower().str.replace(" ", "_")
matches.columns = matches.columns.str.strip().str.lower().str.replace(" ", "_")

# CAMPOS COMUNES
common_cols = (set(wc.columns) & set(matches.columns))
print(common_cols)

# VALIDACIÓN DE CAMPOS RELACIONADOS

# AÑO
print("\nYEAR")
print("Nulos WC:", wc.year.isna().sum(), " | Nulos matches:", matches.year.isna().sum())
print("Diferencia WC y Matches:", set(wc.year) - set(matches.year))
print("Diferencia Matches y WC:", set(matches.year) - set(wc.year))

# HOST
print("\nHOST")
print("Nulos wc:", wc.host.isna().sum(), " | Nulos matches:", matches.host.isna().sum())
print("Diferencia WC y Matches:", set(wc.host) - set(matches.host))
print("Diferencia Matches y WC:", set(matches.host) - set(wc.host))

# ATTENDANCE
print("\nATTENDANCE (agregado por año)")
print("Nulos wc:", wc.attendance.isna().sum(), " | Nulos matches:", matches.attendance.isna().sum())

att_wc = wc[["year", "attendance"]]
att_matches = matches.groupby("year")["attendance"].sum().reset_index()

df = att_wc.merge(att_matches, on="year", how="left", suffixes=("_wc", "_matches"))
df["coinciden"] = df.attendance_wc == df.attendance_matches
print(df)

# Partidos con attendance = 0
zeros = matches[matches["attendance"] == 0][
    ["year", "home_team", "away_team", "attendance"]
]

print("\nPartidos con asistencia = 0:")
print(zeros.head(100))
