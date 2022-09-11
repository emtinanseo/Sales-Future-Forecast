import pandas as pd



def date_componants(df: pd.DataFrame, col, col_dates = True) -> pd.DataFrame:   
    if not col_dates:
        dates = pd.to_datetime(col).dt
    else:
        dates = col
        
    df['Year'] = dates.year
    df['Month'] = dates.month
    
    df['DayOfMonth'] = dates.day
    df['BeginMonth'] = df['DayOfMonth'].apply(lambda x:1 if x<=10 else 0)
    df['MidMonth'] = df['DayOfMonth'].apply(lambda x:1 if (x>10 & x<=20) else 0)
    df['EndMonth'] = df['DayOfMonth'].apply(lambda x:1 if x>20 else 0)
    
    df['DayOfYear'] = dates.dayofyear
    df['DayOfWeek'] = dates.dayofweek
    df['IsWeekend'] = df['DayOfWeek'].apply(lambda x: 0 if x < 5 else 1)
    df['IsWeekday'] = 1 - df['IsWeekend'] 
    
    return df

def index_by_date(df: pd.DataFrame, col_name) -> pd.DataFrame:
    dates = pd.to_datetime(df[col_name])
    df[col_name] = dates
    
    return df.set_index(col_name)
    