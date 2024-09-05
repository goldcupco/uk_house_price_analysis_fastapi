import pandas as pd
import os
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

def load_and_preprocess_data():
    try:
        # Adjust the path as necessary
        directory = os.path.join(os.path.dirname(__file__), '..', 'data')
        file_path = os.path.join(directory, 'UK-HPI-full-file-2020-06.csv')
        
        logger.info(f"Attempting to load data from {file_path}")
        df = pd.read_csv(file_path)
        
        df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
        
        # Filter by region
        regions_of_interest = ['Cambridge', 'Oxford', 'Inner London', 'Manchester',
                               'Brighton and Hove', 'City of Edinburgh', 'Cardiff']
        df = df[df['RegionName'].isin(regions_of_interest)]
        
        logger.info(f"Data loaded successfully. Shape: {df.shape}")
        return df
    except Exception as e:
        logger.error(f"Error in load_and_preprocess_data: {str(e)}")
        raise