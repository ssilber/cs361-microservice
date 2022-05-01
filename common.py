ENDPOINT = "http://0.0.0.0:5000/api/clubs"
MICROSERVICE_FILEPATH = "test.txt"
MICROSERVICE_START_TEXT = "GET"


def read_file(filepath: str) -> str:
    with open(filepath, "r") as f:
        line = f.readline()
        return line


def write_num_to_file(filepath: str, num: str):
    with open(filepath, "w") as f:
        f.write(num)
