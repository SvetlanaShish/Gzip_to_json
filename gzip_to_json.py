import json
import sys
from gzip import open

path = sys.argv[1]
with open(path) as file:
    data = json.loads(file.read())
    for objs in data:
        for obj in objs['key1']:
            for obj2 in objs['key2']:
                file_name = '.'.join(filter(None, (obj['objId'], obj['version'])))
                if obj2 and file_name:
                    with open(f"{path}/jsonfiles/{file_name}.json", "w") as file_json:
                        file_json.write(json.dumps(obj2, separators=(',', ':')))
