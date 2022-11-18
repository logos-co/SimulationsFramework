# Python Imports
import json
import jsonschema


def read_json(file_path: str) -> dict:
    with open(file_path, "r") as file:
        json_content = json.load(file)

    return json_content


def write_json(info: dict, file_path: str):
    with open(file_path, "w") as file:
        json.dump(info, file)


def validate_json(json_content: dict, json_schema: dict):
    jsonschema.validate(instance=json_content, schema=json_schema)

