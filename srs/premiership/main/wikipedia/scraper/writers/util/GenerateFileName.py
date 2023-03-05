from srs.premiership.main.wikipedia.constants import Directories


def generate_individual_file_name(season_start, season_end) -> str:
    """Generates file name for individual season csv files.

    :rtype: str
    :param season_start: Starting 4 digit year of target season (i.e., 2014)
    :param season_end: End 2 digit year of target season (i.e., 15)
    :return: File name for individual season csv file to be written to
    """
    # return Directories.INDIVIDUAL + str(season_start) + "-" + str(season_end) \
    #        + Directories.FILE_NAME_SINGLE_SEASONS_END

    return f"{Directories.INDIVIDUAL}{str(season_start)}-{str(season_end)}" \
           f"{Directories.FILE_NAME_SINGLE_SEASONS_END}"


def generate_grouped_file_name(first_season_start, last_season_end):
    """Generates file name for grouped season csv files.

    :param first_season_start: Starting 4 digit year of first target season (i.e., 2014)
    :param last_season_end: End 2 digit year of final target season (i.e., 23)
    :return: File name for grouped season csv file to be written to
    """
    return f"{Directories.GROUPED}{Directories.FILE_NAME_ALL_SEASONS_START}{str(first_season_start)}" \
           f"-{str(last_season_end)}.csv"
