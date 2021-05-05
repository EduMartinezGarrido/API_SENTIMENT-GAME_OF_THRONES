from config.configuration import collection


def insertafrase(date,season,episode,episodetitle, name, sentence):
    dict_insert = {"Release Date": date,
    "Season": f"{season}",
    "Episode": episode,
    "Episode Title": episodetitle,
    "Name": name,
    "Sentence": sentence
    }
    collection.insert_one(dict_insert)