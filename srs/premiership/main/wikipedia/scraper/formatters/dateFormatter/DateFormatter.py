import datetime
import re

from srs.premiership.main.wikipedia.constants.columns import OriginalColumns
from srs.premiership.main.wikipedia.scraper.formatters.dateFormatter.ExtractDateTime import extract_date_time
from srs.premiership.main.wikipedia.scraper.formatters.dateFormatter.FormatDate import format_date
from srs.premiership.main.wikipedia.scraper.formatters.dateFormatter.FormatTime import format_time

# Constant val for replacing br tags with custom string
BR_REPLACE = "xXx"


def date_formatter(date_data, url):
    """Takes date information, reformats it and returns it in a key: value dictionary format.

    :param date_data: Date information about a match
    :param url: Url that the match data has been scraped from - for using to get the season
    :return: A key: value dictionary containing the date, time, hour, day, month, year and season of a match
    """
    # Creates a List[str] of the date and time of a match
    date_time_split: list[str] = extract_date_time(date_data, BR_REPLACE)

    # Reformats the date
    date: str = format_date(date_time_split[0])

    # Reformats the time
    time = format_time(date_time_split[1])

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
