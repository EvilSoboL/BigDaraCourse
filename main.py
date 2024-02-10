import pandas as pd

from data_analysis.exploratory import ExploratoryDataAnalysis

if __name__ == '__main__':
    exploratory_analysis = ExploratoryDataAnalysis()
    #exploratory_analysis.save_all_box_plot()
    #exploratory_analysis.save_pairplot()
    #exploratory_analysis.save_all_qqplot()
    #print(exploratory_analysis.df.describe())
    exploratory_analysis.save_correlation_matrix()
