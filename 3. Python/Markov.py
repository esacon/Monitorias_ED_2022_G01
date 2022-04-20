from sqlalchemy import asc
import WebScrapping as scrapper
import pandas as pd
from matplotlib import pyplot as plt


"""
arreglo = [1, 2, 3 ,4 ,5]
# Para acceder a varios índices se puede recorrer de la siguiente forma:
# [inicio:(final-1):paso]

print(arreglo[:2])
# Los índices negativos sirven para recorrer en sentido inverso.

# Ejemplo: 
print(arreglo[-1:-4:-1])
"""


noticias = scrapper.getTitulares()

# Concatenar titulares en un solo texto
text = '. '.join([noticia['titular'] for noticia in noticias])
# Separar en palabras de cada titular.
words = text.split()
next_words = words[1:]
next_words.append('FIN')

df = pd.DataFrame({
    'words':words,
    'next_words':next_words
})

# Agrupar y sacar tabla de frecuencias
df_groupped = df.groupby(by=['words', 'next_words']).size().sort_values(ascending=False).reset_index(name='freq')
df_groupped['prob'] = df_groupped['freq']/len(df_groupped)

# Escoger índices
print(df_groupped[df_groupped['words'] == 'de'])

# Graficar
plt.plot(df_groupped['words'].head(10), df_groupped['freq'].head(10))
plt.show()

