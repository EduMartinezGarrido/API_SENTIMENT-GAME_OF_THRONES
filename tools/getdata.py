from config.configuration import db, collection


def personaje_names():
    """
    Funcion que devuelve los personajes
    """

    nombres = collection.distinct("Name")
    return nombres



def mensajespersonaje(personaje):
    """
    Funcion que devuelve la frase seleccionando el personaje que quieres.
    """

    query = {"Name":f"{personaje}"}
    frases = list(collection.find(query,{"_id":0}))
    return frases

def temporadas(temporada,personaje):
    """
    Funcion que devuelve las frases dichas en la temporada y del personaje seleccionado.
    """

    query1 = {"Season":f"{temporada}"}
    query = {"Name":f"{personaje}"}
    frases = list(collection.find({"$and": [query,query1]},{"_id":0}))
    return frases

def base_datos():
    """
    Funcion que devuelve toda la base de datos
    """
    query = {}
    proj = {"Release Date": 1, "Season": 1, "Episode": 1, "Episode Title": 1, "Name": 1, "Sentence": 1,"_id":0}
    basedatos = list(collection.find(query,proj))
    return basedatos