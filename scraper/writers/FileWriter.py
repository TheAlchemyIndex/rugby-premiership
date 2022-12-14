# Import libraries required
from scraper.writers.CsvWriter import write_to_csv
from scraper.results.SeasonScraper import scrape_results

# Constants for url value
URL_START = "https://en.wikipedia.org/wiki/"
URL_END = "_Premiership_Rugby"

# Constants for file names
DIRECTORY = "data/"
FILE_NAME_SINGLE_SEASONS_END = " Season.csv"
FILE_NAME_ALL_SEASONS_START = "All Seasons - "

# Constant for field names
FIELD_NAMES = ['date', 'time', 'team1Name', 'team1Score', 'team2Name', 'team2Score', 'venue',
               'referee', 'totalScore', 'winner', 'extraTime', 'month', 'year', 'season']


def write_to_individual_files(first_season_start, first_season_end, last_season_end):
    # Loop continues until last_season_end is reached
    while first_season_end <= last_season_end:
        url = URL_START + str(first_season_start) + "-" + str(first_season_end) + URL_END
        file_name = DIRECTORY + str(first_season_start) + "-" \
                                                        + str(first_season_end)\
                                                        + FILE_NAME_SINGLE_SEASONS_END

        # Calls write_to_csv and passes scrape_results function to it
        write_to_csv(scrape_results(url), file_name, FIELD_NAMES, "w")

        first_season_start += 1
        first_season_end += 1


def write_to_single_file(first_season_start, first_season_end, last_season_end):
    file_name = DIRECTORY + FILE_NAME_ALL_SEASONS_START + str(first_season_start)\
                                                        + "-" + str(last_season_end)\
                                                        + ".csv"

    # Flag to check if the first season in range has been written to file
    first_season = True

    # Loop continues until last_season_end is reached
    while first_season_end <= last_season_end:

        url = URL_START + str(first_season_start) + "-" + str(first_season_end) + URL_END

        # If the first season in range is being written, the existing file is overwritten
        if first_season:
            # Calls write_to_csv and passes scrape_results function to it
            write_to_csv(scrape_results(url), file_name, FIELD_NAMES, "w")

            first_season = False

            first_season_start = first_season_start + 1
            first_season_end = first_season_end + 1

        # Otherwise the existing file is appended with the second season results onwards
        else:
            # Calls write_to_csv and passes scrape_results function to it
            write_to_csv(scrape_results(url), file_name, FIELD_NAMES, "a")

            first_season_start = first_season_start + 1
            first_season_end = first_season_end + 1
