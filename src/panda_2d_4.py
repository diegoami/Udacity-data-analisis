import pandas as pd

filename = '../newyork/nyc_subway_weather.csv'
subway_df = pd.read_csv(filename)


def correlation(x, y):
    pd.
    return None


entries = subway_df['ENTRIESn_hourly']
cum_entries = subway_df['ENTRIESn']
rain = subway_df['meanprecipi']
temp = subway_df['meantempi']

print correlation(entries, rain)
print correlation(entries, temp)
print correlation(rain, temp)

print correlation(entries, cum_entries)