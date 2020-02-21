import pandas as pd

#create dataframe
df = pd.read_csv("weather.csv")
#print(df)
print(df['Temperature'].max())

print(df[['EST','Temperature','WindSpeedMPH', 'Events']]     [df['Events']=='Rain'])
