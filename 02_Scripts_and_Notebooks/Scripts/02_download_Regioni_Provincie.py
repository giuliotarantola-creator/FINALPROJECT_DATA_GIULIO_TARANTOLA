import os
import pandas as pd

# Definisco da dove scaricare e dove salvare il file csv.
url_anagrafica = "https://raw.githubusercontent.com/opendatasicilia/comuni-italiani/main/dati/comuni.csv"
percorso_salvataggio = "01_Data/Raw_Data/istat_regioni_provincie.csv"

df_scaricato = pd.read_csv(url_anagrafica, dtype={'pro_com_t': str})
df_scaricato.to_csv(percorso_salvataggio, index=False)