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
                cleaned_b = [cleanUp(p.get_text(strip=True)) for p in p_tags]
                cleaned_b = [p for p in cleaned_b if p]
                data.append({"title": current_title, "p": "\n\n".join(cleaned_b)})
                p_tags = []

            cleaned_title = [cleanUp(tag.get_text(strip=True))]
            cleaned_title = [p for p in cleaned_title if p]
            current_title = cleaned_title

        else:
            p_tags.append(tag)

    if current_title and p_tags:
        cleaned_end = [cleanUp(p.get_text(strip=True)) for p in p_tags]
        cleaned_end = [p for p in cleaned_end if p]
        data.append({"title": current_title, "p": "\n\n".join(cleaned_end)})

    return data


def cleanUp(text):
    if text is None:
        return ""
    text = remove_numbers(text)
    #text = remove_seite(text)
    text = remove_dots(text)
    return text


def remove_seite(text):
    if "Seite" in text and text[5].isdigit():
        print("Seite" + text)
        return ''
    else:
        return text

def remove_dots(text):
    if "....." in text:
        print("...." + text)
        return ''
    else:
        return text


def remove_numbers(text):
    if not text.isdigit():
        index = len(text)
        while index > 0 and index > len(text) - 5 and (text[index - 1].isdigit() or text[index - 1] == '-'):
            index -= 1
            #print("index:"+text[index])
        #print(text)
        return text[:index]
    else:
        return ''


# cdu
folder_path = r"/home/a/Documents/Uni/Semester5/ki_bigdata/Projekt/KI-BigData/Parteiprogramme/epub-ordner/HTML/CDUCSU/"
with open('cdudata1.csv', 'a', newline='', encoding='utf-8') as csvfile:
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
                #print(f"Title: {item['title']}\nParagraph: {item['p']}\n---")
