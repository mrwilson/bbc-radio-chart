from bs4 import BeautifulSoup

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

def row_to_entry(row):
    rows = row.find_all("td")
    return {
        "position": int(rows[0].text),
        "movement": calculate_movement(rows[1].text),
        "previous_position": previous_position(rows),
        "weeks": int(rows[3].text),
        "artist": rows[4].text,
        "title": rows[5].text
    }

def to_entries(content):
    soup = BeautifulSoup(content, "xml")
    return [ row_to_entry(row) for row in soup.find_all("tr") if not "Position" in row.text ]