import datetime
import re
from srs.premiership.main.wikipedia.constants.columns import OriginalColumns
from srs.premiership.main.wikipedia.scraper.formatters.dateFormatter.FormatDate import format_date

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

    # Reformats the date
    date = format_date(date_split[0])

    # Reformats the time
    time = date_split[1].replace(".", ":")
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
