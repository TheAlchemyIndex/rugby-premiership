from srs.premiership.wikipedia.constants.columns import OriginalColumns


def calc_rolling_mean(df, cols, new_cols, count):
    """Calculate rolling mean of the values in cols, using count as the number of rows for the rolling amount.

    :param df: The dataframe the calculation will be performed on
    :param cols: The columns of values that the mean will be calculated from
    :param new_cols: The new columns that will be created that contain the mean values
    :param count: The number of rows to calculate the rolling mean from
    :return: A dataframe containing columns of the rolling mean values
    """
    sorted_df = df.sort_values(OriginalColumns.DATE)
    rolling_mean = sorted_df[cols].rolling(count, closed="left").mean()
    sorted_df[new_cols] = rolling_mean
    return sorted_df
