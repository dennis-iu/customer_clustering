import logging as log

# log-config
log.basicConfig(
    level=log.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

class CustomerClustering:
    def __init__(self, data):
        """
        To initialize the CustomerClustering Class.
        
        :param data: str - prepared training data
        :return: None
        """
        self.data = data

    def __enter__(self):
        """Enter class."""
        log.debug("Entering CustomerClustering context")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exit class.

        :param exc_type: Exception Type
        :param exc_val: Exception Value
        :param exc_tb: Exception Traceback
        :return: None
        """
        log.debug("Exiting CustomerClustering context")
        if exc_type is not None:
            log.error(f"Exception: {exc_type} - {exc_val}")
            log.error(
                f"Traceback: {exc_tb.tb_frame.f_code.co_filename} - {exc_tb.tb_lineno}"
            )
            raise exc_val