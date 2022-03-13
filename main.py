import requests
import tempfile
from pathlib import Path
import zipfile

GRADE_URL = 'https://www.ics.uci.edu/~pattis/ICS-33/ics33win22grades.zip'

def download_grades() -> Path:
    '''
    Downloads grades as a zipped file.
    Returns path to grades.
    '''
    grades = requests.get(GRADE_URL)
    grades_path = Path(tempfile.gettempdir())/'grades.zip'
    with open(grades_path, 'wb') as f:
        f.write(grades)
    return grades_path

def unzip_grades(path: Path) -> Path:
    '''
    Unzips grades.
    Returns path to xlsm grades file.
    '''
    file = zipfile.ZipFile(path)
    file.extractall(tempfile.gettempdir())
    return Path(path.parent/file.namelist()[0])

if __name__ == '__main__':
    zipped_grades = download_grades()
    print(unzip_grades(zipped_grades))