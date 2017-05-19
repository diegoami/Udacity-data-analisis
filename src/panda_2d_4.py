import pandas as pd

filename = '../newyork/nyc_subway_weather.csv'
subway_df = pd.read_csv(filename)


def correlation(x, y):
    std_x = (x - x.mean()) / x.std(ddof=0)
    std_y = (y - y.mean()) / y.std(ddof=0)

    return (std_x*std_y).mean()


entries = subway_df['ENTRIESn_hourly']
cum_entries = subway_df['ENTRIESn']
rain = subway_df['meanprecipi']
temp = subway_df['meantempi']

x = pd.Series([1, 2, 3, 4])
y = pd.Series([10, 11, 12, 13])
print correlation(x, y)
"""
print correlation(entries, rain)
print correlation(entries, temp)
print correlation(rain, temp)

print correlation(entries, cum_entries)
"""