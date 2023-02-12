import datetime


def format_date(unformatted_date: str) -> str:
    """Takes a date and returns it in %d/%b/%Y format.

    :rtype: str
    :param unformatted_date: Original date to be reformatted
    :return: New date in %d/%b/%Y format
    """
    # Some dates in 2021 are missing the year value, so this is appended if found
    if unformatted_date == "19 June" or unformatted_date == "26 June":
        date = datetime.datetime.strptime(unformatted_date, '%d %B').strftime('%d/%b/') + "2021"
    else:
        try:
            date = datetime.datetime.strptime(unformatted_date, '%d %B %Y').strftime('%d/%b/%Y')
        except ValueError:
            date = "N/A"

    return date
