import urllib.request
import tempfile
from pathlib import Path

GRADE_URL = 'https://www.ics.uci.edu/~pattis/ICS-33/ics33win22grades.zip'

def download_grades() -> Path:
    request = urllib.request.Request(GRADE_URL)
    response = urllib.request.urlopen(request)
    grades = response.read()
    response.close()
    grades_path = Path(tempfile.gettempdir())/'grades.zip'
    with open(grades_path, 'wb') as f:
        f.write(grades)
    return grades_path


if __name__ == '__main__':
    print(download_grades())