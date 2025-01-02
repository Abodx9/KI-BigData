**AI-BigData**

Unser Projekt für AI-BigData.

[English](README.md)

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

