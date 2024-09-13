import requests
from bs4 import BeautifulSoup
from datetime import datetime as dt

class JWScrapper:
    def __init__(self, language: str = "es"):
        self.domain = "https://www.jw.org"
        self.language = language

    @classmethod
    def get_ministry_guides_by_year(cls, year: str = dt.now().year):
        '''
        Obtener guias de actividades del año
        '''
        
        # URL del sitio web
        url = f'{cls.domain}/{cls.language}/biblioteca/guia-actividades-reunion-testigos-jehova/'
        
        # Realizar la solicitud HTTP
        response = requests.get(url)
        
        # Parsear el contenido HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Usar el selector CSS para encontrar los elementos H1
        h3_elements = soup.select('#pubsViewResults > div > div.syn-body.publication > div.publicationDesc > h3 > a')
        
        # Imprimir el texto de cada elemento H1
        for h3 in h3_elements:
            print(h3.get('href'))
    
    @classmethod
    def get_ministry_guides_by_month(cls, months: str):
        '''
        Obtener los programas de las reuniones del mes
        '''
        
        # URL del sitio web
        url = f'{cls.domain}/{cls.language}/biblioteca/guia-actividades-reunion-testigos-jehova/enero-febrero-2025-mwb/'
        
        # Realizar la solicitud HTTP
        response = requests.get(url)
        
        # Parsear el contenido HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Usar el selector CSS para encontrar los elementos H1
        h3_elements = soup.select('#article > div.toc.cms-clearfix > div > div > h2 > a')
        
        # Imprimir el texto de cada elemento H1
        for h3 in h3_elements:
            print(h3.get('href'))

    @classmethod
    def get_ministry_guide_titles(cls, month_period: str,  week: str):
        '''
        Obtener titulos de la reunion
        '''
        
        # URL del sitio web
        url = f'{cls.domain}/{cls.language}/biblioteca/guia-actividades-reunion-testigos-jehova/septiembre-octubre-2024-mwb/Vida-y-Ministerio-Cristianos-2-a-8-de-septiembre-de-2024/'
        
        # Realizar la solicitud HTTP
        response = requests.get(url)
        
        # Parsear el contenido HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Usar el selector CSS para encontrar los elementos H1
        h1_elements = soup.select('#article > div.docSubContent > div > div.contentBody > div > div > div > h3')
        
        # Imprimir el texto de cada elemento H1
        for h1 in h1_elements:
            print(h1.get_text())
