import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'


def filter_numeric_scores(df):
    """Filter non-numeric values from the score columns.

    :param df: The dataframe the filter will be performed on
    :return: A filtered dataframe with numeric values in the score columns
    """
    numeric_scores_df = df.loc[(df['team1Score'] != 'Cancelled')
                               & (df['team1Score'] != 'Postponed')
                               & (df['team1Score'] != 'Upcoming')]

    numeric_columns = ['team1Score', 'team2Score', 'totalScore']

    for column in numeric_columns:
        numeric_scores_df[column] = pd.to_numeric(numeric_scores_df[column]).astype('int')

    return numeric_scores_df


def filter_upcoming_fixtures(df):
    """Filter all values from the score columns apart from 'Upcoming'.

    :param df: The dataframe the filter will be performed on
    :return: A filtered dataframe with values equaling 'Upcoming' in the score columns
    """
    upcoming_fixtures_df = df.loc[df['team1Score'] == 'Upcoming']
    return upcoming_fixtures_df
