import pandas as pd

url_wc = "https://raw.githubusercontent.com/daramireh/simonBolivarCienciaDatos/refs/heads/main/world_cup_women.csv"
url_matches = "https://raw.githubusercontent.com/daramireh/simonBolivarCienciaDatos/refs/heads/main/matches_1991_2023.csv"
wc = pd.read_csv(url_wc)
matches = pd.read_csv(url_matches)


wc.columns = wc.columns.str.strip().str.lower().str.replace(" ", "_")

# Corregir finalistas 2023
wc.loc[wc['year'] == 2023, 'champion'] = 'Spain'
wc.loc[wc['year'] == 2023, 'runner-up'] = 'England'

wc.head()

