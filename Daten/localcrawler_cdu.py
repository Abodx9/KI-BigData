import os
from bs4 import BeautifulSoup
import csv


def extractor(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    data = []
    p_tags = []
    current_title = None

    for tag in soup.find_all('p'):
        if tag.find('b'):
            if current_title and p_tags:
                data.append({"title": current_title, "p": "\n\n".join([p.get_text(strip=True) for p in p_tags])})
                p_tags = []

            current_title = tag.get_text(strip=True)

        else:
            text = tag.get_text()
            if not text.isdigit():
                text = remove_numbers(text)
                p_tags.append(tag)

    if current_title and p_tags:
        data.append({"title": current_title, "p": "\n\n".join([p.get_text(strip=True) for p in p_tags])})

    return data


def remove_numbers(text):
    index = len(text)
    while index > 0 and index > len(text) - 5 and (text[index - 1].isdigit() or text[index - 1] == '-'):
        index -= 1
    return text[:index]


# cdu
folder_path = r"/home/a/Documents/Uni/Semester5/ki_bigdata/Projekt/KI-BigData/Parteiprogramme/epub-ordner/HTML/CDUCSU/"
with open('dcudata1.csv', 'a', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Titel', 'Paragraph'])
    print(folder_path)

    for filename in sorted(os.listdir(folder_path)):

        if filename.endswith(".html"):  # html bei cdu
            file_path = os.path.join(folder_path, filename)
            extracted_data = extractor(file_path)

            for item in extracted_data:
                title = item["title"]
                paragraph = item["p"]
                csv_writer.writerow([title, paragraph])
                print(f"Title: {item['title']}\nParagraph: {item['p']}\n---")
