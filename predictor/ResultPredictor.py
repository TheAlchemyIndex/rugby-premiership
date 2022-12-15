import pandas as pd
from predictor.calculators.CalcMeanColumns import calculate_means, calculate_conditional_means_two_cols, \
    calculate_conditional_means_three_cols
from predictor.filters.ScoreFilter import filter_numeric_scores


FILE_PATH = r"/data/All Seasons - 2010-23.csv"

df = pd.read_csv(FILE_PATH)
df_filtered = filter_numeric_scores(df)
df_calc_means = calculate_means(df_filtered)
df_calc_cond_means_two_cols = calculate_conditional_means_two_cols(df_calc_means)
df_calc_cond_means_three_cols = calculate_conditional_means_three_cols(df_calc_cond_means_two_cols)

df_calc_cond_means_three_cols.to_csv("results.csv")
