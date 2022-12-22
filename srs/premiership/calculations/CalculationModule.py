import pandas as pd

from srs.premiership.calculations.calculators.MeanCalculator import *
from srs.premiership.calculations.calculators.WinCalculator import calc_win_percentage
from srs.premiership.calculations.filters.ScoreFilter import filter_results


def create_calculated_columns(first_season_start, first_season_end, last_season_end):
    """Reads match data from season csv data, creates calculated columns and writes to new files.

    :param first_season_start: The starting 4 numbers of the first season to be scrapped and written to csv (e.g., 2010)
    :param first_season_end: The last 2 numbers of the first season to be scrapped and written to csv (e.g., 11)
    :param last_season_end: The last 2 numbers of the final season to be scrapped and written to csv (e.g., 23)
    """
    while first_season_end <= last_season_end:
        file_path = r"data/rawData/groupedSeasons/All Seasons - " + str(first_season_start) + "-" \
                    + str(last_season_end) + ".csv"

        # Creates df from file path
        df = pd.read_csv(file_path)
        df['date'] = pd.to_datetime(df["date"])

        # Filters to remove non-numeric data from scores and convert scores to numeric values
        df_filtered = filter_results(df)

        # Calculates means of scores
        df_calc_means = calc_means(df_filtered)

        # Calculates means of scores based on additional column
        df_calc_cond_means_two_cols = calc_conditional_means_two_cols(df_calc_means)

        # Calculates means of scores based on 2 additional columns
        df_calc_cond_means_three_cols = calc_conditional_means_three_cols(df_calc_cond_means_two_cols)

        # Calculates means of previous 5 scores
        df_calc_cond_means_three_cols.sort_values(by='date', inplace=True)

        # Columns for calculating the mean of the last 5 scores for and against the home team
        last_5_results_home_cols = [OriginalColumns.TEAM1_SCORE, OriginalColumns.TEAM2_SCORE]
        last_5_results_home_new_cols = [CalculatedColumns.AVG_HOME_LAST_5_SCORES,
                                        CalculatedColumns.AVG_HOME_LAST_5_SCORES_AGAINST]

        df_calc_last_5_results = df_calc_cond_means_three_cols.groupby(OriginalColumns.TEAM1_NAME).apply(lambda x: calc_rolling_5_scores_mean(x, last_5_results_home_cols, last_5_results_home_new_cols))
        df_calc_last_5_results = df_calc_last_5_results.droplevel(OriginalColumns.TEAM1_NAME)

        # Calculates means of previous 3 scores against each opponent
        df_calc_last_5_results.sort_values(by='date', inplace=True)
        df_calc_last_3_results_opponent = calc_previous_3_scores_mean_opposition(df_calc_last_5_results)

        # Calculates win percentage for each team
        df_calc_wins = calc_win_percentage(df_calc_last_3_results_opponent)

        # Writes season data to csv and increments first_season_end
        df_calc_wins.to_csv(
            "data/calculatedData/Results - " + str(first_season_start) + "-" + str(last_season_end) + ".csv")
        first_season_end += 1
