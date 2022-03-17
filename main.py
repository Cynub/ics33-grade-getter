import requests
import tempfile
from pathlib import Path
import zipfile
from openpyxl import Workbook, load_workbook


GRADE_URL = 'https://www.ics.uci.edu/~pattis/ICS-33/ics33win22grades.zip'


def is_saved_id() -> bool:
    if (Path.cwd() / 'hash.txt').exists():
        return True
    return False


def save_hash_id(hash_id: str) -> None:
    with open('hash.txt', 'w') as f:
        f.write(hash_id)


def download_grades() -> Path:
    '''
    Downloads grades as a zipped file.
    Returns path to grades.
    '''
    grades = requests.get(GRADE_URL)
    grades_path = Path(tempfile.gettempdir())/'grades.zip'
    with open(grades_path, 'wb') as f:
        f.write(grades.content)
    return grades_path

def unzip_grades(path: Path) -> Path:
    '''
    Unzips grades.
    Returns path to xlsm grades file.
    '''
    file = zipfile.ZipFile(path)
    file.extractall(tempfile.gettempdir())
    return Path(path.parent/file.namelist()[0])


def get_row(path: Path, id: int) -> tuple:
    '''
    Given a path and an id, returns the
    row in the table matching the id.
    If not found, returns None.
    '''
    wb = load_workbook(filename = path, data_only=True)
    grade_sheet = wb.worksheets[0]
    for row in grade_sheet:
        if row[0].value == id:
            return row


def get_hash() -> str:
    if is_saved_id():
        with open('hash.txt', 'r') as f:
            return int(f.readline().strip('\n'))
    else:
        print('Please enter your hash id: ')
        hash_id = input()
        save_hash_id(hash_id)
        return int(hash_id)


if __name__ == '__main__':
    hash_id = get_hash()
    zipped_grades = download_grades()
    grades_path = unzip_grades(zipped_grades)
    print(get_row(grades_path, hash_id)[27].value)
    #901377