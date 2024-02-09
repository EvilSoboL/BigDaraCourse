import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SOURCE_DIR = os.path.join(BASE_DIR, "source")
SOURCE_DATA_DIR = os.path.join(SOURCE_DIR, "Plant_1_Generation_Data.csv")

OUTPUT_DIR = os.path.join(BASE_DIR, "output_data")
EXPLORATORY_ANALYSIS = os.path.join(OUTPUT_DIR, "exploratory_analysis")

BOXPLOT_COLUMNS = ['DC_POWER', 'AC_POWER', 'DAILY_YIELD']
PAIRPLOT_DROP = ['PLANT_ID']
