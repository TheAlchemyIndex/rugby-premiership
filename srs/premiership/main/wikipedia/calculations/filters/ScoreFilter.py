import pandas as pd
from srs.premiership.main.wikipedia.constants.columns import OriginalColumns

pd.options.mode.chained_assignment = None  # default='warn'


def filter_results(df):
    """Returns a filtered dataframe containing results of matches that were not cancelled, postponed or upcoming.
    Also converts all points columns to numeric values and filters out results that went to extra time.

    :param df: The dataframe the filter will be performed on
    :return: A filtered dataframe of results that ended in normal time with points in a numeric format
    """
    numeric_points = filter_numeric_points(df)
    normal_time_results = filter_normal_time_results(numeric_points)
    normal_time_results.drop(labels=OriginalColumns.EXTRA_TIME, axis='columns', inplace=True)
    return normal_time_results


def filter_numeric_points(df):
    """Filter non-numeric values from the points columns.

    :param df: The dataframe the filter will be performed on
    :return: A filtered dataframe with numeric values in the points columns
    """
    numeric_points_df = df.loc[(df[OriginalColumns.TEAM1_POINTS] != 'Cancelled')
                               & (df[OriginalColumns.TEAM1_POINTS] != 'Postponed')
                               & (df[OriginalColumns.TEAM1_POINTS] != 'Upcoming')]

    numeric_columns = [OriginalColumns.TEAM1_POINTS, OriginalColumns.TEAM2_POINTS, OriginalColumns.TOTAL_POINTS]
    for column in numeric_columns:
        numeric_points_df[column] = pd.to_numeric(numeric_points_df[column]).astype('int')
    return numeric_points_df


def filter_normal_time_results(df):
    """Filter out results that went to extra time.

    :param df: The dataframe the filter will be performed on
    :return: A filtered dataframe with only results that ended in normal time
    """
    normal_time_results_df = df.loc[df[OriginalColumns.EXTRA_TIME] != 'Y']
    return normal_time_results_df


def filter_upcoming_fixtures(df):
    """Filter all values from the points columns apart from 'Upcoming'.

    :param df: The dataframe the filter will be performed on
    :return: A filtered dataframe with values equaling 'Upcoming' in the points columns
    """
    upcoming_fixtures_df = df.loc[df[OriginalColumns.TEAM1_POINTS] == 'Upcoming']
    return upcoming_fixtures_df
