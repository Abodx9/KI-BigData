import os
from bs4 import BeautifulSoup
import csv



def extractor(file_path):

  with open(file_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

  soup = BeautifulSoup(html_content, 'html.parser')

  data = []
  h3_tag = None
  p_tags = []

  for tag in soup.find_all(['h2', 'h3', 'p']):
    if tag.name == 'h2':
      h3_tag = None
      p_tags = []
    elif tag.name == 'h3':
      if h3_tag is not None:
        data.append({"title": h3_tag.get_text(strip=True), "p": "\n\n".join([p.get_text(strip=True) for p in p_tags])})
      
      h3_tag = tag
      p_tags = []
    elif tag.name == 'p':
      p_tags.append(tag)

  if h3_tag is not None:
    data.append({"title": h3_tag.get_text(strip=True), "p": "\n\n".join([p.get_text(strip=True) for p in p_tags])})

  return data


#Die gruenen
folder_path = r"/Users/phuong/Documents/GitHub/KIAndBigData/KI-BigData/Parteiprogramme/epub-ordner/HTML/gruene"
with open('gruenedata.csv', 'a', newline='', encoding='utf-8') as csvfile:
  csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
  csv_writer.writerow(['Titel', 'Paragraph'])
  print(folder_path)

  for filename in os.listdir(folder_path):

    if filename.endswith(".xhtml"):  #htmlx bei gruenen
      file_path = os.path.join(folder_path, filename)
      extracted_data = extractor(file_path)

      for item in extracted_data:
        title = item["title"].replace('\n', '').replace('\r', '').strip()
        paragraph = item["p"].replace('\n', '').replace('\r', '').strip()
        csv_writer.writerow([title, paragraph])
        print(f"Title: {item['title']}\nParagraph: {item['p']}\n---")




