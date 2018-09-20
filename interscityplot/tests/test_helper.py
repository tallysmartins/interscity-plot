import shutil
import os.path as path

fixtures_dir = path.abspath(path.dirname(__file__) + '/fixtures') 

def delete_folder(path):
    shutil.rmtree(path)
