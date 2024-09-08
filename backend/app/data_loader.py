import pandas as pd
import os

def load_data():
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'UK-HPI-full-file-2020-06.csv')
    df = pd.read_csv(file_path)
    
    # Filter for all cities and add UK Nationwide
    cities = [
        "London", "Birmingham", "Leeds", "Glasgow", "Sheffield", "Bradford", "Liverpool", "Edinburgh", "Manchester",
        "Bristol", "Kirklees", "Fife", "Wirral", "North Lanarkshire", "Wakefield", "Cardiff", "Dudley", "Wigan",
        "East Riding of Yorkshire", "South Lanarkshire", "Coventry", "Belfast", "Leicester", "Sunderland", "Sandwell",
        "Doncaster", "Stockport", "Sefton", "Nottingham", "Newcastle upon Tyne", "Kingston upon Hull", "Bolton",
        "Plymouth", "Rotherham", "Stoke-on-Trent", "Wolverhampton", "Derby", "Swansea", "Southampton", "Salford",
        "Aberdeen", "Aberdeenshire", "Northampton", "Dudley", "Portsmouth", "Norwich", "Walsall", "Bournemouth",
        "Southend-on-Sea", "Swindon", "Basildon", "Cheshire East", "Chelmsford", "Armagh", "Lisburn", "Derry",
        "Bath", "Cambridge", "Chester", "Chichester", "Dundee", "Dunfermline", "Ely", "Exeter", "Hereford",
        "Inverness", "Lancaster", "Lichfield", "Lincoln", "Newport", "Oxford", "Perth", "Preston", "Ripon",
        "St Albans", "St Asaph", "St Davids", "Stirling", "Truro", "Wells", "Winchester", "Wrexham"
    ]
    
    df_cities = df[df['RegionName'].isin(cities)]
    
    # Add UK Nationwide data
    uk_nationwide = df.groupby('Date')['AveragePrice'].mean().reset_index()
    uk_nationwide['RegionName'] = 'UK Nationwide'
    
    df_final = pd.concat([df_cities, uk_nationwide])
    
    return df_final
