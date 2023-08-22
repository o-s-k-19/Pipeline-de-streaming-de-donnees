import sys
import requests

from logger import logging
from exception import CustomException


def get_random_person_data(url: str) -> dict:
    """
    recupere des infos de personnes depuis l'API random user
    """
    try:
        response = requests.get(url)
        data = response.json()
        results = data["results"][0]
        logging.info(f"recupération des infos de {results['name']['title']}. {results['name']['first']}. {results['name']['last']} avec succes")
        return results
    except Exception as e:
        raise CustomException(e,sys)
    
def retrieve_best_format_data(data:dict)->dict:
    """
    format l'objet json de depart en un nouveau objet simplifié
    """
    retrived_data = {}
    retrived_data["full_name"] = f"{data['name']['title']}. {data['name']['first']} {data['name']['last']}"
    retrived_data["gender"] = data["gender"]
    retrived_data["location"] = f"{data['location']['street']['number']}, {data['location']['street']['name']}"
    retrived_data["city"] = data['location']['city']
    retrived_data["country"] = data['location']['country']
    retrived_data["postcode"] = data['location']['postcode']
    retrived_data["latitude"] = float(data['location']['coordinates']['latitude'])
    retrived_data["longitude"] = float(data['location']['coordinates']['longitude'])
    retrived_data["email"] = data["email"]

    return retrived_data