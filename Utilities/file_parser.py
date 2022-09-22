import json


class ConfigurationFileParser:

    def __init__(self, file_path):
        self._file_path = file_path

    def read_content(self):
        # Retrieve raw info
        data = self._parse_file()

        # Check valid flags depending on simulation ()
        print("asd")
        # Parse values

        return "data"

    def _parse_file(self):
        with open(self._file_path, "r") as file:
            data = json.load(file)

        return data
