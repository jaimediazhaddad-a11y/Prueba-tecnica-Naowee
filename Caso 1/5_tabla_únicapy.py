import pandas as pd

# Cargar datos
matches = pd.read_csv(
    "https://raw.githubusercontent.com/daramireh/simonBolivarCienciaDatos/refs/heads/main/matches_1991_2023.csv"
)
m = matches.rename(columns=str.lower)

# Tabla "larga" uniendo home y away
home = pd.DataFrame({
    "year": m["year"], "host": m["host"], "equipo": m["home_team"],
    "gf": m["home_score"], "gc": m["away_score"],
    "pg": (m["home_score"] > m["away_score"]).astype(int),
    "pe": (m["home_score"] == m["away_score"]).astype(int),
    "pp": (m["home_score"] < m["away_score"]).astype(int),
    "asistencia": m["attendance"]
})

away = pd.DataFrame({
    "year": m["year"], "host": m["host"], "equipo": m["away_team"],
    "gf": m["away_score"], "gc": m["home_score"],
    "pg": (m["away_score"] > m["home_score"]).astype(int),
    "pe": (m["away_score"] == m["home_score"]).astype(int),
    "pp": (m["away_score"] < m["home_score"]).astype(int),
    "asistencia": m["attendance"]
})

tabla = pd.concat([home, away])

# Agrupar por año + host + equipo
res = tabla.groupby(["year", "host", "equipo"]).agg(
    pj=("equipo", "count"),
    gf_total=("gf", "sum"),
    gf_prom=("gf", "mean"),
    gc_total=("gc", "sum"),
    gc_prom=("gc", "mean"),
    pg=("pg", "sum"),
    pe=("pe", "sum"),
    pp=("pp", "sum"),
    asistencia_prom=("asistencia", "mean")
).reset_index()

print(res)
