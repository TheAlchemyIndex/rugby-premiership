from srs.premiership.wikipedia.constants.columns import CalculatedColumns, OriginalColumns


def generate_category_codes(df):
    """Generates a unique numeric code for various key columns that contain string values.

    :param df: The dataframe the code generation will be performed on
    :return: A dataframe with new columns of numeric codes for key columns that contain strings
    """

    df[CalculatedColumns.HOME_TEAM_CODE] = df[OriginalColumns.TEAM1_NAME].astype("category").cat.codes
    df[CalculatedColumns.AWAY_TEAM_CODE] = df[OriginalColumns.TEAM2_NAME].astype("category").cat.codes
    df[CalculatedColumns.MONTH_CODE] = df[OriginalColumns.MONTH].astype("category").cat.codes
    df[CalculatedColumns.VENUE_CODE] = df[OriginalColumns.VENUE].astype("category").cat.codes
    df[CalculatedColumns.DAY_CODE] = df[OriginalColumns.DAY].astype("category").cat.codes
    df[CalculatedColumns.REFEREE_CODE] = df[OriginalColumns.REFEREE].astype("category").cat.codes
    df[CalculatedColumns.SEASON_CODE] = df[OriginalColumns.SEASON].astype("category").cat.codes
    df[CalculatedColumns.TARGET_CODE] = (df[OriginalColumns.WINNER] == "H").astype("int")
    return df
