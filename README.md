# Data Analytics - Capstone Project
# Analisi Rischio Stradale Italia - Modello B2G

## Descrizione del Progetto
Questo progetto di Data Analytics analizza l'andamento degli incidenti stradali in Italia dal 2019 al 2023. L'obiettivo di business è fornire alla direzione vendite di un'azienda di prevenzione rischi le giuste direttive su dove investire in sicurezza stradale (semafori, guardrail, asfalto drenante), ottimizzando il focus commerciale oltre il classico circuito delle metropoli e puntando ai reali colli di bottiglia del traffico nazionale.

## Struttura dei file
* `01_Data/Raw_Data/`: Contiene i dataset statici e grezzi scaricati dalle fonti API originali (ISTAT e ISTAT SITUAS).
* `01_Data/Clean_Data/`: Contiene il file `istat_incidenti_pulito_2019_2023.csv`, ovvero il dataset esplorato, sottoposto a JOIN, filtrato sul periodo di interesse e arricchito tramite feature engineering con nuove metriche aziendali.
* `02_Scripts_and_Notebooks/Scripts/`: Script Python strutturati per il fetch automatico dei dati.
* `02_Scripts_and_Notebooks/Notebooks/01_Data_Exploration_and_Cleaning.ipynb`: Notebook contenente il processo di data ingestion, unione, pulizia e arricchimento geografico.
* `02_Scripts_and_Notebooks/Notebooks/02_EDA_and_Visualizations.ipynb`: Analisi Esplorativa dei Dati (EDA) in risposta a domande mirate di business.
* `02_Scripts_and_Notebooks/Notebooks/03_Machine_Learning.ipynb`: Segmentazione avanzata del target tramite algoritmo di Clustering (K-Means) e previsioni future con Regressione Lineare (Forecasting).
* `03_Dashboards/PowerBI/`: File di Business Intelligence contenente la dashboard interattiva con l'esplorazione dei risultati.
* `04_Presentation/`: Slide di presentazione finale (pitching) rivolta al management aziendale.
* `requirements.txt`: Elenco delle dipendenze e delle librerie necessarie per l'ambiente virtuale.

## Istruzioni per l'uso
1. Clonare il repository sulla propria macchina locale.
2. Installare i pacchetti necessari all'interno del proprio ambiente Python eseguendo: `pip install -r requirements.txt`.
3. (Opzionale) Rieseguire gli script di download presenti in `02_Scripts_and_Notebooks/Scripts/` per aggiornare il repository dei dati RAW.
4. Eseguire in sequenza logica i Jupyter Notebook presenti in `02_Scripts_and_Notebooks/Notebooks/` per rigenerare i dati puliti e riprodurre i modelli di intelligenza artificiale.
5. Aprire il file dashboard `.pbix` con Power BI Desktop per esplorare visivamente lo storytelling dei risultati ricollegandolo ai file esportati in `Clean_Data`.

## Tecnologie usate
* **Python** (Librerie: *Pandas, Numpy* per la manipolazione dati e il data wrangling).
* **Scikit-Learn** (Algoritmi di Clustering e Regressione Lineare).
* **Matplotlib / Seaborn** (Data Visualization statistica).
* **Power BI** (Creazione filtri, dashboard interattive, storytelling visivo).
* **Git e GitHub** (Version Control e struttura del Workspace).
