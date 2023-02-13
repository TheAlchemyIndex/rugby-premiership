import re


def clean_score(unclean_score_string):
    """Takes a score string and removes bracket based characters.

    :param unclean_score_string: A score string that may contain bracket based characters.
    :return: The score string cleaned by removing bracket based characters
    """
    try:
        return re.sub("\[(.*?)\]", "", unclean_score_string, flags=re.DOTALL).strip()
    except TypeError:
        return "N/A"
