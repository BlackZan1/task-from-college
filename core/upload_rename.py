from uuid import uuid4
import os

def upload_rename(path):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]

        filename = '{}.{}'.format(uuid4().hex, ext)

        return os.path.join(path, filename)

    return wrapper