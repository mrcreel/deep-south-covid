import pandas as pd
import io
import requests
url="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv"
s=requests.get(url).content
confirmed=pd.DataFrame(pd.read_csv(io.StringIO(s.decode('utf-8'))))

print(confirmed.head())

confirmed = confirmed.drop(['UID', 'iso2', 'iso3', 'code3', 'FIPS', 'Country_Region', 'Lat', 'Long_', 'Combined_Key'], axis = 1)

"""
for col in confirmed.columns: 
    print(col)
"""