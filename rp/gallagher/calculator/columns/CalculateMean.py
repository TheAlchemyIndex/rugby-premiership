from rp.gallagher.calculator.columns.ColumnHelper import *
from rp.gallagher.constants import OriginalColumns
from rp.gallagher.constants import CalculatedColumns


def calc_means(df):
    """Calculate the mean of the score columns.

    :param df: The dataframe the calculation will be performed on
    :return: A dataframe containing columns of mean values for the score columns
    """
    df[CalculatedColumns.AVG_HOME_SCORE] = df[OriginalColumns.TEAM1_SCORE].mean()
    df[CalculatedColumns.AVG_AWAY_SCORE] = df[OriginalColumns.TEAM2_SCORE].mean()
    df[CalculatedColumns.AVG_TOTAL_SCORE] = df[OriginalColumns.TOTAL_SCORE].mean()
    return df


def calc_conditional_means_two_cols(df):
    """Calculate the mean of the score columns, based on the month, year and season columns.

    :param df: The dataframe the calculation will be performed on
    :return: A dataframe containing columns of mean values for the score columns by month, year and
    season
    """
    # By home team scores
    avg_home_score_by_month = two_columns_mean(df, OriginalColumns.MONTH, OriginalColumns.TEAM1_SCORE,
                                               CalculatedColumns.AVG_HOME_SCORE_BY_MONTH)
    avg_home_score_by_year = two_columns_mean(df, OriginalColumns.YEAR, OriginalColumns.TEAM1_SCORE,
                                              CalculatedColumns.AVG_HOME_SCORE_BY_YEAR)
    avg_home_score_by_season = two_columns_mean(df, OriginalColumns.SEASON, OriginalColumns.TEAM1_SCORE,
                                                CalculatedColumns.AVG_HOME_SCORE_BY_SEASON)
    avg_home_score_by_venue = two_columns_mean(df, OriginalColumns.VENUE, OriginalColumns.TEAM1_SCORE,
                                               CalculatedColumns.AVG_HOME_SCORE_BY_VENUE)
    avg_home_score_by_team = two_columns_mean(df, OriginalColumns.TEAM1_NAME, OriginalColumns.TEAM1_SCORE,
                                              CalculatedColumns.AVG_HOME_SCORE_BY_TEAM)

    # By away team scores
    avg_away_score_by_month = two_columns_mean(df, OriginalColumns.MONTH, OriginalColumns.TEAM2_SCORE,
                                               CalculatedColumns.AVG_AWAY_SCORE_BY_MONTH)
    avg_away_score_by_year = two_columns_mean(df, OriginalColumns.YEAR, OriginalColumns.TEAM2_SCORE,
                                              CalculatedColumns.AVG_AWAY_SCORE_BY_YEAR)
    avg_away_score_by_season = two_columns_mean(df, OriginalColumns.SEASON, OriginalColumns.TEAM2_SCORE,
                                                CalculatedColumns.AVG_AWAY_SCORE_BY_SEASON)
    avg_away_score_by_venue = two_columns_mean(df, OriginalColumns.VENUE, OriginalColumns.TEAM2_SCORE,
                                               CalculatedColumns.AVG_AWAY_SCORE_BY_VENUE)
    avg_away_score_by_team = two_columns_mean(df, OriginalColumns.TEAM2_NAME, OriginalColumns.TEAM2_SCORE,
                                              CalculatedColumns.AVG_AWAY_SCORE_BY_TEAM)

    # By total score
    avg_total_score_by_month = two_columns_mean(df, OriginalColumns.MONTH, OriginalColumns.TOTAL_SCORE,
                                                CalculatedColumns.AVG_TOTAL_SCORE_BY_MONTH)
    avg_total_score_by_year = two_columns_mean(df, OriginalColumns.YEAR, OriginalColumns.TOTAL_SCORE,
                                               CalculatedColumns.AVG_TOTAL_SCORE_BY_YEAR)
    avg_total_score_by_season = two_columns_mean(df, OriginalColumns.SEASON, OriginalColumns.TOTAL_SCORE,
                                                 CalculatedColumns.AVG_TOTAL_SCORE_BY_SEASON)
    avg_total_score_by_venue = two_columns_mean(df, OriginalColumns.VENUE, OriginalColumns.TOTAL_SCORE,
                                                CalculatedColumns.AVG_TOTAL_SCORE_BY_VENUE)

    # Merge with df and return new_df of values, rounded to 2 decimal places
    new_df = pd.merge(df, avg_home_score_by_month, on=OriginalColumns.MONTH, how="outer")
    new_df = pd.merge(new_df, avg_home_score_by_year, on=OriginalColumns.YEAR, how="outer")
    new_df = pd.merge(new_df, avg_home_score_by_season, on=OriginalColumns.SEASON, how="outer")
    new_df = pd.merge(new_df, avg_home_score_by_venue, on=OriginalColumns.VENUE, how="outer")
    new_df = pd.merge(new_df, avg_home_score_by_team, on=OriginalColumns.TEAM1_NAME, how="outer")
    new_df = pd.merge(new_df, avg_away_score_by_month, on=OriginalColumns.MONTH, how="outer")
    new_df = pd.merge(new_df, avg_away_score_by_year, on=OriginalColumns.YEAR, how="outer")
    new_df = pd.merge(new_df, avg_away_score_by_season, on=OriginalColumns.SEASON, how="outer")
    new_df = pd.merge(new_df, avg_away_score_by_venue, on=OriginalColumns.VENUE, how="outer")
    new_df = pd.merge(new_df, avg_away_score_by_team, on=OriginalColumns.TEAM2_NAME, how="outer")
    new_df = pd.merge(new_df, avg_total_score_by_month, on=OriginalColumns.MONTH, how="outer")
    new_df = pd.merge(new_df, avg_total_score_by_year, on=OriginalColumns.YEAR, how="outer")
    new_df = pd.merge(new_df, avg_total_score_by_season, on=OriginalColumns.SEASON, how="outer")
    new_df = pd.merge(new_df, avg_total_score_by_venue, on=OriginalColumns.VENUE, how="outer")
    new_df.fillna('N/A', inplace=True)
    new_df = new_df.round(2)
    return new_df


