import shutil
import os.path as path

current_dir = path.dirname(__file__)
fixtures_dir = path.abspath(current_dir + '/fixtures') 

def delete_folder(path):
    shutil.rmtree(path)
