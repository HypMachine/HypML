from yaml import safe_load
from jsonschema import validate, FormatChecker
from os.path import dirname, join

def load(path, ignore_validation=False):

    with open(path, 'r') as file:
        document = safe_load(file)
    
    module_path = dirname(__file__)
    with open(join(module_path, 'hypml.schema'), 'r') as file:
        schema = safe_load(file)
    
    try:
        validate(document, 
                 schema, 
                 format_checker = FormatChecker())
        return document
    except Exception as e:
        raise Exception(e)
        if ignore_validation:
            return document
        