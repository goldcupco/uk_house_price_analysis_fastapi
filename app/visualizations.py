import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from matplotlib.dates import DateFormatter, YearLocator
import logging

logger = logging.getLogger(__name__)

def create_hpi_trend_plot(df):
    try:
        plt.figure(figsize=(12, 5))
        for region, group in df.groupby('RegionName'):
            plt.plot(group['Date'], group['AveragePrice'], label=region)
        plt.legend()
        plt.title('HPI - Average Price of Properties across the UK')
        plt.ylabel('Average Price (£)')
        plt.xlabel('Transaction Date')
        plt.xticks(rotation=-90)
        plt.gca().xaxis.set_major_formatter(DateFormatter('%Y'))
        plt.gca().xaxis.set_major_locator(YearLocator())
        plt.tight_layout()
        logger.info("HPI trend plot created successfully")
        return plt
    except Exception as e:
        logger.error(f"Error in create_hpi_trend_plot: {str(e)}")
        raise

def create_regional_comparison_plot(df):
    try:
        latest_date = df['Date'].max()
        latest_data = df[df['Date'] == latest_date]
        
        plt.figure(figsize=(12, 5))
        sns.barplot(x='RegionName', y='AveragePrice', data=latest_data)
        plt.title(f'Regional House Price Comparison (as of {latest_date.strftime("%B %Y")})')
        plt.xlabel('Region')
        plt.ylabel('Average Price (£)')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        logger.info("Regional comparison plot created successfully")
        return plt
    except Exception as e:
        logger.error(f"Error in create_regional_comparison_plot: {str(e)}")
        raise

def create_year_on_year_change_plot(df):
    try:
        plt.figure(figsize=(12, 5))
        for region, group in df.groupby('RegionName'):
            growth = (1 + group['AveragePrice'].pct_change()).cumprod()
            plt.plot(group['Date'], growth, label=region)
        plt.legend()
        plt.title('HPI - Relative Cumulative Change of Average Price of Properties across the UK')
        plt.ylabel('Growth since start')
        plt.xlabel('Transaction Date')
        plt.xticks(rotation=-90)
        plt.gca().xaxis.set_major_formatter(DateFormatter('%Y'))
        plt.gca().xaxis.set_major_locator(YearLocator())
        plt.tight_layout()
        logger.info("Year-on-year change plot created successfully")
        return plt
    except Exception as e:
        logger.error(f"Error in create_year_on_year_change_plot: {str(e)}")
        raise

def check_data_integrity(df):
    required_columns = ['Date', 'RegionName', 'AveragePrice']
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")
    
    if df.empty:
        raise ValueError("DataFrame is empty")
    
    logger.info(f"Data shape: {df.shape}")
    logger.info(f"Columns: {df.columns.tolist()}")
    logger.info(f"Data types: {df.dtypes}")
    logger.info("Data integrity check passed")

def create_all_plots(df):
    try:
        check_data_integrity(df)
        return {
            'hpi_trend': create_hpi_trend_plot(df),
            'regional_comparison': create_regional_comparison_plot(df),
            'yoy_change': create_year_on_year_change_plot(df)
        }
    except Exception as e:
        logger.error(f"Error in create_all_plots: {str(e)}")
        raise