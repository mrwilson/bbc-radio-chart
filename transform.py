from bs4 import BeautifulSoup
from datetime import datetime

def calculate_movement(input):
    if input[0:2] == "UP":
        return int(input[2:])
    elif input[0:4] == "DOWN":
        return -int(input[4:])
    else:
        return 0

def previous_position(rows):
    if rows[1].text == "NEW":
        return 0
    else:
        return int(rows[2].text)

def row_to_entry(row, date):
    rows = row.find_all("td")
    entry = {
        "position": int(rows[0].text),
        "movement": calculate_movement(rows[1].text),
        "previous_position": previous_position(rows),
        "weeks": int(rows[3].text),
        "artist": rows[4].text,
        "title": rows[5].text
    }

    if date:
        entry['date'] = date

    return entry

def extract_date(soup):
    if soup.find('h1'):
        date = soup.find('h1')\
        .text\
        .replace("The Official UK Top 40 Singles Chart - ","")\
        .replace("st "," ")\
        .replace("th "," ")\
        .replace("nd "," ")\
        .replace("rd "," ")

        parsed = datetime.strptime(date, '%A %d %B')
        return parsed.replace(year=datetime.now().year)
    else:
        return None

def to_entries(content):
    soup = BeautifulSoup(content, "xml")
    date = extract_date(soup)

    return [ row_to_entry(row, date) for row in soup.find_all("tr") if not "Position" in row.text ]