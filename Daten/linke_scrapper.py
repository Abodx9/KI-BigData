import os
from bs4 import BeautifulSoup
import csv

def linke_extractor(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    data = []
    current_title = ""
    paragraphs = []


    for p_tag in soup.find_all('p'):

        if p_tag.find('b'):

            if current_title and paragraphs:
                data.append({"title": current_title.strip(), "p": "\n\n".join(paragraphs).strip()})
                current_title = ""  
                paragraphs = []


            current_title += " " + p_tag.get_text(strip=True)

        else:

            paragraph_text = p_tag.get_text(strip=True)
            paragraphs.append(paragraph_text)


    if current_title and paragraphs:
        data.append({"title": current_title.strip(), "p": "\n\n".join(paragraphs).strip()})

    return data




#Die linke
folder_path = r"/Users/phuong/Documents/GitHub/KIAndBigData/KI-BigData/Parteiprogramme/epub-ordner/HTML/linke"
with open('linkedata.csv', 'a', newline='', encoding='utf-8') as csvfile:
  csv_writer = csv.writer(csvfile)
  csv_writer.writerow(['Titel', 'Paragraph'])
  print(folder_path)

  for filename in os.listdir(folder_path):

    if filename.endswith(".html"):  #htmlx bei gruenen
      file_path = os.path.join(folder_path, filename)
      extracted_data = linke_extractor(file_path)

      for item in extracted_data:
        title = item["title"]
        paragraph = item["p"]
        csv_writer.writerow([title, paragraph])
        print(f"Title: {item['title']}\nParagraph: {item['p']}\n---")