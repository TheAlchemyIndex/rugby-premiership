import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'


def filter_numeric_scores(df):
    numeric_scores_df = df.loc[(df['team1Score'] != 'Cancelled')
                               & (df['team1Score'] != 'Postponed')
                               & (df['team1Score'] != 'Upcoming')]

    numeric_columns = ['team1Score', 'team2Score', 'totalScore']

    for column in numeric_columns:
        numeric_scores_df[column] = pd.to_numeric(numeric_scores_df[column]).astype('int')

    return numeric_scores_df


def filter_upcoming_fixtures(df):
    upcoming_fixtures_df = df.loc[df['team1Score'] == 'Upcoming']

    return upcoming_fixtures_df
