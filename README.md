# LexiMent-Network

A continuación, se presenta el contenido generado en el proyecto

Archivos con "V2" en el nombre: Estos archivos contienen el léxico modificado después de la traducción manual de algunas palabras del léxico original en inglés al español. Esto se hizo para lograr una traducción más contextual.

Carpeta "Complementos": Contiene varios archivos relacionados con el proyecto, aunque no influyen directamente en la generación de gráficos. Aquí se encuentran archivos de texto que incluyen listas de palabras en inglés junto con sus emociones asociadas, en ambos formatos: el original y el utilizado en el proyecto. También, hay dos archivos .csv: uno contiene información de 'Palabra/Polaridad' y otro de 'Palabra/Tipo de palabra', extraídos de los Tweets utilizados en el proyecto.

Archivos específicos:
emotion_dictionary_functions.py: Este archivo contiene funciones auxiliares para generar el diccionario de palabras del proyecto. Lee "Spanish-NRC-Emolex-V2.txt," con 14,000+ palabras en inglés y sus emociones traducidas al español. Luego, crea "Dic-Spanish-NRC-V2.txt" con palabras en español y al menos una emoción relacionada.

LexiMent.py: Este archivo alberga las funciones principales del proyecto, lo que permite usar el diccionario de palabras junto con sus emociones y obtener información variada. Esto incluye la identificación de emociones en una oración, la polaridad de una palabra o conjunto de palabras, y la creación de los archivos .csv mencionados previamente.

Tweets.xlsx: Se trata de un archivo de Excel donde cada fila corresponde a un Tweet relacionado con el tema de investigación.

Nodos_Finales.csv y Relaciones_Finales.csv: Estos archivos contienen todos los nodos y relaciones finales del gráfico resultante del algoritmo de Louvain, junto con su polaridad y la cantidad de veces que aparecieron en el total de Tweets.

LexiMent Network.ipynb: Este es el Jupyter Notebook principal del proyecto, el cual lee los Tweets, los analiza y genera varios tipos de gráficos. Esto incluye la Rosa de Plutchik para visualizar las emociones presentes en los Tweets, así como diversos tipos de gráficos para observar las relaciones entre las palabras y su polaridad.

LexiMent Network (ext).ipynb: Versión “extendida” de Jupyter Notebook principal. Ofrece una visualización más detallada de cada etapa del proyecto. al incluir tanto los gráficos "finales" como los gráficos "intermedios".


Referencias:

Stella, M. (2020). Text-mining forma mentis networks reconstruct public perception of the STEM gender gap in social media. PeerJ Computer Science, 6, e295.

Semeraro, A., Vilella, S., & Ruffo, G. (2021). PyPlutchik: Visualising and comparing emotion-annotated corpora. Plos one, 16(9), e0256503.
