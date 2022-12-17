# Function for looping through tags in divs and extracting data
def tag_extractor(divs):

    match_data = []

    for tag in divs:
        tables = tag.find_all("table")
        for table_tag in tables:
            table_tds = table_tag.find_all("td")
            for td in table_tds:
                # Ignoring text that is not required
                if (td.text != "") & (td.text.find("Report") == -1) & (td.text.find("Try") == -1) \
                        & (td.text.find("Pen") == -1) & (td.text.find("Drop") == -1) \
                        & (td.text.find("Con") == -1) & (td.text.find("[1]") == -1):
                    match_data.append(td.text)

    return match_data
