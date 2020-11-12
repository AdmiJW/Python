
# # 1.0 - Sea Level Predictor
#
# ![Bar](https://github.com/AdmiJW/Items/blob/master/SeperatingBars/Horizontalbar_red.png?raw=true)
#
# In this assignment, we will be fetching the data of the global sea levels from year 1880 up until 2014. Then, a scatterplot will be plotted for the sea levels, then 2 line of best fit will be plotted on the graph:
# * One line of best fit using ALL the data, meaning from year 1880 up until 2014
# * One line of best fit using data starting from 2000 ONLY, up until the year 2014

# ![Bar](https://github.com/AdmiJW/Items/blob/master/SeperatingBars/Horizontalbar_red.png?raw=true)
#
# ### 1.1 - Fetching CSV in More Traditional Way
#
# As usual, the more 'traditional' way of fetching CSV are using the `requests` method. However this way we will have to construct the `DataFrame` ourselves, and converting datatype of each column ourselves.


# Let's first import the necessary libraries first:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

import requests
from typing import *

# Here is the traditional way of fetching the CSV data, using requests library
def read_csv_using_requests(url: str, delimiter: str = ',') -> List:
    if (len(delimiter) != 1):
        raise ValueError("Length of delimiter must be 1! Provided: {}".format(delimiter))
    try:
        response: requests.Response = requests.request('GET', url)
        if (response.status_code != 200):
            raise ConnectionError()
    except:
        raise ConnectionError("Error Occurred while trying to fetch the CSV with given url: {}".format(url))

    # Split the text into lines, then split each line using the delimiter
    values = response.text.split('\r\n')
    values = list(map(lambda x: x.split(delimiter), values))

    return values




# ![Bar](https://github.com/AdmiJW/Items/blob/master/SeperatingBars/Horizontalbar_red.png?raw=true)
#
# ### 1.2 - Fetching CSV in Pandas Way
#
# `pandas` comes with a handful function of reading CSV files provided url. This is way more convenient than fetching it using `requests` as it involves less line of code, and even already prepared a lot of parameter list for us to customize the behavior of CSV fetching!

# apper function to simplify the interface of reading CSV using pandas. Only some functionalities are preserved
def read_csv_using_pandas(url: str, delimiter: str = ',', header: bool = False):
    if (len(delimiter) != 1):
        raise ValueError('Length of delimiter must be 1! Provided: {}'.format(delimiter))

    df = pd.read_csv(url, sep=delimiter, header=0 if header else None)

    return df



# ![Bar](https://github.com/AdmiJW/Items/blob/master/SeperatingBars/Horizontalbar_blue.png?raw=true)
#
# # 2.0 - Fetching the Data and Modifying DataFrame
#
# ![Bar](https://github.com/AdmiJW/Items/blob/master/SeperatingBars/Horizontalbar_blue.png?raw=true)
#
# Now in this section, we are going to fetch the data in the traditional way, and setting the column names, index, and the datatypes of the columns ourselves.

# ![Bar](https://github.com/AdmiJW/Items/blob/master/SeperatingBars/Horizontalbar_blue.png?raw=true)
#
# ### 2.1 - Fetching the Data
#
# Fetch the data using the 'traditional' way function defined above


arrays = read_csv_using_requests('https://raw.githubusercontent.com/AdmiJW/Items/master/epa-sea-level_csv.csv')

df = pd.DataFrame(arrays)

# ![Bar](https://github.com/AdmiJW/Items/blob/master/SeperatingBars/Horizontalbar_blue.png?raw=true)
#
# ### 2.2 - Set the Column Names
#
# The first row of data is actually the column names. Set that and drop the first row afterwards

# In[308]:


df.columns = df.iloc[0]

df.drop(0, axis=0, inplace=True)

# ![Bar](https://github.com/AdmiJW/Items/blob/master/SeperatingBars/Horizontalbar_blue.png?raw=true)
#
# ### 2.3 - Deleting the Last Few Invalid Rows
#
# We can see that the last row is either empty or doesn't contain useful data. We can drop them



df = df.iloc[:-2]

# ![Bar](https://github.com/AdmiJW/Items/blob/master/SeperatingBars/Horizontalbar_blue.png?raw=true)
#
# ### 2.4 - Setting the Year Column as Index
#
# We shall be identifying each row based on the year that data is recorded. Therefore we set the year column as the index



df.index = df.Year

df.drop('Year', axis=1, inplace=True)

# ![Bar](https://github.com/AdmiJW/Items/blob/master/SeperatingBars/Horizontalbar_blue.png?raw=true)
#
# ### 2.5 - Preserve only the Year
#
# We can see that for the year column, the month and date are actually repeated, only the year are changing. Therefore we can simplify the column so that it contains only the year



# Map each date string so that only the first 4 characters (YEar) are obtained
substrArr = df.index.map(lambda s: s[:4])

# Set the index, while converting it into data type of int16
df.index = substrArr.astype(np.int16)


# ![Bar](https://github.com/AdmiJW/Items/blob/master/SeperatingBars/Horizontalbar_blue.png?raw=true)
#
# ### 2.6 - A Function that Finds Min and Max, or Errors in Numeric Column
#
# We can write a function that checks for a column that are supposed to contain numeric data. If it is valid (All numeric data),
# then return the max and min of the entire column, else it will return the row indices that contain error



