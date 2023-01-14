from srs.premiership.wikipedia.constants.columns import OriginalColumns


def drop_columns(df):
    """Drops non-required columns from df.

    :param df: The dataframe the drop will be performed on
    :return: A filtered dataframe with only required columns
    """

    new_df = df.drop([OriginalColumns.TIME,
                      OriginalColumns.TEAM1_POINTS,
                      OriginalColumns.TEAM2_POINTS,
                      OriginalColumns.TOTAL_POINTS,
                      OriginalColumns.HOUR,
                      OriginalColumns.YEAR,
                      OriginalColumns.TEAM1_BPS,
                      OriginalColumns.TEAM2_BPS,
                      OriginalColumns.TEAM1_TRIES,
                      OriginalColumns.TEAM1_CONVERSIONS,
                      OriginalColumns.TEAM1_PENALTIES,
                      OriginalColumns.TEAM1_DROP_GOALS,
                      OriginalColumns.TEAM2_TRIES,
                      OriginalColumns.TEAM2_CONVERSIONS,
                      OriginalColumns.TEAM2_PENALTIES,
                      OriginalColumns.TEAM2_DROP_GOALS], axis=1)
    return new_df
