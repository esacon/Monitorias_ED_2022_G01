# Importar las librerías de NLP
import nltk 
import pandas as pd
import WebScrapping as scrapper
import re
import string 

# Descargar el paquete de palabras stop
nltk.download('stopwords')
stopwords = set(nltk.corpus.stopwords.words('spanish'))

# Stopwords en español.
# print(stopwords)

noticias = scrapper.getTitulares()[2:]

fechas = {
    "enero": "01",
    "febrero": "02",
    "marzo": "03",
    "abril": "04"
}

# Convertir archivo a Dataframe para facilitar el manejo de los datos.
df = pd.DataFrame(noticias)

def clean_titulares(columna):
    return df[columna].str.replace(r" +", " ", regex=True).str.replace(r"[%s]" % re.escape(string.punctuation), "", regex=True)

# Titulares sin espacios de más, y sin signos de puntuación ingleses.
df['titular'] = clean_titulares('titular')

for old, new in fechas.items():
    df['fecha'] = df['fecha'].str.replace(old, new, regex=True)

df['fecha'] = pd.to_datetime(df['fecha'], format='%H:%M %d %m %Y')

df['date'] = df['fecha'].dt.date
df['dia'] = df['fecha'].dt.day
df['month'] = df['fecha'].dt.month
df['year'] = df['fecha'].dt.year
print(df)

def dist_freq(df, n):
    """
    df: dataframe
    n = Top n de la lista.
    """
    # Concatenamos todos los titulares en un solo texto.
    # titular_text = ' '.join(df['titular'])
    titular_text = df['titular'].str.cat(sep=' ')

    # Separar palabras del texto por espacios.
    words = titular_text.split()

    # Filtramos las stopwords
    filtered_words = [word for word in words if word.lower() not in stopwords]

    # Devolvemos la distribución de frecuencia de esas palabras.
    return nltk.FreqDist(filtered_words).most_common(n)


print(dist_freq(df, 10))

def articulos_fecha(date=-1, dia=21, mes=-1, year=-1):
    if mes != -1:
        titulares_fecha = df[df['month'] == mes]
    elif dia != -1:
        titulares_fecha = df[df['dia'] == dia]
    elif year != -1:
        titulares_fecha = df[df['year'] == year]
    
    print()
    print(titulares_fecha)
    # Devolvemos una distribucion de frecuencias de esa fecha
    return dist_freq(titulares_fecha, 10)

print(articulos_fecha(dia=12))


