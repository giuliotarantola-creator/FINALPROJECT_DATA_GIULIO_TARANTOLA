# Importo le librerie necessarie.
import requests
import os

# Defenisco il percorso di salvataggio dei file.
percorso_salvataggio = "01_Data/Raw_Data/istat_incidenti_raw.csv"

# Ho definito due variabili, una relativa all'url API ed una per l'headers la quale quest'ultima
# verrà utilizzata nel metodo request per poter restituire un file CSV invece di un XML. 
# Documentazione: https://github.com/ondata/guida-api-istat
url_api_istat = "https://esploradati.istat.it/SDMXWS/rest/data/41_983"
headers_csv = {
    'Accept': 'application/vnd.sdmx.data+csv;version=1.0.0'}

# Effettuo il metodo Request.GET,verifico la risposta, apro un file nel percorso_salvataggio
# che avevo definito come oggetto all'inizio. 
response = requests.get(url_api_istat, headers=headers_csv)
if response.status_code == 200:
    with open(percorso_salvataggio, 'wb') as f:
        f.write(response.content)
    print(f"Download completato! File salvato")
else:
    print(f"Errore durante il download. Status Code: {response.status_code}")