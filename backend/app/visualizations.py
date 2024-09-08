import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib.dates as mdates
import numpy as np
import logging
import io
import base64

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
    logger.info(f"Date range: {df['Date'].min()} to {df['Date'].max()}")
    logger.info("Data integrity check passed")

def prepare_data(df, region_name):
    if region_name == "UK Nationwide":
        data = df.groupby('Date')['AveragePrice'].mean().reset_index()
    else:
        data = df[df['RegionName'] == region_name].copy()
    
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)
    data = data.resample('ME').last()
    data = data.ffill()
    data = data.reset_index()
    
    return data

def setup_plot(fig, ax, title, ylabel):
    ax.set_title(title)
    ax.set_ylabel(ylabel)
    ax.set_xlabel('Transaction Date')
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.MonthLocator())
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')
    fig.tight_layout()

def create_average_price_plot(data, region_name):
    fig, ax = plt.subplots(figsize=(12, 5))
    x = data['Date']
    y = (data['AveragePrice'] / 1000).round(2)
    ax.plot(x, y, linewidth=2)
    setup_plot(fig, ax, f'Average Price of Properties in {region_name}', 'Average Price (Thousands £)')
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: format(int(x), ',')))
    return fig, data[['Date', 'AveragePrice']].to_dict('records')

def create_cumulative_change_plot(data, region_name):
    fig, ax = plt.subplots(figsize=(12, 5))
    initial_price = data['AveragePrice'].iloc[0]
    cumulative_change = ((data['AveragePrice'] / initial_price - 1) * 100).round(2)
    ax.plot(data['Date'], cumulative_change, linewidth=2)
    setup_plot(fig, ax, f'Cumulative Change of Average Price in {region_name}', 'Cumulative Change (%)')
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x:.2f}%'))
    return fig, data[['Date', 'AveragePrice']].to_dict('records')

def create_property_type_plot(data, region_name):
    fig, ax = plt.subplots(figsize=(12, 5))
    for prop_type in ['DetachedPrice', 'SemiDetachedPrice', 'TerracedPrice', 'FlatPrice']:
        ax.plot(data['Date'], (data[prop_type] / 1000).round(2), linewidth=2, label=prop_type.replace('Price', ''))
    ax.legend()
    setup_plot(fig, ax, f'Average Price by Property Type in {region_name}', 'Average Price (Thousands £)')
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: format(int(x), ',')))
    return fig, data[['Date', 'DetachedPrice', 'SemiDetachedPrice', 'TerracedPrice', 'FlatPrice']].to_dict('records')

def create_property_type_change_plot(data, region_name):
    fig, ax = plt.subplots(figsize=(12, 5))
    for prop_type in ['DetachedPrice', 'SemiDetachedPrice', 'TerracedPrice', 'FlatPrice']:
        initial_price = data[prop_type].iloc[0]
        change = ((data[prop_type] / initial_price - 1) * 100).round(2)
        ax.plot(data['Date'], change, linewidth=2, label=prop_type.replace('Price', ''))
    ax.legend()
    setup_plot(fig, ax, f'Cumulative Change by Property Type in {region_name}', 'Cumulative Change (%)')
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x:.2f}%'))
    return fig, data[['Date', 'DetachedPrice', 'SemiDetachedPrice', 'TerracedPrice', 'FlatPrice']].to_dict('records')

def create_all_plots(df, region_name):
    try:
        check_data_integrity(df)
        data = prepare_data(df, region_name)
        plots = {}
        plot_data = {}
        
        plots['average_price'], plot_data['average_price'] = create_average_price_plot(data, region_name)
        plots['cumulative_change'], plot_data['cumulative_change'] = create_cumulative_change_plot(data, region_name)
        
        if region_name != "UK Nationwide":
            plots['property_type'], plot_data['property_type'] = create_property_type_plot(data, region_name)
            plots['property_type_change'], plot_data['property_type_change'] = create_property_type_change_plot(data, region_name)
        
        encoded_plots = {}
        for key, fig in plots.items():
            buf = io.BytesIO()
            fig.savefig(buf, format='png')
            buf.seek(0)
            encoded_plots[key] = base64.b64encode(buf.getvalue()).decode('utf-8')
            plt.close(fig)
        
        return {"plots": encoded_plots, "data": plot_data}
    except Exception as e:
        logger.error(f"Error in create_all_plots for {region_name}: {str(e)}")
        raise