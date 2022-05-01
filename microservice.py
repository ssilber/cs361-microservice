import json

import requests

from common import (
    ENDPOINT,
    MICROSERVICE_FILEPATH,
    MICROSERVICE_START_TEXT,
    read_file,
    write_num_to_file,
)


def main():
    line = read_file(filepath=MICROSERVICE_FILEPATH)
    if line == MICROSERVICE_START_TEXT:
        r = requests.get(ENDPOINT)
        json_blob = r.json()
        num_objects = len(json_blob)
        write_num_to_file(filepath=MICROSERVICE_FILEPATH, num=str(num_objects))


if __name__ == "__main__":
    main()
