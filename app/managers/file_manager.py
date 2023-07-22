import json


class FileManager:
    
    @classmethod
    def read_json_file(cls, path: str):
        with open(path, 'r') as file:
            return json.loads(file.read())
