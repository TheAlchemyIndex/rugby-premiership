import datetime
import re
from rp.gallagher.constants import OriginalColumns

# Constant val for replacing br tags with custom string
BR_REPLACE = "xXx"


# Function for formatting date details
def date_formatter(match_data, url):
    match_data = re.sub("\[(.*?)\]", "", match_data, flags=re.DOTALL).strip()
    date_split = match_data.split(BR_REPLACE)

    try:
        date = datetime.datetime.strptime(date_split[0], '%d %B %Y').strftime('%d/%b/%Y')
    except ValueError:
        date = datetime.datetime.strptime(date_split[0], '%d %B').strftime('%d/%b/') + "2020"

    time = date_split[1].replace(".", ":")

    if date_split[1].find("pm") != -1:
        time = datetime.datetime.strptime(time, '%I:%M%p').strftime('%H:%M')

    month = datetime.datetime.strptime(date, '%d/%b/%Y').strftime('%b')
    year = datetime.datetime.strptime(date, '%d/%b/%Y').strftime('%Y')
    # Extracts season info from url of match details
    season = re.search("[0-9][0-9][0-9][0-9]-[0-9][0-9]", url).group()

    formatted_date = {OriginalColumns.DATE: date, OriginalColumns.TIME: time, OriginalColumns.MONTH: month,
                      OriginalColumns.YEAR: year, OriginalColumns.SEASON: season}

    return formatted_date
