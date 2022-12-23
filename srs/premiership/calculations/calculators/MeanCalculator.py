from srs.premiership.constants import OriginalColumns


def calc_rolling_5_scores_mean(df, cols, new_cols):
    """Calculate the mean for the last 5 home scores and points scored against for each home team on a rolling basis.

    :param df: The dataframe the calculation will be performed on
    :param cols: The columns of values that the mean will be calculated from
    :param new_cols: The new columns that will be created that contain the mean values
    :return: A dataframe containing columns of the rolling mean values for the home team's previous 5 scores as well
    as the points scored against them
    """
    sorted_df = df.sort_values(OriginalColumns.DATE)
    rolling_scores = sorted_df[cols].rolling(5, closed="left").mean()
    sorted_df[new_cols] = rolling_scores
    new_df = sorted_df.dropna(subset=new_cols)
    return new_df
