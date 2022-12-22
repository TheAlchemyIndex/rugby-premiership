from statistics import mean
import pandas as pd
import operator as op


def two_columns_mean(df, col1, col2, col_rename):
    """Calculate the mean based on 2 columns.

    :param df: The dataframe the calculation will be performed on
    :param col1: The column of values the dataframe will be grouped by
    :param col2: The column of values the mean will be calculated from
    :param col_rename: The name of the column that will contain the mean values
    :return: A dataframe containing the values of col1 and col_rename
    """
    avg_2_cols = df.groupby(col1)[col2].mean().reset_index().rename(columns={col2: col_rename})
    return avg_2_cols


def three_columns_mean(df, col1, col2, col3, col_rename):
    """Calculate the mean based on 3 columns.

    :param df: The dataframe the calculation will be performed on
    :param col1: The first column of values the dataframe will be grouped by
    :param col2: The second column of values the dataframe will be grouped by
    :param col3: The column of values the mean will be calculated from
    :param col_rename: The name of the column that will contain the mean values
    :return: A dataframe containing the values of col1, col2 and col_rename
    """
    avg_3_cols = df.groupby([col1, col2])[col3].mean().reset_index().rename(columns={col3: col_rename})
    return avg_3_cols


def mean_previous_5_scores(df, col1, col2, col_rename):
    """Calculate the mean of a team's previous 5 scores.

    :param df: The dataframe the calculation will be performed on
    :param col1: The column of values the dataframe will be filtered by
    :param col2: The column of values the mean will be calculated from
    :param col_rename: The name of the column that will contain the mean values
    :return: A dataframe containing the values of col1 and col_rename
    """

    # Sorts the dataframe by date, ascending
    df = df.sort_values(by='date', ascending=True)

    # Extracts unique team names from col1
    teams = sorted(df.drop_duplicates(subset=[col1])[col1].tolist())

    mean_last_5_scores = []

    for value in teams:
        # Adds team name to team_mean_scores list
        team_mean_scores = [value]
        filtered_df = df.loc[df[col1] == value]
        scores = filtered_df[col2].tolist()

        # If there is less than 5 scores, the mean is calculated on the available scores
        if len(scores) < 5:
            mean_scores = mean(scores)
        else:
            # Otherwise the mean is calculated using the last 5 values in scores list
            mean_scores = mean(scores[-5:])

        team_mean_scores.append(mean_scores)
        # mean_last_5_scores is appended with team_mean_scores, creating a list of lists
        mean_last_5_scores.append(team_mean_scores)

    # mean_last_5_scores is converted to a dataframe with renamed columns
    mean_last_5_df = pd.DataFrame(mean_last_5_scores)
    mean_last_5_df.rename(columns={mean_last_5_df.columns[0]: col1}, inplace=True)
    mean_last_5_df.rename(columns={mean_last_5_df.columns[1]: col_rename}, inplace=True)
    return mean_last_5_df


def mean_previous_3_scores_opposition(df, col1, col2, col3, col_rename):
    """Calculate the mean of a team's previous 3 scores against opposing teams.

    :param df: The dataframe the calculation will be performed on
    :param col1: The first column of values the dataframe will be filtered by
    :param col2: The second column of values the dataframe will be filtered by
    :param col3: The column of values the mean will be calculated from
    :param col_rename: The name of the column that will contain the mean values
    :return: A dataframe containing the values of col1, col2 and col_rename
    """

    # Sorts the dataframe by date, ascending
    df = df.sort_values(by='date', ascending=True)

    # Extracts unique team names from col1
    teams = sorted(df.drop_duplicates(subset=[col1])[col1].tolist())
    # Creates a copy of teams list so both lists can be iterated through
    teams_copy = teams

    mean_last_3_scores = []

    for value1 in teams:
        for value2 in teams_copy:
            if value1 == value2:
                continue
            else:
                # Creates a filtered copy of df
                team1_df = df.loc[df[col1] == value1]
                if value2 in team1_df[col2].values:
                    # Adds both team name to team_mean_scores list
                    team_mean_scores = [value1, value2]
                    # Creates a filtered copy of team1_df
                    team2_df = team1_df.loc[df[col2] == value2]
                    scores = team2_df[col3].tolist()

                    # If there is less than 3 scores, the mean is calculated on the available scores
                    if len(scores) < 3:
                        mean_scores = mean(scores)
                    else:
                        mean_scores = mean(scores[-3:])

                    team_mean_scores.append(mean_scores)
                    # mean_last_3_scores is appended with team_mean_scores, creating a list of lists
                    mean_last_3_scores.append(team_mean_scores)

    # mean_last_3_scores is converted to a dataframe with renamed columns
    mean_last_3_opponent_df = pd.DataFrame(mean_last_3_scores)
    mean_last_3_opponent_df.rename(columns={mean_last_3_opponent_df.columns[0]: col1}, inplace=True)
    mean_last_3_opponent_df.rename(columns={mean_last_3_opponent_df.columns[1]: col2}, inplace=True)
    mean_last_3_opponent_df.rename(columns={mean_last_3_opponent_df.columns[2]: col_rename}, inplace=True)
    return mean_last_3_opponent_df


def win_percentage(df, col1, col2, team_type, col_rename):
    """Calculate a teams win percentage

    :param df: The dataframe the calculation will be performed on
    :param col1: The column of values the dataframe will be filtered by
    :param col2: The column of values the wins will be extracted from
    :param team_type: Defines whether col1 relates to home teams or away teams
    :param col_rename: The name of the column that will contain the win percentage
    :return: A dataframe containing the values of col1 and col_rename
    """

    # Extracts unique team names from col1
    teams = sorted(df.drop_duplicates(subset=[col1])[col1].tolist())

    wins = []

    for value in teams:
        # Adds team name to team_wins list
        team_wins = [value]
        filtered_df = df.loc[df[col1] == value]
        outcomes = filtered_df[col2].tolist()
        total_outcomes = len(outcomes)

        # Counts the number of wins and calculates win percentage
        total_wins = op.countOf(outcomes, team_type)
        percentage = str((total_wins / total_outcomes) * 100) + "%"

        team_wins.append(percentage)
        # wins is appended with team_wins, creating a list of lists
        wins.append(team_wins)

    # wins is converted to a dataframe with renamed columns
    wins_df = pd.DataFrame(wins)
    wins_df.rename(columns={wins_df.columns[0]: col1}, inplace=True)
    wins_df.rename(columns={wins_df.columns[1]: col_rename}, inplace=True)
    return wins_df

