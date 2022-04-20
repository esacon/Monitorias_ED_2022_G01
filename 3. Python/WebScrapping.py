from bs4 import BeautifulSoup as soup
import requests

# Número de titulares
n = 20
URL = 'https://www.bbc.com/mundo/topics/c67q9nnn8z7t/page/'


def getTitulares(n : int=20):
    # URLs = ['{url}{index}'.format(url=URL, index=i) for i in range(1, round(n//10) + 1)]  
    URLs = [f'{URL}{i}' for i in range(1, round(n//10) + 1)]
    titulares = []
    for url in URLs:
        response = requests.get(url)
        page = soup(response.content, 'html.parser')
        titular_span_content = page.find_all('span', class_='lx-stream-post__header-text gs-u-align-middle')
        date_span_content = page.find_all('span', class_='qa-post-auto-meta')
        for (fecha_span, titular_span) in zip(date_span_content, titular_span_content):
            titulares.append({'fecha': fecha_span.text, 'titular': titular_span.text})
    print(f'Se recopilaron {len(titulares)} titulares.')

    return titulares

if __name__ == '__main__':
    getTitulares()