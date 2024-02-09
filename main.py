import pandas as pd

from config import SOURCE_DATA_DIR
from data_analysis.exploratory import ExploratoryDataAnalysis

if __name__ == '__main__':
    exploratory_analysis = ExploratoryDataAnalysis()
    exploratory_analysis.save_pairplot('PLANT_ID')

