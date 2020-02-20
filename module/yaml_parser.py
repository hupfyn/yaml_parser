import yaml

file = None


def load_file(file_path):
    global file
    print(file_path)
    with open(file_path, 'r') as stream:
        try:
            file = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)


def parse_section(section, file_path=None):
    if not file:
        file_path = file_path or "test.yaml"
        load_file(file_path)
    return file[section]
