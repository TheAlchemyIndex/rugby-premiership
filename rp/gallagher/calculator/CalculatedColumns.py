import pandas as pd
from rp.gallagher.calculator.columns.CalculateMean import calc_means, calc_conditional_means_two_cols, \
    calc_conditional_means_three_cols, calc_previous_5_scores_mean, \
    calc_previous_3_scores_mean_opposition
from rp.gallagher.calculator.columns.filters.ScoreFilter import filter_numeric_scores, filter_results

FILE_PATH = r"../data/All Seasons - 2010-23.csv"

df = pd.read_csv(FILE_PATH)
df['date'] = pd.to_datetime(df["date"])
df_filtered = filter_results(df)
df_calc_means = calc_means(df_filtered)
df_calc_cond_means_two_cols = calc_conditional_means_two_cols(df_calc_means)
df_calc_cond_means_three_cols = calc_conditional_means_three_cols(df_calc_cond_means_two_cols)
df_calc_cond_means_three_cols.sort_values(by='date', inplace=True)
df_calc_last_5_results = calc_previous_5_scores_mean(df_calc_cond_means_three_cols)
df_calc_last_3_results_opponent = calc_previous_3_scores_mean_opposition(df_calc_last_5_results)

#breakpoint()

df_calc_last_3_results_opponent.to_csv("results.csv")
