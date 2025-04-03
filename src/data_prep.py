import logging as log
import pandas as pd

# log-config
log.basicConfig(
    level=log.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

class DataPreperation:
    def __init__(self, data_path):
        """
        To initialize the DataPreperation Class.
        
        :param data_path: str - path to the training data
        :return: None
        """
        self.data_path = data_path

    def __enter__(self):
        """Enter class."""
        log.debug("Entering DataPreperation context")
        self.load_data()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exit class.

        :param exc_type: Exception Type
        :param exc_val: Exception Value
        :param exc_tb: Exception Traceback
        :return: None
        """
        log.debug("Exiting DataPreperation context")
        if exc_type is not None:
            log.error(f"Exception: {exc_type} - {exc_val}")
            log.error(
                f"Traceback: {exc_tb.tb_frame.f_code.co_filename} - {exc_tb.tb_lineno}"
            )
            raise exc_val

    def load_data(self):
        """Function to load data from a csv into a pandas DataFrame."""
        self.data = pd.read_csv(self.data_path)

    def process_data(self):
        """Process the data for planned training."""
        return self.data