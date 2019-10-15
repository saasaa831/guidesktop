import os, logging.config, json
import tarfile
import zipfile

def extract_zip(zip_file, to_directory):
    archive = zipfile.ZipFile(zip_file)
    archive.extractall(to_directory)
    return archive.namelist()


def extract_tar_file(tar_file, to_dir):
    try:
        tar = tarfile.open(tar_file.name, mode="r:gz")
    except tarfile.ReadError:
        tar = tarfile.open(tar_file.name, mode="r:bz2")
    members = tar.getmembers()
    tar.extractall(to_dir)
    tar.close()
    return members


def unpack(archive, to_directory=None):
    if not to_directory:
        to_directory = os.path.dirname(archive.name)
    if archive.endswith(".zip"):
        return extract_zip(archive, to_directory)
    else:
        file_list = extract_tar_file(archive, to_directory)
        return [x.name for x in file_list]

def setup_logging(default_path, default_level=logging.INFO, env_key='LOG_CFG'):
    """Setup logging configuration"""
    path = os.path.join(default_path, 'config', 'logging.json')
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)