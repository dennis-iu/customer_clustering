# main file to start the program
import logging as log

from src.data_prep import DataPreperation
from src.customer_clustering import CustomerClustering

# log-config
log.basicConfig(
    level=log.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

def main():
    log.info("Starting Customer Clustering!")

    # 1. Data Preperation: Loading and Feature Engineering
    with DataPreperation("data/imaginary_customers.csv") as dp:
        prepared_data = dp.process_data()

    # 2. Customer Clustering: Train Model and visualize results
    with CustomerClustering(prepared_data) as cc:
        log.info("clustering...")
        
if __name__ == "__main__":
    main()

