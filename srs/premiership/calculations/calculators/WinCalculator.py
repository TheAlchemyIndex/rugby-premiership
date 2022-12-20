import pandas as pd
from srs.premiership.calculations.helpers.ColumnHelper import win_percentage
from srs.premiership.constants import OriginalColumns, CalculatedColumns


def calc_win_percentage(df):
    """Calculate the win percentage of teams.

    :param df: The dataframe the calculation will be performed on
    :return: A dataframe containing columns for the win percentages of home and away teams
    """
    # By home team win percentage
    home_win_percentage = win_percentage(df, OriginalColumns.TEAM1_NAME, OriginalColumns.WINNER, "H",
                                         CalculatedColumns.HOME_WIN_PERCENTAGE)

    # By away team win percentage
    away_win_percentage = win_percentage(df, OriginalColumns.TEAM2_NAME, OriginalColumns.WINNER, "A",
                                         CalculatedColumns.AWAY_WIN_PERCENTAGE)

    # Merge with df and return new_df of values, rounded to 2 decimal places
    new_df = pd.merge(df, home_win_percentage, on=OriginalColumns.TEAM1_NAME, how="outer")
    new_df = pd.merge(new_df, away_win_percentage, on=OriginalColumns.TEAM2_NAME, how="outer")
    return new_df
