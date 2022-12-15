def two_columns_mean(df, col1, col2, col_rename):
    avg_2_cols = df.groupby(col1)[col2].mean().reset_index().rename(columns={col2: col_rename})

    return avg_2_cols


def three_columns_mean(df, col1, col2, col3, col_rename):
    avg_3_cols = df.groupby([col1, col2])[col3].mean().reset_index().rename(columns={col3: col_rename})

    return avg_3_cols
