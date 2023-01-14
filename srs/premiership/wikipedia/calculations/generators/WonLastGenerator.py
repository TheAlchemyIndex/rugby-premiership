from srs.premiership.wikipedia.constants.columns import OriginalColumns


def generate_won_last(df, col, new_col):
    """Generates a 1 or 0 to indicate if the team won or last their match.

    :param df: The dataframe the code generation will be performed on
    :param col: The column that will be used to sort the dataframe by team name
    :param new_col: The new column that contains the numeric value of 1 or 0
    :return: A dataframe with new the column of numeric codes that indicate if the team won or lost the match
    """
    sorted_df = df.sort_values(OriginalColumns.DATE)
    won_last = sorted_df[col].rolling(1, closed="left").sum()
    sorted_df[new_col] = won_last
    new_df = sorted_df.dropna(subset=new_col)
    return new_df
