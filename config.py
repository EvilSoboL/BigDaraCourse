import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SOURCE_DIR = os.path.join(BASE_DIR, "source")
PATH_TO_GENERATION = os.path.join(SOURCE_DIR, "Plant_1_Generation_Data.csv")
PATH_TO_WEATHER = os.path.join(SOURCE_DIR, "Plant_1_Weather_Sensor_Data.csv")

OUTPUT_DIR = os.path.join(BASE_DIR, "output_data")
EXPLORATORY_ANALYSIS = os.path.join(OUTPUT_DIR, "exploratory_analysis")

SOURCE_COLUMNS_TO_READ_GENERATION = ['DATE_TIME', 'DAILY_YIELD', 'TOTAL_YIELD']
SOURCE_COLUMNS_TO_READ_WEATHER = ['DATE_TIME', 'AMBIENT_TEMPERATURE', 'MODULE_TEMPERATURE', 'IRRADIATION']
BOXPLOT_COLUMNS = ['DAILY_YIELD', 'AMBIENT_TEMPERATURE', 'MODULE_TEMPERATURE', 'IRRADIATION']
PAIRPLOT_DROP = ['PLANT_ID']
