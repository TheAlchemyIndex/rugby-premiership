from srs.premiership.main.wikipedia.constants import StringSplitter
from srs.premiership.main.wikipedia.constants.columns import OriginalColumns
from srs.premiership.main.wikipedia.scraper.formatters.dateFormatter.util.CleanDate import clean_date
from srs.premiership.main.wikipedia.scraper.formatters.dateFormatter.util.ExtractDateTime import extract_date_time
from srs.premiership.main.wikipedia.scraper.formatters.dateFormatter.util.FormatDate import format_date
from srs.premiership.main.wikipedia.scraper.formatters.dateFormatter.util.FormatTime import format_time
from srs.premiership.main.wikipedia.scraper.formatters.dateFormatter.util.SplitDateTimeComponents import \
    split_date_time_components


def date_formatter(date_data, url):
    """Takes date information, reformats it and returns it in a key: value dictionary format.

    :param date_data: Date information about a match
    :param url: Url that the match data has been scraped from - for using to get the season
    :return: A key: value dictionary containing the date, time, hour, day, month, year and season of a match
    """
    # Removes any brackets and characters in between if found in the date string
    date_cleaned: str = clean_date(date_data)

    # Creates a List[str] of the date and time of a match
    date_time_split: list[str] = extract_date_time(date_cleaned, StringSplitter.BR_REPLACE)

    # Reformats the date
    date: str = format_date(date_time_split[0])

    # Reformats the time
    time: str = format_time(date_time_split[1])

    # Extracts individual components from date and time of match
    date_time_components: list[str] = split_date_time_components(date, time, url)

    hour: str = date_time_components[0]
    day: str = date_time_components[1]
    month: str = date_time_components[2]
    year: str = date_time_components[3]
    season: str = date_time_components[4]

    formatted_date: dict[str, str] = {OriginalColumns.DATE: date,
                                      OriginalColumns.TIME: time,
                                      OriginalColumns.HOUR: hour,
                                      OriginalColumns.DAY: day,
                                      OriginalColumns.MONTH: month,
                                      OriginalColumns.YEAR: year,
                                      OriginalColumns.SEASON: season}

    return formatted_date
