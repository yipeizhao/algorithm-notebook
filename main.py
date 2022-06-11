import json
from datetime import datetime

class Notebook:
    def __init__(self):
        with open('records.json') as f:
            self.records = json.load(f)
        f.close()
        self.id_no = len(self.records)+1
        
        with open('algos.json') as f:
            self.algos = json.load(f)
        f.close()
    # Load an algorithm
    # para:
    # name, str. Algorithm name
    # return:
    # res, json. Loading the entry
    def load(self,name):
        return 0

    # Create a new algorithm
    # para:
    # algo_name, json. Json file of algorithm
    # time, python time object. Current time
    # description, str. Description of the algorithm
    # return:
    # bool, successfully added or not
    def create(self, algo_name, time = datetime.now().strftime("%d/%m/%Y %H:%M:%S"), description=""):
        # Create algo json
        if algo_name not in [item['name'] for item in self.records['records']]:
            x = {'id':self.id_no,
                 'name':algo_name,
                 'last_edited_time':time,
                 'description':description,
                 'example':[],
                 'function':[]
                }
            write_json(x,'algos.json')
            write_json({"id":self.id_no,"name":algo_name},'records.json')
            # Increase id by 1
            self.id_no += 1
            return True
        else:
            return False
    

    # Edit an algorithm
    # para:
    # algo_name, str. Current algorithm name.
    # attribute, str. The attribute to be changed
    # content, str. Replacing the old content of the attribute
    # return:
    # Bool, successfully changed or not
    def edit(self,algo_name,attribute,content):
        return 0

    # Add example record to an entry
    # para:
    # example_jason, json of the example
    # return:
    # bool, successful added or not
    def add_example(self,example_json):
        return 0

    # Add a function to exsist algorithm
    # para:
    # algo_name, str. Name of the algorithm
    # file_path, str. Directory of the file
    # return:
    # bool, wether the function is added or not
    def add_function(self,alg_name,file_path):
        return 0
    # Delete an algorithm
    # para:
    # algo_name, str. Algorithm name
    # return:
    # Bool, Successfully deleted or not
    def delete(self,algo_name):
        return 0

    # Serach an algorithm
    # para:
    # algo_name
    # return:
    # list of strings. List of results
    def search(self,algo_name):
        return 0

    # Display info
    # para: algo_name,str
    # return:
    # void
    def display(self,algo,name):
        return 0
    
# function to add to JSON
def write_json(new_data, filename):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data[list(file_data.keys())[0]].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)