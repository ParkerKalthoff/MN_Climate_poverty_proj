import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

airData = pd.read_csv('ad_viz_plotval_data.csv')
povertyData = pd.read_csv('SAIPE_05-05-2023.csv')
#print(df.head())

def county_average_pol(site_counties):
    site_data = airData[airData['COUNTY'] == site_counties]
    pm25_mean = site_data['Daily Mean PM2.5 Concentration'].mean()
    aqi_mean = site_data['DAILY_AQI_VALUE'].mean()
    return pm25_mean, aqi_mean

def county_unique_names():
    county_names = airData['COUNTY'].unique().tolist()
    return county_names

def site_poverty(site_county):
    site_data = povertyData[povertyData["Name"] == site_county]
    povertyRate = site_data.iloc[0]['Percent in Poverty']
    return povertyRate

counties = county_unique_names()

povertyRates = []
averageAQIs = []
averagePMs = []

for county in counties:
    temp = county_average_pol(county)
    averagePMs.append(temp[0])
    averageAQIs.append(temp[1])
    povertyRates.append(site_poverty(county))

x = povertyRates # Your x-axis values
y = averageAQIs # Your y-axis values

plt.scatter(x, y) # Create scatter plot
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x, p(x), "r--")
plt.xlabel('Poverty Rate') # Set x-axis label
plt.ylabel('Average AQI') # Set y-axis label
plt.title('Poverty Rate against AQI') # Set title of scatter plot
plt.show()

#x = povertyRates # Your x-axis values
y = averagePMs # Your y-axis values

plt.scatter(x, y) # Create scatter plot
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x, p(x), "r--")
plt.xlabel('Poverty Rate') # Set x-axis label
plt.ylabel('Average PM 2.5 Rate') # Set y-axis label
plt.title('Poverty Rate against PM 2.5') # Set title of scatter plot
plt.show()