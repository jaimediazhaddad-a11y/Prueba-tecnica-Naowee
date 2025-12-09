import pandas as pd
import ast

# Función para contar eventos en columnas tipo lista en texto
def count_events(val):
    if pd.isna(val) or val == "":
        return 0
    try:
        lista = ast.literal_eval(val)
        if isinstance(lista, list):
            return len(lista)
        return 1
    except Exception:
        return 1

matches = pd.read_csv(
    "https://raw.githubusercontent.com/daramireh/simonBolivarCienciaDatos/refs/heads/main/matches_1991_2023.csv"
)
matches.columns = matches.columns.str.strip().str.lower().str.replace(" ", "_")

# Filtrar sólo mundial 1991
m1991 = matches[matches["year"] == 1991].copy()

# Contar tarjetas por lado
m1991["home_yellow"] = m1991["home_yellow_card_long"].apply(count_events)
m1991["away_yellow"] = m1991["away_yellow_card_long"].apply(count_events)

# Rojas = rojas directas + doble amarilla
m1991["home_red"] = (
    m1991["home_red_card"].apply(count_events)
    + m1991["home_yellow_red_card"].apply(count_events)
)
m1991["away_red"] = (
    m1991["away_red_card"].apply(count_events)
    + m1991["away_yellow_red_card"].apply(count_events)
)

# Lado local
home = pd.DataFrame({
    "equipo": m1991["home_team"],
    "gf": m1991["home_score"],
    "gc": m1991["away_score"],
    "pg": (m1991["home_score"] > m1991["away_score"]).astype(int),
    "pe": (m1991["home_score"] == m1991["away_score"]).astype(int),
    "pp": (m1991["home_score"] < m1991["away_score"]).astype(int),
    "yellow": m1991["home_yellow"],
    "red": m1991["home_red"],
})

# Lado visitante
away = pd.DataFrame({
    "equipo": m1991["away_team"],
    "gf": m1991["away_score"],
    "gc": m1991["home_score"],
    "pg": (m1991["away_score"] > m1991["home_score"]).astype(int),
    "pe": (m1991["away_score"] == m1991["home_score"]).astype(int),
    "pp": (m1991["away_score"] < m1991["home_score"]).astype(int),
    "yellow": m1991["away_yellow"],
    "red": m1991["away_red"],
})

# Unir filas de local y visitante
tabla = pd.concat([home, away], ignore_index=True)

# Agregar por equipo
res = tabla.groupby("equipo").agg(
    pj=("equipo", "count"),
    pg=("pg", "sum"),
    pe=("pe", "sum"),
    pp=("pp", "sum"),
    gf=("gf", "sum"),
    gc=("gc", "sum"),
    yellow=("yellow", "sum"),
    red=("red", "sum"),
).reset_index()

# Diferencia de gol
res["dg"] = res["gf"] - res["gc"]

# Juego limpio (JL): amarilla = -1, roja = -2
res["jl"] = -1 * res["yellow"] + -2 * res["red"]

# Puntos por resultado: 3*PG + 1*PE
res["puntos"] = 3 * res["pg"] + 1 * res["pe"]

# Ordenar por puntos, luego DG, luego GF
res = res.sort_values(
    by=["puntos", "dg", "gf"],
    ascending=[False, False, False]
).reset_index(drop=True)

# Dejar sólo las columnas pedidas
res = res[[
    "equipo", "pj", "pg", "pe", "pp",
    "gf", "gc", "dg", "jl", "puntos"
]]

print(res)
