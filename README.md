# Sentiment Analysis - Game of Thrones

![image](https://qph.fs.quoracdn.net/main-qimg-7e40a587fbc65fa697d4311d39586176)









## Table of Contents
1. [Información general](#Informacion-general)
2. [Datos](#Datos)
3. [Tecnologías](#Tecnologías)
4. [Librerías](#Librerías)
## Información general
***
Tareas a desarrollar en este proyecto:


- Crear una API con Flask usando los métodos GET y POST.
```
GET:

* Nombre de todos los personajes
    (/name) --> Devuelve un json de todos los nombres

* Frases según el personaje que selecciones
    (/frases/<name>) --> (/frases/jon snow)

* Frases según la temporada y personaje
    (/frases/<season>/<name>) --> (/frases/Season 3/jon snow)

* Devuelve la base de datos completa
    (/basedatos) --> Devuelve un json con el dataset completo

POST:

* Para introducir nuevos personajes, frases, temporadas, capitulos y nombre del capitulo
    (/nuevafrase) -->  {'Season': "Season 1",
                        'Episode': "Episode 1",
                        'Episode Title': 'Winter is Coming',
                        'Name': 'Edu Martinez',
                        'Sentence': 'A Martinez always pays his debts'}
```
```
- Realizar un Sentiment Analysis de las frases dichas en la serie Game of Thrones.

![image](https://github.com/EduMartinezGarrido/API_SENTIMENT-GAME_OF_THRONES/blob/main/images/personaje.png)
```
## Datos
***
Los datos que usamos vienen de un dataset descargado en Kaggle.

Data processing:
- Cargar datos en Mongo DB
- Llamadas API
- Sentiment Analysis de la API

## Tecnologias
***
Una lista de las librerías utilizadas en elproyecto:
* [Jupyter Notebook](https://jupyter.org/) : Version 6.1.4
* [Python](https://www.python.org/): Version 3.8.5
* [Visual Studio Code](https://code.visualstudio.com/)
## Librerías
***
Una pequeña introducción a las librerías usadas: 
```
import pandas as pd
from pymongo import MongoClient
import requests
import re
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from textblob import TextBlob
import spacy
from spacy import displacy
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
```
