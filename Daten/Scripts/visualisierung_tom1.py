import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import os
import matplotlib

# Matplotlib-Backend einstellen
matplotlib.use('TkAgg')

# Absoluter Pfad zu den Dateien
files_root = "/home/a/Documents/Uni/Semester5/ki_bigdata/Projekt/KI-BigData/Daten/fertige_Daten"
filepaths = [
    "AFD_Daten.csv",
    "cdu.csv",
    "FDP_Daten.csv",
    "freiewaehler_daten_cleaned.csv",
    "gruenedata.csv",
    "SPD.csv",
    "Linke_Daten.csv"
]

dataframes = []
for file in filepaths:
    file_path = os.path.join(files_root, file)
    if os.path.exists(file_path):
        try:
            # Lade Dateien, ignoriere fehlerhafte Zeilen
            df = pd.read_csv(file_path, names=["Titel", "Paragraph"], encoding="utf-8", on_bad_lines="skip")
            df['Quelle'] = os.path.splitext(file)[0]
            dataframes.append(df)
        except Exception as e:
            print(f"Fehler beim Verarbeiten der Datei {file}: {e}")
    else:
        print(f"Datei nicht gefunden: {file_path}")

# Prüfe, ob Daten erfolgreich geladen wurden
if dataframes:
    combined_df = pd.concat(dataframes, ignore_index=True)

    # Eigene Stopwörter definieren
    custom_stopwords = {"Freie Demokraten", "und", "oder", "aber", "dass", "wir", "sie", "mit", "von", "zu", "da", "die", "den", "al",
                        "Die", "eine", "auch", "bei der", "ein", "zum Beispiel", "ab", "sind", "der", "für", "das",
                        "um", "auf", "einem", "zur", "au", "haben", "seine", "um", "einer", "bei", "sowie", "de",
                        "diese", "machen", "wird", "ist", "wollen", "werden", "nicht", "müssen", "durch", "muss",
                        "als", "einen", "sich", "können", "sein", "ihre", "damit", "n", "im", "des", "aus", "un",
                        "dem", "über", "aus", "e", "es", "etwa", "er", "gibt", "bi", "ihrer", "anderen", "nutzen",
                        "viele", "noch", "andere", "wieder", "ihrer", "bi", "bereit", "neue", "wenn", "sollten",
                        "eines", "ihren", "beim", "allen", "hat", "aller", "ihnen", "bis", "stellen", "möglich",
                        "selbst", "Denn", "Unser", "großen", "sondern", "gilt", "braucht", "bereits", "darf", "dazu",
                        "ohne", "gelten", "zudem", "gerade", "unter", "dort", "insbesondere", "unsere", "uns", "dafür",
                        "dabei", "gegen", "gegenüber", "keine", "statt", "hier", "dies", "daher", "kein", "geht",
                        "nur", "innen", "diesen", "ermöglicht", "jede", "vor", "allem", "neben", "wurde", "weiter",
                        "indem", "sollte", "nach", "besonders", "dieser", "mindesten", "kommen", "deren", "setzen",
                        "oft", "vom", "denen", "ob", "vielen", "geben", "gehen", "ihr", "ebenso",
                        "sollen", "soll", "mehr", "Deshalb", "schaffen", "alle", "dürfen", "ermöglichen", "lehnen", "kann",
                        "zum", "deutlich", "Außerdem", "weitere", "immer", "gute", "unseren", "Teil", "wichtige", "bisher",
                        "ge", "treten", "große", "hin", "hohe"
                        }
    stopwords = STOPWORDS.union(custom_stopwords)

    # WordCloud erstellen
    all_text = " ".join(combined_df["Paragraph"].dropna())
    wordcloud = WordCloud(
        width=1000,
        height=1000,
        background_color="white",
        stopwords=stopwords
    ).generate(all_text)

    # WordCloud anzeigen
    plt.figure(figsize=(15, 15))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("WordCloud für alle Daten (ohne Füllwörter)")
    plt.show()

    # Kombinierte Daten speichern
    combined_df.to_csv(
        "/home/a/Documents/Uni/Semester5/ki_bigdata/Projekt/KI-BigData/Daten/fertige_Daten/kombinierte_daten.csv",
        index=False,
        encoding="utf-8"
    )
else:
    print("Keine Daten konnten geladen werden.")
