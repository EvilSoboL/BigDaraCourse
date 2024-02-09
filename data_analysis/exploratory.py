import pandas as pd
import matplotlib.pyplot as plt
import os

from config import SOURCE_DATA_DIR, EXPLORATORY_ANALYSIS, BOXPLOT_COLUMNS


class ExploratoryDataAnalysis:
    def __init__(self):
        self.path_to_source = None
        self.df = None

        self.set_path_to_source(SOURCE_DATA_DIR)
        self.get_source_df(10_000)

        self.create_exploratory_dir()

        #self.save_box_plot()

    def set_path_to_source(self, path_to_source):
        self.path_to_source = path_to_source

    def get_source_df(self, rows_to_read: int):
        if not self.path_to_source:
            raise Warning("Атрибут path_to_source не задан!")
        self.df = pd.read_csv(SOURCE_DATA_DIR, nrows=rows_to_read)

    def create_exploratory_dir(self):
        os.makedirs(EXPLORATORY_ANALYSIS, exist_ok=True)

    def save_box_plot(self, column_to_plot: str):
        plt.boxplot(self.df[column_to_plot])
        plt.title(column_to_plot)
        plt.ylabel('kW')
        self.save_plot(EXPLORATORY_ANALYSIS, f'boxplot_{column_to_plot}')

    def save_plot(self, dir_to_save, filename):
        path_to_save = os.path.join(dir_to_save, f'{filename}.png')
        plt.savefig(path_to_save)
        plt.close()

    def save_all_box_plot(self):
        for column_to_plot in BOXPLOT_COLUMNS:
            self.save_box_plot(column_to_plot)
