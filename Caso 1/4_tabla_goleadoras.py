import pandas as pd

matches = pd.read_csv(
    "https://raw.githubusercontent.com/daramireh/simonBolivarCienciaDatos/refs/heads/main/matches_1991_2023.csv"
)
matches.columns = matches.columns.str.strip().str.lower().str.replace(" ", "_")

m = matches[matches["year"] == 2023].copy()

#Convertir listas en nmbres
m["home_goal_nombres"] = m["home_goal"].fillna("").apply(
    lambda x: [p.split("·")[0].strip() for p in str(x).split("|") if "·" in p]
)
m["away_goal_nombres"] = m["away_goal"].fillna("").apply(
    lambda x: [p.split("·")[0].strip() for p in str(x).split("|") if "·" in p]
)

#Listas en una sola
todas = m["home_goal_nombres"].sum() + m["away_goal_nombres"].sum()

#Goles por jugadoras
tabla = pd.Series(todas).value_counts().reset_index()
tabla.columns = ["jugadora", "goles"]

print(tabla)

