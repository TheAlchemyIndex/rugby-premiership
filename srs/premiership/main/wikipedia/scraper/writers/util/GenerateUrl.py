from srs.premiership.main.wikipedia.constants import Urls


def generate_url(season_start, season_end) -> str:
    """Generates a url to be scraped. If the season_start year is greater than or equal to the season_end year,
    an Exception is raised.

    :rtype: str
    :param season_start: Starting 4 digit year of target season (i.e., 2014)
    :param season_end: End 2 digit year of target season (i.e., 15)
    :return: Url to be scraped
    """
    if int(season_start[2:4]) >= int(season_end):
        raise Exception(f"Starting year of the season should not be greater than or equal to the end year of "
                        f"the season.\n"
                        f"The value of season_start was: {season_start}\n"
                        f"The value of season_end was: {season_end}")
    elif (int(season_end) - int(season_start[2:4])) > 1:
        raise Exception(f"The difference between the starting year of the season and the end year of the season "
                        f"should not be greater than 1 year.\n"
                        f"The value of season_start was: {season_start}\n"
                        f"The value of season_end was: {season_end}")
    else:
        return f"{Urls.PREMIERSHIP_URL_START}{str(season_start)}-{str(season_end)}{Urls.PREMIERSHIP_URL_END}"
