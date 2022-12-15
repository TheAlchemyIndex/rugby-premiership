import pandas as pd
from predictor.calculators.CalcColumnsHelper import two_columns_mean, three_columns_mean

TEAM1_NAME = "team1Name"
TEAM2_NAME = "team2Name"
TEAM1_SCORE = "team1Score"
TEAM2_SCORE = "team2Score"
TOTAL_SCORE = "totalScore"
MONTH = "month"
YEAR = "year"
SEASON = "season"


def calculate_means(df):
    df["avgHomeScore"] = df[TEAM1_SCORE].mean()
    df["avgAwayScore"] = df[TEAM2_SCORE].mean()
    df["avgTotalScore"] = df[TOTAL_SCORE].mean()

    return df


def calculate_conditional_means_two_cols(df):
    original_df = df

    avg_home_score_by_month = two_columns_mean(df, MONTH, TEAM1_SCORE, "avgHomeScoreByMonth")
    avg_home_score_by_year = two_columns_mean(df, YEAR, TEAM1_SCORE, "avgHomeScoreByYear")
    avg_home_score_by_season = two_columns_mean(df, SEASON, TEAM1_SCORE, "avgHomeScoreBySeason")
    avg_home_score_by_team = two_columns_mean(df, TEAM1_NAME, TEAM1_SCORE, "avgHomeScoreByTeam")

    avg_away_score_by_month = two_columns_mean(df, MONTH, TEAM2_SCORE, "avgAwayScoreByMonth")
    avg_away_score_by_year = two_columns_mean(df, YEAR, TEAM2_SCORE, "avgAwayScoreByYear")
    avg_away_score_by_season = two_columns_mean(df, SEASON, TEAM2_SCORE, "avgAwayScoreBySeason")
    avg_away_score_by_team = two_columns_mean(df, TEAM2_NAME, TEAM2_SCORE, "avgAwayScoreByTeam")

    avg_total_score_by_month = two_columns_mean(df, MONTH, TOTAL_SCORE, "avgTotalScoreByMonth")
    avg_total_score_by_year = two_columns_mean(df, YEAR, TOTAL_SCORE, "avgTotalScoreByYear")
    avg_total_score_by_season = two_columns_mean(df, SEASON, TOTAL_SCORE, "avgTotalScoreBySeason")

    original_df = pd.merge(original_df, avg_home_score_by_month, on=MONTH, how="outer")
    original_df = pd.merge(original_df, avg_home_score_by_year, on=YEAR, how="outer")
    original_df = pd.merge(original_df, avg_home_score_by_season, on=SEASON, how="outer")
    original_df = pd.merge(original_df, avg_home_score_by_team, on=TEAM1_NAME, how="outer")
    original_df = pd.merge(original_df, avg_away_score_by_month, on=MONTH, how="outer")
    original_df = pd.merge(original_df, avg_away_score_by_year, on=YEAR, how="outer")
    original_df = pd.merge(original_df, avg_away_score_by_season, on=SEASON, how="outer")
    original_df = pd.merge(original_df, avg_away_score_by_team, on=TEAM2_NAME, how="outer")
    original_df = pd.merge(original_df, avg_total_score_by_month, on=MONTH, how="outer")
    original_df = pd.merge(original_df, avg_total_score_by_year, on=YEAR, how="outer")
    original_df = pd.merge(original_df, avg_total_score_by_season, on=SEASON, how="outer")

    original_df.fillna('N/A', inplace=True)
    original_df = original_df.round(2)
    return original_df


def calculate_conditional_means_three_cols(df):
    original_df = df

    avg_home_score_by_team_by_month = three_columns_mean(df, MONTH, TEAM1_NAME, TEAM1_SCORE, "avgHomeScoreByTeamByMonth")
    avg_home_score_by_team_by_year = three_columns_mean(df, YEAR, TEAM1_NAME, TEAM1_SCORE, "avgHomeScoreByTeamByYear")
    avg_home_score_by_team_by_season = three_columns_mean(df, SEASON, TEAM1_NAME, TEAM1_SCORE, "avgHomeScoreByTeamBySeason")

    avg_away_score_by_team_by_month = three_columns_mean(df, MONTH, TEAM2_NAME, TEAM2_SCORE, "avgAwayScoreByTeamByMonth")
    avg_away_score_by_team_by_year = three_columns_mean(df, YEAR, TEAM2_NAME, TEAM2_SCORE, "avgAwayScoreByTeamByYear")
    avg_away_score_by_team_by_season = three_columns_mean(df, SEASON, TEAM2_NAME, TEAM2_SCORE, "avgAwayScoreByTeamBySeason")

    original_df = pd.merge(original_df, avg_home_score_by_team_by_month, on=[TEAM1_NAME, MONTH], how="left")
    original_df = pd.merge(original_df, avg_home_score_by_team_by_year, on=[TEAM1_NAME, YEAR], how="left")
    original_df = pd.merge(original_df, avg_home_score_by_team_by_season, on=[TEAM1_NAME, SEASON], how="left")
    original_df = pd.merge(original_df, avg_away_score_by_team_by_month, on=[TEAM2_NAME, MONTH], how="left")
    original_df = pd.merge(original_df, avg_away_score_by_team_by_year, on=[TEAM2_NAME, YEAR], how="left")
    original_df = pd.merge(original_df, avg_away_score_by_team_by_season, on=[TEAM2_NAME, SEASON], how="left")

    original_df.fillna('N/A', inplace=True)
    original_df = original_df.round(2)
    return original_df
