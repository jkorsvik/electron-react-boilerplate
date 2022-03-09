import requests
import shutil
import zipfile

FRENCHMODELURL = 'https://alphacephei.com/vosk/models/vosk-model-fr-0.22.zip'
RELATIVEMODELPATH = './backend/api/model/'


def download_file(url):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
    return local_filename

def unzip_file_to_modelfolder(filename):
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall(RELATIVEMODELPATH)
    print(f"Extracted {filename} to models folder")
    return filename

def download_unzip_french_model(): 
    local_filename = download_file(FRENCHMODELURL)
    print(f"Downloaded {local_filename}")
    return local_filename
    
    







    
    
    
