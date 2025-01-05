**Ki-BigData**

Unser Projekt für KI - BigData.


## **Projektübersicht**

Dieses Repository enthält den Quellcode für unser AI-BigData-Projekt. Das Projekt zielt darauf ab, Daten von politischen Parteien zu sammeln, zu verarbeiten und zu analysieren, indem fortgeschrittene Techniken wie Vector Database und RAG (Retrieval-Augmented Generation) verwendet werden.



# **Entwicklungsgeschichte**

### **Parteiendatenerhebung**

- Herunterladen von Daten als PDF aufgrund der Verfügbarkeit
- Konvertierung von PDFs in EPUB, um Bilder zu entfernen
- Konvertierung der EPUB-Dateien in HTML zur einfacheren Analyse

### **Datenverarbeitung**

- Erstellung von HTML-Extraktoren für jede Partei
- Entwicklung von PDF-Extraktoren aufgrund der anspruchsvollen Dokumentenstruktur
- Optimierte PDF-Extraktoren auf der Grundlage von Schriftnamen und -größen
- Manuelle Verarbeitung, wo nötig, implementiert

## **Visualisierung von Daten**

- Erstellung von Diagrammen und Grafiken zur Visualisierung der Daten in % 
- Verwendung von Matplotlib, Seaborn und Wordcloud zur Erstellung von Diagrammen und Grafiken

- Wordcloud zur Visualisierung der häufigsten Wörter in den Parteiprogrammen (für Themen und Meinungen)
- Balkendiagramm zur Visualisierung der Wortlänge in den Parteiprogrammen (für Meinungen)
- Balkendiagramm zur Visualisierung der Sentimentanalyse in den Parteiprogrammen 
- Balkendiagramm zu Visualisierung der Häufigkeit von Schlüsselwörtern in den Themen von den Wahlprogrammen
- Heatmap zur Visualisierung der Häufigkeit von Schlüsselwörtern für Meinungen von den Wahlprogrammen

## **Erstellung-Vektorendatenbank**

- Erstellung der Vektordatenbank mit chromaDB
- Befüllung der Vektordatenbank mit unseren gesammelten Daten
- Verwendung von GTR-T5 (Large) als Modell für die Einbettung
- Aufteilung langer Texte in überschaubare Abschnitte
- Skript zum Abrufen von Daten aus der Vektordatenbank

## **Refaktorisierung und Optimierung**
- Umstrukturierung des Codes zur besseren Organisation
- Verbesserte Datenbereinigungsprozesse


## **Beiträge**

Beiträge sind willkommen! Bitte nicht zögern, Probleme oder Pull Requests einzureichen.

