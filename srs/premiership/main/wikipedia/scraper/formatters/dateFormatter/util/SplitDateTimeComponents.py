import datetime
import re


def split_date_time_components(date: str, time: str, url: str) -> list[str]:
    """Splits hour, day, month, year and season components from a date, time and season url

    :rtype: list[str]
    :param date: Date of match to be split
    :param time: Time of match to extract hour information from
    :param url: Url of season data
    :return: A set of string values representing each date and time component
    """
    try:
        hour: str = time.split(":")[0]
        day: str = datetime.datetime.strptime(date, '%d/%b/%Y').strftime('%a')
        month: str = datetime.datetime.strptime(date, '%d/%b/%Y').strftime('%b')
        year: str = datetime.datetime.strptime(date, '%d/%b/%Y').strftime('%Y')
    except ValueError:
        hour: str = "N/A"
        day: str = "N/A"
        month: str = "N/A"
        year: str = "N/A"

    # Extracts season info from url of match details
    try:
        season: str = re.search("[0-9][0-9][0-9][0-9]-[0-9][0-9]", url).group()
    except AttributeError:
        season: str = "N/A"

    return [hour, day, month, year, season]
