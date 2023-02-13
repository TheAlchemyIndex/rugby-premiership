import re


def clean_date(unclean_date_string):
    """Takes a date string and removes bracket based characters.

    :param unclean_date_string: A date string that may contain bracket based characters.
    :return: The date string cleaned by removing bracket based characters
    """
    try:
        return re.sub("\[(.*?)\]", "", unclean_date_string, flags=re.DOTALL).strip()
    except TypeError:
        return "N/A"
