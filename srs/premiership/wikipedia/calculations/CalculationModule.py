import numpy as np
import pandas as pd

from srs.premiership.wikipedia.calculations.calculators.MeanCalculator import calc_rolling_mean
from srs.premiership.wikipedia.calculations.filters.ColumnDropper import drop_columns
from srs.premiership.wikipedia.calculations.filters.ScoreFilter import filter_results
from srs.premiership.wikipedia.calculations.generators.CodeGenerator import generate_category_codes
from srs.premiership.wikipedia.calculations.generators.WonLastGenerator import generate_won_last
from srs.premiership.wikipedia.constants.columns import CalculatedColumns, OriginalColumns


def create_calculated_columns(first_season_start, first_season_end, last_season_end):
    """Reads match data from csv files, creates calculated columns and writes to new csv files.

    :param first_season_start: The starting 4 numbers of the first season to be used (e.g., 2010)
    :param first_season_end: The last 2 numbers of the first season to be used (e.g., 11)
    :param last_season_end: The last 2 numbers of the final season to be used (e.g., 23)
    """
    while first_season_end <= last_season_end:
        file_path = r"wikipedia/data/rawData/groupedSeasons/All Seasons - " + str(first_season_start) + "-" \
                    + str(last_season_end) + ".csv"

        # Creates df from file path and converts date column to datetime
        df = pd.read_csv(file_path)
        df[OriginalColumns.DATE] = pd.to_datetime(df[OriginalColumns.DATE])

        # Filters to remove non-numeric data from points and convert points to numeric values
        df_filtered = filter_results(df)

        # Columns for calculating mean of the points scored in the last 5 matches for and against for each team
        last_5_points_cols = [OriginalColumns.TEAM1_POINTS,
                              OriginalColumns.TEAM2_POINTS]
        last_5_points_new_cols = [CalculatedColumns.AVG_LAST_5_SCORES,
                                  CalculatedColumns.AVG_LAST_5_SCORES_AGAINST]

        # Calculates rolling mean of the points scored in the last 5 matches for and against for each team
        df_calc_last_5_points = df_filtered.groupby(OriginalColumns.TEAM1_NAME) \
            .apply(lambda x: calc_rolling_mean(x, last_5_points_cols, last_5_points_new_cols, 5))
        df_calc_last_5_points = df_calc_last_5_points.droplevel(OriginalColumns.TEAM1_NAME)

        # Columns for calculating the mean bps from the last 5 matches for and against each team
        last_5_bps_cols = [OriginalColumns.TEAM1_BPS,
                           OriginalColumns.TEAM2_BPS]
        last_5_bps_new_cols = [CalculatedColumns.AVG_LAST_5_BPS,
                               CalculatedColumns.AVG_LAST_5_BPS_AGAINST]

        # Calculates rolling mean of bps scored in the last 5 matches for and against for each team
        df_calc_last_5_bps = df_calc_last_5_points.groupby(OriginalColumns.TEAM1_NAME) \
            .apply(lambda x: calc_rolling_mean(x, last_5_bps_cols, last_5_bps_new_cols, 5))
        df_calc_last_5_bps = df_calc_last_5_bps.droplevel(OriginalColumns.TEAM1_NAME)

        # Columns for calculating the mean tries, cons, pens and dgs from the last 5 matches for and against each team
        last_5_scoring_cols = [OriginalColumns.TEAM1_TRIES,
                               OriginalColumns.TEAM1_CONVERSIONS,
                               OriginalColumns.TEAM1_PENALTIES,
                               OriginalColumns.TEAM1_DROP_GOALS,
                               OriginalColumns.TEAM2_TRIES,
                               OriginalColumns.TEAM2_CONVERSIONS,
                               OriginalColumns.TEAM2_PENALTIES,
                               OriginalColumns.TEAM2_DROP_GOALS]
        last_5_scoring_new_cols = [CalculatedColumns.AVG_LAST_5_TRIES,
                                   CalculatedColumns.AVG_LAST_5_CONVERSIONS,
                                   CalculatedColumns.AVG_LAST_5_PENALTIES,
                                   CalculatedColumns.AVG_LAST_5_DROP_GOALS,
                                   CalculatedColumns.AVG_LAST_5_TRIES_AGAINST,
                                   CalculatedColumns.AVG_LAST_5_CONVERSIONS_AGAINST,
                                   CalculatedColumns.AVG_LAST_5_PENALTIES_AGAINST,
                                   CalculatedColumns.AVG_LAST_5_DROP_GOALS_AGAINST]

        # Calculates rolling mean of tries, cons, pens and dgs scored in the last 5 matches for and against each team
        df_calc_last_5_scoring = df_calc_last_5_bps.groupby(OriginalColumns.TEAM1_NAME) \
            .apply(lambda x: calc_rolling_mean(x, last_5_scoring_cols, last_5_scoring_new_cols, 5))
        df_calc_last_5_scoring = df_calc_last_5_scoring.droplevel(OriginalColumns.TEAM1_NAME)

        # Generates numeric codes for key columns that contain strings
        df_codes = generate_category_codes(df_calc_last_5_scoring)

        # Creates column to show if team1 won their last game or not
        df_won_last_team1 = df_codes.groupby(OriginalColumns.TEAM1_NAME) \
            .apply(lambda x: generate_won_last(x, CalculatedColumns.TARGET_CODE, "wonLastTeam1"))
        df_won_last_team1 = df_won_last_team1.droplevel(OriginalColumns.TEAM1_NAME)

        # Creates column to show if team2 won their last game or not
        df_won_last_team2 = df_won_last_team1.groupby(OriginalColumns.TEAM2_NAME) \
            .apply(lambda x: generate_won_last(x, CalculatedColumns.TARGET_CODE, "wonLastTeam2"))
        df_won_last_team2 = df_won_last_team2.droplevel(OriginalColumns.TEAM2_NAME)
        df_won_last_team2["wonLastTeam2"] = np.where(df_won_last_team2["wonLastTeam2"] == 1, 0, 1)

        # Drops non-required columns
        df_dropped_columns = drop_columns(df_won_last_team2)

        # Sorts by date in ascending order
        df_dropped_columns.sort_values(by='date', inplace=True)

        # Writes season data to csv and increments first_season_end
        df_dropped_columns.to_csv("wikipedia/data/calculatedData/Calculated - " + str(first_season_start) + "-"
                        + str(last_season_end) + ".csv")
        first_season_end += 1
