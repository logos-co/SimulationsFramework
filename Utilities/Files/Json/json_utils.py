# Python Imports
import json
import jsonschema


def read_json(file_path):
    with open(file_path, "r") as file:
        json_content = json.load(file)

    return json_content


def validate_json(json_content, json_schema):
    jsonschema.validate(instance=json_content, schema=json_schema)

