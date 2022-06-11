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
    # bool, successfully added or not
    def create(algo_name, time = datetime.now().strftime("%d/%m/%Y %H:%M:%S"), description):

        return 0

    # Edit an algorithm
    # para:
    # algo_name, str. Current algorithm name.
    # attribute, str. The attribute to be changed
    # content, str. Replacing the old content of the attribute
    # return:
    # Bool, successfully changed or not
    def edit(algo_name,attribute,content):
        return 0

    # Add example record to an entry
    # para:
    # example_jason, json of the example
    # return:
    # bool, successful added or not
    def add_example(example_json):
        return 0

    # Add a function to exsist algorithm
    # para:
    # algo_name, str. Name of the algorithm
    # file_path, str. Directory of the file
    # return:
    # bool, wether the function is added or not
    def add_function(alg_name,file_path):
        return 0
    # Delete an algorithm
    # para:
    # algo_name, str. Algorithm name
    # return:
    # Bool, Successfully deleted or not
    def delete(algo_name):
        return 0

    # Serach an algorithm
    # para:
    # algo_name
    # return:
    # list of strings. List of results
    def search(algo_name):
        return 0

    # Display info
    # para: algo_name,str
    # return:
    # void
    def display(algo,name):
        return 0

