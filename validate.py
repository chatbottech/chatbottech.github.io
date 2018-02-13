import logging
import os
import yaml
import traceback

logger = logging.getLogger(__name__)


FORMAT = '%(message)s'
logging.basicConfig(format=FORMAT)

class CheckException(Exception):
    pass


def get_yaml(open_file):
    content = ""
    count = 0
    for line in open_file:
        if line == '---\n':
            count += 1
            if count > 1:
                break
        else:
            content += line
    return content


def check(condition, file_path):
    if not condition:
        stack = traceback.extract_stack(limit=2)
        print("ERROR in", file_path)
        print(traceback.format_list(stack)[0])
    return condition


def validate():
    # traverse root directory, and list directories as dirs and files as files
    for root, dirs, files in os.walk("_reviews"):
        for file in files:
            if not file.endswith('.md'):
                continue
            file_path = os.path.join(root, file)
            print("Checking", file_path)
            with open(file_path) as open_file:
                doc = yaml.load(get_yaml(open_file))
                if check('position' in doc, file_path):
                    check(type(doc['position']) == int, file_path)
                check('logo' in doc, file_path)
                check('site' in doc, file_path)
                check('info' in doc, file_path)
                check('ratings' in doc, file_path)
                

if __name__ == "__main__":
    validate()
