import json
from datetime import datetime

class notebook:
    # Load an algorithm
    # para:
    # name, str. Algorithm name
    # return:
    # res, json. Loading the entry
    def load(name):
        return 0

    # Create a new algorithm
    # para:
    # algo_name, json. Json file of algorithm
    # time, python time object. Current time
    # description, str. Description of the algorithm
    # return:
    # void
    def create(algo_name, time = datetime.now().strftime("%d/%m/%Y %H:%M:%S"), description):
        return Null

    # Edit an algorithm
    # para:
    # algo_name, str. Current algorithm name.
    # attribute, str. The attribute to be changed
    # content, str. Replacing the old content of the attribute
    # return:
    # Bool, successfully changed or not
    def edit(algo_name,attribute,content):
        return Null

    # Delete an algorithm
    # para:
    # algo_name, str. Algorithm name
    # return:
    # Bool, Successfully deleted or not
    def delete(algo_name):
        return Null

    # Serach an algorithm
    # para:
    # algo_name
    # return:
    # list of strings. List of results
    def search(algo_name):
        return 0