# If the column is valid, will return [ True, [min, max] ]
# Otherwise if column is invalid, will reutrn [ False, [ indices of invalid data...] ]
def check_numeric_column(series: pd.Series) -> List:
    result = [True, list()]
    min_val = float('inf')
    max_val = -float('inf')

    # Series requires us to use iloc, and will raise KeyError if we don't. THerefore catch the exception
    for i in range(len(series)):
        try:
            n = float(series[i])
        except:
            try:
                n = float(series.iloc[i])  # Maybe it is an KeyError. Try to use iloc instead!
            except:
                result[0] = False
                result[1].append(i)
                continue

        min_val = min(n, min_val)
        max_val = max(n, max_val)

    # If the first item is True, that means column is valid. Append min and max
    if result[0]:
        result[1].append(min_val)
        result[1].append(max_val)

    return result



# ![Bar](https://github.com/AdmiJW/Items/blob/master/SeperatingBars/Horizontalbar_blue.png?raw=true)
#
# ### 2.7 - Converting All Columns into Float Datatype
#
# All of those columns are supposed to contain floating point values. Therefore we will be converting all of the columns into the respective datatype.

# In[314]:


##################################
# CSIRO Adjusted Sea Level Column
##################################

print(check_numeric_column(df['CSIRO Adjusted Sea Level']))  # [True, [-0.440944881, 9.326771644] ]

df['CSIRO Adjusted Sea Level'] = df['CSIRO Adjusted Sea Level'].astype(np.float64)


##################################
# Lower Error Bound
##################################

print(check_numeric_column(df['Lower Error Bound']))  # [True, [-1.346456692, 8.992125975] ]

df['Lower Error Bound'] = df['Lower Error Bound'].astype(np.float64)



##################################
# Upper Error Bound
##################################

print(check_numeric_column(df['Upper Error Bound']))  # [True, [0.464566929, 9.661417313] ]

df['Upper Error Bound'] = df['Upper Error Bound'].astype(np.float64)


##################################
# NOAA Adjusted Sea Level
##################################

print(check_numeric_column(df['NOAA Adjusted Sea Level']))  # [False, [...] ]

# The error is mainly due to empty strings. We can see that most of the years does not have entries for NOAA Adjusted Sea Level
# until recent years only. Therefore for it to parse correctly, first replace empty strings to np.nan

correctedNan = df['NOAA Adjusted Sea Level'].map(lambda x: x if len(x) else np.nan)

# Now only it can be interpreted
print(check_numeric_column(correctedNan))  # [True, [ 6.297493046, 8.546648227] ]

# Convert the datatype
df['NOAA Adjusted Sea Level'] = correctedNan.astype(np.float64)



# ![Bar](https://github.com/AdmiJW/Items/blob/master/SeperatingBars/Horizontalbar_green.png?raw=true)
#
# # 3.0 - Plotting
#
# ![Bar](https://github.com/AdmiJW/Items/blob/master/SeperatingBars/Horizontalbar_green.png?raw=true)
#
# Now we have to plot the actual graph. First of all, we are going to plot the scatterplot of the sealevel against year. Then,
# we will be going to add 2 line of best fit and extrapolate it up until year 2050.
# * One using data from the beginning of data - year 1880
# * One using data from the recent years - year 2000
#
# Since this involves drawing of straight lines, let's make a little function which takes in gradient, y-intercept, and a x value, to calculate the y value
#

# In[319]:


# Little function to calculate the y, given m, x and c. ( y = mx + c )
def calculate_y(m: float, c: float, x: float) -> float:
    return m * x + c




def draw_plot():
    sns.set_style('whitegrid')
    #########################
    # Create scatter plot
    #########################
    plt.figure(figsize=(16, 10))

    axes = plt.scatter(df.index, df['CSIRO Adjusted Sea Level'], c='#3498db', s=20, linewidths=1, edgecolors='#2980b9')

    ################################
    # Create first line of best fit
    #################################
    # To get the line of best fit, we need the equation in the form y=mx+c. We need to obtain the gradient, m and the
    # y intercept, c which the scipy.stats will do for us!
    # After getting the m and c value, we need to draw a straight line, which start from minimum of the years, until 2050.
    # We need to obtain the y value for us to be able to plot the line up

    slope, intercept, _, _, _ = stats.linregress(df.index, df['CSIRO Adjusted Sea Level'])

    # X and Y values to plot
    x_values1 = np.arange(df.index.min(), 2050)

    y_values1 = [calculate_y(slope, intercept, x) for x in x_values1]

    plt.plot(x_values1, y_values1, 'r:', label=f'Extrapolate from Year {df.index.min()}', )

    #####################################
    # Create second line of best fit
    #####################################
    slope, intercept, _, _, _ = stats.linregress(df.loc[2000:].index, df.loc[2000:]['CSIRO Adjusted Sea Level'])

    # X values to plot
    x_values2 = np.arange(2000, 2050)
    # Y values to plot
    y_values2 = [calculate_y(slope, intercept, x) for x in x_values2]

    print(y_values1)

    plt.plot(x_values2, y_values2, 'b--', label='Extrapolate from Year 2000')

    ##########################
    # Add labels and title
    ###########################
    plt.title('Rise in Sea Level', fontsize='xx-large')
    plt.xlabel('Year', fontsize='x-large')
    plt.ylabel('Sea Level (inches)', fontsize='x-large')
    plt.xticks([x * 25 + 1850 for x in range(10)])
    plt.legend(fontsize='large', shadow=True, borderpad=1)

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()


# In[372]:


draw_plot()

# In[ ]:




