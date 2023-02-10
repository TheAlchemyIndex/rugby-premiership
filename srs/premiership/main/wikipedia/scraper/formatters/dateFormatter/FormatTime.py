import datetime


def format_time(unformatted_time: str) -> str:
    """Takes a time and returns it in %H:%M format.

    :rtype: str
    :param unformatted_time: Original time to be reformatted
    :return: New time in %H:%M format
    """
    time = unformatted_time.replace(".", ":")

    try:
        if (time.find("pm") != -1) or (time.find("am") != -1):
            if len(time.split(":")[0]) == 1:
                time = datetime.datetime.strptime(time, '%I:%M%p').strftime('%H:%M')
            else:
                time = datetime.datetime.strptime(time, '%H:%M%p').strftime('%H:%M')
        else:
            if len(time.split(":")[0]) == 1:
                time = datetime.datetime.strptime(time, '%I:%M').strftime('%H:%M')
            else:
                time = datetime.datetime.strptime(time, '%H:%M').strftime('%H:%M')
    except ValueError:
        time = "N/A"

    return time
