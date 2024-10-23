import requests
from bs4 import BeautifulSoup

URL = "https://fmf.mx/noticias"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# Encuentra el contenedor que tiene los bloques de noticias
news_blocks = soup.find_all("div", class_="noticia_block")

for block in news_blocks:

    title_element = block.find("h2", attrs={"_ngcontent-sc53": True})
    title = title_element.text.strip() if title_element else "Título no encontrado"

    description_element = block.find("p", class_="desc")
    description = description_element.text.strip() if description_element else "Descripción no encontrada"
    
    date_element = block.find("p", class_="date")
    date = date_element.text.strip() if date_element else "Fecha no encontrada"

    link_element = block.find("a", href=True)
    link = "https://fmf.mx"  + link_element['href'] if link_element else "Enlace no encontrado"
    
    print(f"Título: {title}")
    print(f"Descripción: {description}")
    print(f"Fecha: {date}")
    print(f"Enlace: {link}")
    print("-" * 150)