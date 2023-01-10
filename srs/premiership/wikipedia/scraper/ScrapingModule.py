from srs.premiership.wikipedia.scraper.writers.FileWriter import write_to_individual_files,\
    write_to_single_file, write_recent_results


def write(write_type, first_season_start, first_season_end, last_season_end):
    """Writes match data to csv files.

    :param write_type: Determines whether data is written to individual files, a single file, or both
    :param first_season_start: The starting 4 numbers of the first season to be scrapped and written to csv (e.g., 2010)
    :param first_season_end: The last 2 numbers of the first season to be scrapped and written to csv (e.g., 11)
    :param last_season_end: The last 2 numbers of the final season to be scrapped and written to csv (e.g., 23)
    """
    if write_type == "single":
        # Creates individual files
        write_to_individual_files(first_season_start, first_season_end, last_season_end)
    elif write_type == "grouped":
        # Creates single file
        write_to_single_file(first_season_start, first_season_end, last_season_end)
    elif write_type == "both":
        # Creates individual files
        write_to_individual_files(first_season_start, first_season_end, last_season_end)
        # Creates single file
        write_to_single_file(first_season_start, first_season_end, last_season_end)
    elif write_type == "recent":
        # Writes only recent season data to file of previous seasons
        write_recent_results(first_season_start, last_season_end - 1, "20" + str(last_season_end - 1), last_season_end)
    else:
        print("No write type selected")
