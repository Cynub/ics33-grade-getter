import requests
import tempfile
from pathlib import Path
import zipfile
from openpyxl import Workbook, load_workbook


GRADE_URL = 'https://www.ics.uci.edu/~pattis/ICS-33/ics33win22grades.zip'

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


if __name__ == '__main__':
    zipped_grades = download_grades()
    grades_path = unzip_grades(zipped_grades)
    print(get_row(grades_path, 901377)[27].value)