import shutil

from srs.premiership.main.wikipedia.constants.columns import OriginalColumns
from srs.premiership.main.wikipedia.scraper.writers.CsvWriter import write_to_csv
from srs.premiership.main.wikipedia.scraper.seasons.SeasonScraper import scrape_results
from srs.premiership.main.wikipedia.scraper.writers.util.GenerateFileName import generate_individual_file_name, \
    generate_grouped_file_name
from srs.premiership.main.wikipedia.scraper.writers.util.GenerateUrl import generate_url

# Constant list for field names
FIELD_NAMES = [OriginalColumns.DATE,
               OriginalColumns.TIME,
               OriginalColumns.TEAM1_NAME,
               OriginalColumns.TEAM1_POINTS,
               OriginalColumns.TEAM2_NAME,
               OriginalColumns.TEAM2_POINTS,
               OriginalColumns.VENUE,
               OriginalColumns.TEAM_TYPE,
               OriginalColumns.REFEREE,
               OriginalColumns.TOTAL_POINTS,
               OriginalColumns.RESULT,
               OriginalColumns.EXTRA_TIME,
               OriginalColumns.HOUR,
               OriginalColumns.DAY,
               OriginalColumns.MONTH,
               OriginalColumns.YEAR,
               OriginalColumns.SEASON,
               OriginalColumns.TEAM1_BPS,
               OriginalColumns.TEAM2_BPS,
               OriginalColumns.TEAM1_TRIES,
               OriginalColumns.TEAM1_CONVERSIONS,
               OriginalColumns.TEAM1_PENALTIES,
               OriginalColumns.TEAM1_DROP_GOALS,
               OriginalColumns.TEAM2_TRIES,
               OriginalColumns.TEAM2_CONVERSIONS,
               OriginalColumns.TEAM2_PENALTIES,
               OriginalColumns.TEAM2_DROP_GOALS]


def write_to_individual_files(first_season_start, first_season_end, last_season_end):
    """Writes match data to individual csv files for each season.

    :param first_season_start: The starting 4 numbers of the first season to be scrapped and written to csv (e.g., 2010)
    :param first_season_end: The last 2 numbers of the first season to be scrapped and written to csv (e.g., 11)
    :param last_season_end: The last 2 numbers of the final season to be scrapped and written to csv (e.g., 23)
    """
    # Loop continues until last_season_end is reached
    while first_season_end <= last_season_end:
        url = generate_url(first_season_start, first_season_end)

        file_name = generate_individual_file_name(first_season_start, first_season_end)

        write_to_csv(scrape_results(url), file_name, FIELD_NAMES, "w")
        first_season_start += 1
        first_season_end += 1


def write_to_single_file(first_season_start, first_season_end, last_season_end):
    """Writes match data to a single csv file containing data for all seasons.

    :param first_season_start: The starting 4 numbers of the first season to be scrapped and written to csv (e.g., 2010)
    :param first_season_end: The last 2 numbers of the first season to be scrapped and written to csv (e.g., 11)
    :param last_season_end: The last 2 numbers of the final season to be scrapped and written to csv (e.g., 23)
    """
    file_name = generate_grouped_file_name(first_season_start, last_season_end)

    # Flag to check if the first season in range has been written to file
    first_season = True

    # Loop continues until last_season_end is reached
    while first_season_end <= last_season_end:
        url = generate_url(first_season_start, first_season_end)

        # If the first season in range is being written, the existing file is overwritten
        if first_season:
            write_to_csv(scrape_results(url), file_name, FIELD_NAMES, "w")
            first_season = False
            first_season_start = first_season_start + 1
            first_season_end = first_season_end + 1
        # Otherwise the existing file is appended with the second season results onwards
        else:
            write_to_csv(scrape_results(url), file_name, FIELD_NAMES, "a")
            first_season_start = first_season_start + 1
            first_season_end = first_season_end + 1


def write_recent_results(first_season_start, last_season_end, recent_season_start, recent_season_end):
    """Writes match data for current season and appends to file for previous seasons.

    :param first_season_start: The starting 4 numbers of the first season of data to be appended to (e.g., 2010)
    :param last_season_end: The last 2 numbers of the last season of data to be appended to (e.g., 22)
    :param recent_season_start: The first 2 numbers of the current season to be scrapped and appended to previous
                                seasons data (e.g., 22)
    :param recent_season_end: The last 2 numbers of the current season to be scrapped and appended to previous
                                seasons data (e.g., 23)
    """
    # File name of previous season data to be appended to
    old_file_name = generate_grouped_file_name(first_season_start, last_season_end)

    # New file name for previous season data and current season data
    new_file_name = generate_grouped_file_name(first_season_start, recent_season_end)

    # Creates copy of old_file_name and renames as new_file_name, so current season data can be appended to it
    shutil.copy(old_file_name, new_file_name)

    url = generate_url(recent_season_start, recent_season_end)

    write_to_csv(scrape_results(url), new_file_name, FIELD_NAMES, "a")
