import urllib.request
import tempfile

GRADE_URL = 'https://www.ics.uci.edu/~pattis/ICS-33/ics33win22grades.zip'

def download_grades() -> str:
    request = urllib.request.Request(GRADE_URL)
    response = urllib.request.urlopen(request)
    grades = response.read()
    response.close()
    temp_file = tempfile.NamedTemporaryFile(mode='wb')
    with temp_file as f:
        f.write(grades)
        return temp_file.name


if __name__ == '__main__':
    print(download_grades())