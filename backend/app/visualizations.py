import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from matplotlib.dates import DateFormatter, YearLocator
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def check_data_integrity(df):
    required_columns = ['Date', 'RegionName', 'AveragePrice', 'DetachedPrice', 'SemiDetachedPrice', 'TerracedPrice', 'FlatPrice']
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")
    
    if df.empty:
        raise ValueError("DataFrame is empty")
    
    logger.info(f"Data shape: {df.shape}")
    logger.info(f"Columns: {df.columns.tolist()}")
    logger.info(f"Data types: {df.dtypes}")
    logger.info("Data integrity check passed")

def create_average_price_plot(df, region_name):
    try:
        fig, ax = plt.subplots(figsize=(12, 5))
        if region_name == "Across the UK":
            for region, group in df.groupby('RegionName'):
                ax.plot(group['Date'], group['AveragePrice'], label=region)
            ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        else:
            region_data = df[df['RegionName'] == region_name]
            ax.plot(region_data['Date'], region_data['AveragePrice'])
        ax.set_title(f'Average Price of Properties in {region_name}')
        ax.set_ylabel('Average Price (£)')
        ax.set_xlabel('Transaction Date')
        ax.tick_params(axis='x', rotation=-90)
        ax.xaxis.set_major_formatter(DateFormatter('%Y'))
        ax.xaxis.set_major_locator(YearLocator())
        fig.tight_layout()
        logger.info(f"Average price plot for {region_name} created successfully")
        return fig
    except Exception as e:
        logger.error(f"Error in create_average_price_plot for {region_name}: {str(e)}")
        raise

def create_cumulative_change_plot(df, region_name):
    try:
        fig, ax = plt.subplots(figsize=(12, 5))
        if region_name == "Across the UK":
            for region, group in df.groupby('RegionName'):
                growth = (1 + group['AveragePrice'].pct_change()).cumprod()
                ax.plot(group['Date'], growth, label=region)
            ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        else:
            region_data = df[df['RegionName'] == region_name]
            growth = (1 + region_data['AveragePrice'].pct_change()).cumprod()
            ax.plot(region_data['Date'], growth)
        ax.set_title(f'Relative Cumulative Change of Average Price of Properties in {region_name}')
        ax.set_ylabel('Growth since start')
        ax.set_xlabel('Transaction Date')
        ax.tick_params(axis='x', rotation=-90)
        ax.xaxis.set_major_formatter(DateFormatter('%Y'))
        ax.xaxis.set_major_locator(YearLocator())
        fig.tight_layout()
        logger.info(f"Cumulative change plot for {region_name} created successfully")
        return fig
    except Exception as e:
        logger.error(f"Error in create_cumulative_change_plot for {region_name}: {str(e)}")
        raise

def create_property_type_plot(df, region_name):
    try:
        region_data = df[df['RegionName'] == region_name]
        fig, ax = plt.subplots(figsize=(12, 5))
        for prop_type in ['DetachedPrice', 'SemiDetachedPrice', 'TerracedPrice', 'FlatPrice']:
            ax.plot(region_data['Date'], region_data[prop_type], label=prop_type.replace('Price', ''))
        ax.legend()
        ax.set_title(f'Average Price by Property Type in {region_name}')
        ax.set_ylabel('Average Price (£)')
        ax.set_xlabel('Transaction Date')
        ax.tick_params(axis='x', rotation=-90)
        ax.xaxis.set_major_formatter(DateFormatter('%Y'))
        ax.xaxis.set_major_locator(YearLocator())
        fig.tight_layout()
        logger.info(f"Property type plot for {region_name} created successfully")
        return fig
    except Exception as e:
        logger.error(f"Error in create_property_type_plot for {region_name}: {str(e)}")
        raise

def create_property_type_change_plot(df, region_name):
    try:
        region_data = df[df['RegionName'] == region_name]
        fig, ax = plt.subplots(figsize=(12, 5))
        for prop_type in ['DetachedPrice', 'SemiDetachedPrice', 'TerracedPrice', 'FlatPrice']:
            growth = (1 + region_data[prop_type].pct_change()).cumprod()
            ax.plot(region_data['Date'], growth, label=prop_type.replace('Price', ''))
        ax.legend()
        ax.set_title(f'Relative Cumulative Change of Average Price by Property Type in {region_name}')
        ax.set_ylabel('Growth since start')
        ax.set_xlabel('Transaction Date')
        ax.tick_params(axis='x', rotation=-90)
        ax.xaxis.set_major_formatter(DateFormatter('%Y'))
        ax.xaxis.set_major_locator(YearLocator())
        fig.tight_layout()
        logger.info(f"Property type change plot for {region_name} created successfully")
        return fig
    except Exception as e:
        logger.error(f"Error in create_property_type_change_plot for {region_name}: {str(e)}")
        raise

def create_all_plots(df, region_name):
    try:
        if region_name != "Across the UK":
            region_data = df[df['RegionName'] == region_name]
        else:
            region_data = df
        check_data_integrity(region_data)
        plots = {}
        
        plots['average_price'] = create_average_price_plot(region_data, region_name)
        plt.close()
        
        plots['cumulative_change'] = create_cumulative_change_plot(region_data, region_name)
        plt.close()
        
        if region_name != "Across the UK":
            plots['property_type'] = create_property_type_plot(region_data, region_name)
            plt.close()
            
            plots['property_type_change'] = create_property_type_change_plot(region_data, region_name)
            plt.close()
        
        return plots
    except Exception as e:
        logger.error(f"Error in create_all_plots for {region_name}: {str(e)}")
        raise