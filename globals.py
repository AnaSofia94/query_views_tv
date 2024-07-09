import logging
import pandas as pd

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class DataFrameManager:
    _instance = None
    _data_frame = pd.DataFrame()

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DataFrameManager, cls).__new__(cls)
        return cls._instance

    def get_dataframe(self):
        return self._data_frame

    def set_dataframe(self, df):
        self._data_frame = df


data_frame_manager = DataFrameManager()
