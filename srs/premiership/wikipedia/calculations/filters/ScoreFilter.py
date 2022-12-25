import pandas as pd
from srs.premiership.wikipedia.constants import OriginalColumns

pd.options.mode.chained_assignment = None  # default='warn'


def filter_results(df):
    """Returns a filtered dataframe containing results of matches that were not cancelled, postponed or upcoming.
    Also converts all score columns to numeric values and filters out results that went to extra time.

    :param df: The dataframe the filter will be performed on
    :return: A filtered dataframe of results that ended in normal time with scores in a numeric format
    """
    numeric_scores = filter_numeric_scores(df)
    normal_time_results = filter_normal_time_scores(numeric_scores)
    normal_time_results.drop(labels=OriginalColumns.EXTRA_TIME, axis='columns', inplace=True)
    return normal_time_results


def filter_numeric_scores(df):
    """Filter non-numeric values from the score columns.

    :param df: The dataframe the filter will be performed on
    :return: A filtered dataframe with numeric values in the score columns
    """
    numeric_scores_df = df.loc[(df[OriginalColumns.TEAM1_SCORE] != 'Cancelled')
                               & (df[OriginalColumns.TEAM1_SCORE] != 'Postponed')
                               & (df[OriginalColumns.TEAM1_SCORE] != 'Upcoming')]

    numeric_columns = [OriginalColumns.TEAM1_SCORE, OriginalColumns.TEAM2_SCORE, OriginalColumns.TOTAL_SCORE]
    for column in numeric_columns:
        numeric_scores_df[column] = pd.to_numeric(numeric_scores_df[column]).astype('int')
    return numeric_scores_df


def filter_normal_time_scores(df):
    """Filter results that went to extra time from the dataframe.

    :param df: The dataframe the filter will be performed on
    :return: A filtered dataframe with only results that ended in normal time
    """
    normal_time_scores_df = df.loc[df[OriginalColumns.EXTRA_TIME] != 'Y']
    return normal_time_scores_df


def filter_upcoming_fixtures(df):
    """Filter all values from the score columns apart from 'Upcoming'.

    :param df: The dataframe the filter will be performed on
    :return: A filtered dataframe with values equaling 'Upcoming' in the score columns
    """
    upcoming_fixtures_df = df.loc[df[OriginalColumns.TEAM1_SCORE] == 'Upcoming']
    return upcoming_fixtures_df
