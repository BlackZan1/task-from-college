def wrapper(instance, filename):
    ext = filename.split('.')[-1]

    filename = '{}.{}'.format(uuid4().hex, ext)

    return os.path.join(path, filename)

def upload_rename(path):
    return wrapper