from srs.premiership.wikipedia.constants.columns import CalculatedColumns, OriginalColumns


def generate_category_codes(df):
    """Generates a unique numeric code for key columns that contain string values.

    :param df: The dataframe the code generation will be performed on
    :return: A dataframe with new columns of numeric codes for key columns that contain strings
    """
    df[CalculatedColumns.TARGET_CODE] = (df[OriginalColumns.RESULT] == "W").astype("int")
    return df