def calc_conditional_means_three_cols(df):
    """Calculate the mean of the score columns, based on the month, year and season columns, by team.

    :param df: The dataframe the calculation will be performed on
    :return: A dataframe containing columns of mean values for the score columns of each team by month,
    year and season
    """
    # By home team scores
    avg_home_score_by_team_by_month = three_columns_mean(df, OriginalColumns.MONTH, OriginalColumns.TEAM1_NAME,
                                                         OriginalColumns.TEAM1_SCORE,
                                                         CalculatedColumns.AVG_HOME_SCORE_BY_TEAM_BY_MONTH)
    avg_home_score_by_team_by_year = three_columns_mean(df, OriginalColumns.YEAR, OriginalColumns.TEAM1_NAME,
                                                        OriginalColumns.TEAM1_SCORE,
                                                        CalculatedColumns.AVG_HOME_SCORE_BY_TEAM_BY_YEAR)
    avg_home_score_by_team_by_season = three_columns_mean(df, OriginalColumns.SEASON, OriginalColumns.TEAM1_NAME,
                                                          OriginalColumns.TEAM1_SCORE,
                                                          CalculatedColumns.AVG_HOME_SCORE_BY_TEAM_BY_SEASON)
    avg_home_score_by_team_by_venue = three_columns_mean(df, OriginalColumns.VENUE, OriginalColumns.TEAM1_NAME,
                                                         OriginalColumns.TEAM1_SCORE,
                                                         CalculatedColumns.AVG_HOME_SCORE_BY_TEAM_BY_VENUE)

    # By away team scores
    avg_away_score_by_team_by_month = three_columns_mean(df, OriginalColumns.MONTH, OriginalColumns.TEAM2_NAME,
                                                         OriginalColumns.TEAM2_SCORE,
                                                         CalculatedColumns.AVG_AWAY_SCORE_BY_TEAM_BY_MONTH)
    avg_away_score_by_team_by_year = three_columns_mean(df, OriginalColumns.YEAR, OriginalColumns.TEAM2_NAME,
                                                        OriginalColumns.TEAM2_SCORE,
                                                        CalculatedColumns.AVG_AWAY_SCORE_BY_TEAM_BY_YEAR)
    avg_away_score_by_team_by_season = three_columns_mean(df, OriginalColumns.SEASON, OriginalColumns.TEAM2_NAME,
                                                          OriginalColumns.TEAM2_SCORE,
                                                          CalculatedColumns.AVG_AWAY_SCORE_BY_TEAM_BY_SEASON)
    avg_away_score_by_team_by_venue = three_columns_mean(df, OriginalColumns.VENUE, OriginalColumns.TEAM2_NAME,
                                                         OriginalColumns.TEAM2_SCORE,
                                                         CalculatedColumns.AVG_AWAY_SCORE_BY_TEAM_BY_VENUE)

    # Merge with df and return new_df of values, rounded to 2 decimal places
    new_df = pd.merge(df, avg_home_score_by_team_by_month, on=[OriginalColumns.TEAM1_NAME, OriginalColumns.MONTH],
                      how="left")
    new_df = pd.merge(new_df, avg_home_score_by_team_by_year, on=[OriginalColumns.TEAM1_NAME, OriginalColumns.YEAR],
                      how="left")
    new_df = pd.merge(new_df, avg_home_score_by_team_by_season, on=[OriginalColumns.TEAM1_NAME, OriginalColumns.SEASON],
                      how="left")
    new_df = pd.merge(new_df, avg_home_score_by_team_by_venue, on=[OriginalColumns.TEAM1_NAME, OriginalColumns.VENUE],
                      how="left")
    new_df = pd.merge(new_df, avg_away_score_by_team_by_month, on=[OriginalColumns.TEAM2_NAME, OriginalColumns.MONTH],
                      how="left")
    new_df = pd.merge(new_df, avg_away_score_by_team_by_year, on=[OriginalColumns.TEAM2_NAME, OriginalColumns.YEAR],
                      how="left")
    new_df = pd.merge(new_df, avg_away_score_by_team_by_season, on=[OriginalColumns.TEAM2_NAME, OriginalColumns.SEASON],
                      how="left")
    new_df = pd.merge(new_df, avg_away_score_by_team_by_venue, on=[OriginalColumns.TEAM2_NAME, OriginalColumns.VENUE],
                      how="left")
    new_df.fillna('N/A', inplace=True)
    new_df = new_df.round(2)
    return new_df


