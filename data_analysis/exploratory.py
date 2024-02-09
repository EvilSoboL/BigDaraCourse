import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns
import statsmodels.api as sm

from config import (PATH_TO_GENERATION,
                    PATH_TO_WEATHER,
                    EXPLORATORY_ANALYSIS,
                    BOXPLOT_COLUMNS,
                    SOURCE_COLUMNS_TO_READ_GENERATION,
                    SOURCE_COLUMNS_TO_READ_WEATHER)


class ExploratoryDataAnalysis:
    def __init__(self):
        self.path_to_generation = None
        self.path_to_weather = None
        self.columns_to_read_generation = None
        self.columns_to_read_weather = None
        self.df = None

        self.set_path_to_generation(PATH_TO_GENERATION)
        self.set_path_to_weather(PATH_TO_WEATHER)
        self.set_columns_to_read_generation(SOURCE_COLUMNS_TO_READ_GENERATION)
        self.set_columns_to_read_weather(SOURCE_COLUMNS_TO_READ_WEATHER)

        self.get_source_df(10_102)

        self.create_exploratory_dir()

        #self.save_box_plot()

    def set_path_to_generation(self, path_to_generation):
        self.path_to_generation = path_to_generation

    def set_path_to_weather(self, path_to_weather):
        self.path_to_weather = path_to_weather

    def set_columns_to_read_generation(self, columns_to_use):
        self.columns_to_read_generation = columns_to_use

    def set_columns_to_read_weather(self, columns_to_use):
        self.columns_to_read_weather = columns_to_use

    def get_source_df(self, rows_to_read: int):
        if not self.path_to_generation and self.path_to_weather:
            raise Warning("Атрибут path_to_generation или path_to_weather не задан!")
        generation_df = pd.read_csv(self.path_to_generation, nrows=rows_to_read, usecols=self.columns_to_read_generation)
        weather_df = pd.read_csv(self.path_to_weather, nrows=466, usecols=self.columns_to_read_weather)
        generation_df, weather_df = self._set_dtype_to_datetime(
            [generation_df, weather_df], 'DATE_TIME'
        )
        merged_data = pd.merge(generation_df, weather_df, on='DATE_TIME', how='inner')
        self.df = merged_data

    def create_exploratory_dir(self):
        os.makedirs(EXPLORATORY_ANALYSIS, exist_ok=True)

    def _save_boxplot(self, column_to_plot: str):
        plt.boxplot(self.df[column_to_plot])
        plt.title(column_to_plot)
        if column_to_plot in ['AMBIENT_TEMPERATURE', 'MODULE_TEMPERATURE']:
            plt.ylabel(r'$ ^oC$')
        elif column_to_plot == 'IRRADIATION':
            plt.ylabel('')
        else:
            plt.ylabel('kW')
        self._save_plot(EXPLORATORY_ANALYSIS, f'boxplot_{column_to_plot}')

    def _save_plot(self, dir_to_save, filename):
        path_to_save = os.path.join(dir_to_save, f'{filename}.png')
        plt.savefig(path_to_save)
        plt.close()

    def save_all_box_plot(self):
        for column_to_plot in BOXPLOT_COLUMNS:
            self._save_boxplot(column_to_plot)

    def save_pairplot(self):
        sns.pairplot(self.df)
        plt.tight_layout()
        self._save_plot(EXPLORATORY_ANALYSIS, 'pairplot')

    def _set_dtype_to_datetime(self, dfs: list[pd.DataFrame], datetime_columns) -> tuple[pd.DataFrame, ...]:
        for df in dfs:
            df[datetime_columns] = pd.to_datetime(df[datetime_columns], dayfirst=True)
        return tuple(dfs)

    def _save_qqplot(self, column_to_plot: str):
        sm.qqplot(self.df[column_to_plot], line='45')
        plt.title(column_to_plot)
        self._save_plot(EXPLORATORY_ANALYSIS, f'qqplot_{column_to_plot}')

    def save_all_qqplot(self):
        for column_to_plot in BOXPLOT_COLUMNS:
            self._save_qqplot(column_to_plot)
