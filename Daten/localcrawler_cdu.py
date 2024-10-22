from bs4 import BeautifulSoup

soup = BeautifulSoup("Parteiprogramme/epub-ordner/HTML/CDUCSU/index_split_000.html  ", "html.parser")

print(soup.prettify())