def calc_previous_5_scores_mean(df):
    """Calculate the mean of the score columns, based on the last 5 or fewer scores.

    :param df: The dataframe the calculation will be performed on
    :return: A dataframe containing columns of mean values for the score columns, based on the last
    5 or fewer scores
    """
    # By home team scores
    avg_home_score_last_5_results = mean_previous_5_scores(df, OriginalColumns.TEAM1_NAME, OriginalColumns.TEAM1_SCORE,
                                                           CalculatedColumns.AVG_HOME_LAST_5_RESULTS)
    # By away team scores
    avg_away_score_last_5_results = mean_previous_5_scores(df, OriginalColumns.TEAM2_NAME, OriginalColumns.TEAM2_SCORE,
                                                           CalculatedColumns.AVG_AWAY_LAST_5_RESULTS)

    # Merge with df and return new_df of values, rounded to 2 decimal places
    new_df = pd.merge(df, avg_home_score_last_5_results, on=OriginalColumns.TEAM1_NAME, how="outer")
    new_df = pd.merge(new_df, avg_away_score_last_5_results, on=OriginalColumns.TEAM2_NAME, how="outer")
    new_df.fillna('N/A', inplace=True)
    new_df = new_df.round(2)
    return new_df


def calc_previous_3_scores_mean_opposition(df):
    """Calculate the mean of the score columns, based on the last 3 or fewer scores against opposing teams.

    :param df: The dataframe the calculation will be performed on
    :return: A dataframe containing columns of mean values for the score columns, based on the last
    3 or fewer scores against opposing teams
    """
    # By home team scores
    avg_home_score_last_3_results_opposition = mean_previous_3_scores_opposition(df, OriginalColumns.TEAM1_NAME,
                                                                                 OriginalColumns.TEAM2_NAME,
                                                                                 OriginalColumns.TEAM1_SCORE,
                                                                                 CalculatedColumns.AVG_HOME_LAST_3_RESULTS_OPPOSITION)
    # By away team scores
    avg_away_score_last_3_results_opposition = mean_previous_3_scores_opposition(df, OriginalColumns.TEAM2_NAME,
                                                                                 OriginalColumns.TEAM1_NAME,
                                                                                 OriginalColumns.TEAM2_SCORE,
                                                                                 CalculatedColumns.AVG_AWAY_LAST_3_RESULTS_OPPOSITION)

    # Merge with df and return new_df of values, rounded to 2 decimal places
    new_df = pd.merge(df, avg_home_score_last_3_results_opposition,
                      on=[OriginalColumns.TEAM1_NAME, OriginalColumns.TEAM2_NAME], how="left")
    new_df = pd.merge(new_df, avg_away_score_last_3_results_opposition,
                      on=[OriginalColumns.TEAM2_NAME, OriginalColumns.TEAM1_NAME], how="left")
    new_df.fillna('N/A', inplace=True)
    new_df = new_df.round(2)
    return new_df
