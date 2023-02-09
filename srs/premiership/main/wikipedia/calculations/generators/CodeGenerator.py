from srs.premiership.main.wikipedia.constants.columns import OriginalColumns, CalculatedColumns


def generate_category_codes(df):
    """Generates a 1 or 0 to indicate if the team won or last the match.

    :param df: The dataframe the code generation will be performed on
    :return: A dataframe with new the column of numeric codes that indicate if the team won or lost the match
    """
    df[CalculatedColumns.TARGET_CODE] = (df[OriginalColumns.RESULT] == "W").astype("int")
    return df
