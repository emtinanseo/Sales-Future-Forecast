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
    
    df['WeekOfYear'] = dates.isocalendar().week
    
    df['DayOfYear'] = dates.dayofyear
    df['DayOfWeek'] = dates.dayofweek
    df['IsWeekend'] = df['DayOfWeek'].apply(lambda x: 0 if x < 5 else 1)
    df['IsWeekday'] = 1 - df['IsWeekend'] 
    
    return df

def index_by_date(df: pd.DataFrame, col_name) -> pd.DataFrame:
    dates = pd.to_datetime(df[col_name])
    df[col_name] = dates
    
    return df.set_index(col_name).sort_index()


def before_after_holidays(df: pd.DataFrame, n:int, holidayType=None, multiday = False):
    if holidayType:
        dates = df[df['StateHoliday'] == holidayType].index.unique().sort_values()
    else:
        dates = df[df['StateHoliday'] != '0'].index.unique().sort_values()
    
    step = 1 if multiday else 0
    n_days = pd.to_timedelta(n, 'd')
    a_day = pd.to_timedelta(1, 'd')
    
    i=0
    while i < len(dates):
        df.loc[dates[i]-n_days: dates[i]-a_day, 'BeforeHoliday'] = 1
        df.loc[dates[i+step]+a_day: dates[i+step]+n_days, 'AfterHoliday'] = 1
        i = i +1 +step
        
    return df


def days_wrt_holiday(df: pd.DataFrame, public= 2, easter=5, chrismas=7):
    df['BeforeHoliday'] = 0
    df['AfterHoliday'] = 0
    
    df = before_after_holidays(df, public, holidayType = 'a')
    df = before_after_holidays(df, easter, holidayType = 'b', multiday = True)
    df = before_after_holidays(df, chrismas, holidayType = 'c', multiday = True)
        
    return df
    
def handle_promo2(df: pd.DataFrame):
     
    df['WeeksSincePromo2'] = (df['Year'] - df['Promo2SinceYear'])*52 + df['WeekOfYear'] - df['Promo2SinceWeek']
    
    df['WeeksSincePromo2'].fillna(0, inplace = True)
    
    return df.drop(columns = ['Promo2SinceYear', 'Promo2SinceWeek', 'PromoInterval'])
    
def handle_competition(df: pd.DataFrame):
    df['HasCompetition'] = 0
    df.loc[(df['Month'] >= df['CompetitionOpenSinceMonth'])&(df['Year'] >= df['CompetitionOpenSinceYear']), 
           'HasCompetition'] = 1
    
    return df.drop(columns = ['CompetitionOpenSinceMonth', 'CompetitionOpenSinceYear', 'CompetitionDistance'])
    