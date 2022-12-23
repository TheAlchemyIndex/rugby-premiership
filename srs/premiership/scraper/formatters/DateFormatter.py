import datetime
import re
from srs.premiership.constants import OriginalColumns

# Constant val for replacing br tags with custom string
BR_REPLACE = "xXx"


def date_formatter(date_data, url):
    """Takes date information, reformats it and returns it in a key: value dictionary format.

    :param date_data: Date information about a match
    :param url: Url that the match data has been scraped from - for using to get the season
    :return: A key: value dictionary containing the date, time, hour, day, month, year and season of a match
    """
    # Removes any brackets and characters in between if found in the date
    date_data = re.sub("\[(.*?)\]", "", date_data, flags=re.DOTALL).strip()
    date_split = date_data.split(BR_REPLACE)

    # Some dates in 2020 are missing the year value, so this is appended if found using try except
    try:
        date = datetime.datetime.strptime(date_split[0], '%d %B %Y').strftime('%d/%b/%Y')
    except ValueError:
        date = datetime.datetime.strptime(date_split[0], '%d %B').strftime('%d/%b/') + "2020"

    time = date_split[1].replace(".", ":")

    # Reformats the time
    if date_split[1].find("pm") != -1:
        time = datetime.datetime.strptime(time, '%I:%M%p').strftime('%H:%M')

    hour = time.split(":")[0]
    day = datetime.datetime.strptime(date, '%d/%b/%Y').strftime('%a')
    month = datetime.datetime.strptime(date, '%d/%b/%Y').strftime('%b')
    year = datetime.datetime.strptime(date, '%d/%b/%Y').strftime('%Y')

    # Extracts season info from url of match details
    season = re.search("[0-9][0-9][0-9][0-9]-[0-9][0-9]", url).group()

    formatted_date = {OriginalColumns.DATE: date, OriginalColumns.TIME: time, OriginalColumns.HOUR: hour,
                      OriginalColumns.DAY: day, OriginalColumns.MONTH: month, OriginalColumns.YEAR: year,
                      OriginalColumns.SEASON: season}
    return formatted_date
