# **AI-BigData**

Our Project for AI-BigData.

[Deutsch](Daten/Others/README-de.md)

## **Project Overview**

This repository contains the source code for our AI-BigData project. The project aims to collect, process, and analyze political party data using advanced techniques such as Vector Database and RAG (Retrieval-Augmented Generation).



# **Development History**

### **Party Data Collection**

- Downloaded data as PDF due to availability
- Converted PDFs to EPUB to remove images
- Converted EPUB files to HTML for easier parsing

### **Data Processing**

- Created HTML extractors for each party
- Developed PDF extractors due to challenging document structures
- Optimized PDF extractors based on font names and sizes
- Implemented manual processing where necessary

### **Vector Database Creation**

- Created Vector Database using chromaDB
- Populated Vector Database with our collected data
- Used GTR-T5 (Large) as the embeddings model
- Split long texts into manageable chunks
- Script to retrieve data from Vector Database

### **Refactoring and Optimization**
- Restructured code for better organization
- Improved data cleaning processes


## **Contributing**

Contributions are welcome! Please feel free to submit issues or pull requests.
