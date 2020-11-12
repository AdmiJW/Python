import requests
from typing import *
import pandas as pd
import numpy as np


def fetchCsv( url: str, delimiter: str = ',' ) -> List:
    #   Invalid delimiter of csv provided. Just raise an exception
    if ( len(delimiter) != 1 ):
        raise ValueError("Delimiter must be a single character!")

    #   Fetch the csv file at the provided url
    response = requests.get( url )

    #   Unable to fetch the csv file in provided url. Raise an exception for that
    if (response.status_code != 200 ):
        raise ConnectionError("Error: Unable to fetch the csv file at {}\n\
                status code: {}".format(url, response.status_code) )

    #   Obtain the text, split them into lines (Based on \r\n )
    responseText = response.text
    responseList = responseText.split('\r\n')

    #   Map each line into a list of values split by the delimiter specified.
    responseList = list( map( lambda s: s.split( delimiter ), responseList) )

    return responseList


def pandasFetchCSV(url:str, delimiter:str = ',', header:bool = False):
    df:Union[pd.io.parsers.TextFileReader, pd.Series, pd.DataFrame, None] = pd.read_csv(
        url,
        sep=delimiter,
        header=0 if header else None)

    return df


# This is a custom function which take in a Series of string, which supposed to be integers.
# It will check for each value, if it is ALL valid integers. This is to safely parse into correct datatype
def checkStringIntValues(series: pd.Series, can_negative: bool = False) -> List:
    result = [True, list()]
    vmax = -float('inf')
    vmin = float('inf')

    for i in series.index:
        try:
            num = int(series[i])

            if not can_negative and num < 0:
                raise ValueError("Negative values")

            vmax = max(vmax, num)
            vmin = min(vmin, num)
        except:
            result[0] = False
            result[1].append(i)

    if len(result[1]) == 0:
        result[1].append(vmin)
        result[1].append(vmax)

    return result




def calculate_demographic_data(print_data=True):


    listItems = fetchCsv('https://raw.githubusercontent.com/AdmiJW/Items/master/adult.data.csv')

    # Use the DataFrame constructor, passing in the List
    df = pd.DataFrame(listItems)

    # Set the name of the DataFrame
    df.name = 'Demographic Analysis Data'

    # Set the column names of the DataFrame, which is on the first row
    df.columns = df.iloc[0]
    # Since the first row is now column name, the first row shall be dropped now
    df.drop(0, inplace=True)

    # Remove the last 2 rows which is Empty rows
    df = df.iloc[:-2]
    df.tail()

    ###########################################
    # age column > int8 (Since age really don't go high)
    ###########################################
    # Since highest value is only 90, we can safely use int8 as datatype
    df['age'] = df['age'].astype(np.int8)

    ###########################################
    # fnlwgt column. Let's see if there's any invalid numeric values
    ###########################################
    # Now we see values go up as high as 1484705. int32 shall be suitable
    df['fnlwgt'] = df['fnlwgt'].astype(np.int32)

    ############################################
    # education-num column. Let's see
    ###########################################
    # Only as low as 16. Use int8
    df['education-num'] = df['education-num'].astype(np.int8)

    ############################################
    # capital-gain column. Let's see
    ###########################################
    # A int32 will suffice
    df['capital-gain'] = df['capital-gain'].astype(np.int32)

    ############################################
    # capital-loss column. Let's see
    ###########################################
    # In this case maximum is only 4356, well within range of int16
    df['capital-loss'] = df['capital-loss'].astype(np.int16)

    ############################################
    # hours-per-week column. Let's see
    ###########################################
    # int8 is already more than enoguh
    df['hours-per-week'] = df['hours-per-week'].astype(np.int8)





    # This problem asks for a frequency table. This is how we actually check for
    # number of unique values! Use Series.value_counts() to get the result!
    Q1_ans = df['race'].value_counts()

    #-------------------------------------------------------

    # This problem asks for average age of men.
    # Unfortunately, pandas Series does not have a average function. However,
    # there is instead a sum() function. Use sum() divided by the number of entries

    male_mask = df.sex == 'Male'

    Q2_ans = df[male_mask].age.sum() / len(df[male_mask])

    # -------------------------------------------------------

    # This problem asks for number of people with 'Bachelors' value in its education
    # column, over all people, in percentage
    sample = len(df[df.education == 'Bachelors'])
    Q3_ans = sample / len(df) * 100

    # -------------------------------------------------------

    # This is a compounded query. We have to find
    # Those people which has advanced education
    # Those people which makes more than 50K

    # Basically, it is ( advanced edu & 50K ) / (50K)

    # To get boolean mask whether values is in a specified values list, use
    # isin() function
    advanced_edu_values = ['Bachelors', 'Masters', 'Doctorate']
    advanced_edu_mask = df.education.isin(advanced_edu_values)

    over_50K_mask = df.salary == '>50K'

    Q4_ans = len(df[(advanced_edu_mask) & (over_50K_mask)]) \
             / len(df[advanced_edu_mask]) * 100

    # -------------------------------------------------------

    # This problem requires
    # >    People with no advanced education. Just negate the last mask
    # >    People making more than 50K. Just use the last mask

    advanced_edu_values = ['Bachelors', 'Masters', 'Doctorate']
    advanced_edu_mask = df.education.isin(advanced_edu_values)
    no_advanced_edu_mask = ~advanced_edu_mask

    Q5_ans = len(df[(no_advanced_edu_mask) & (over_50K_mask)]) \
             / len(df[(no_advanced_edu_mask)]) * 100

    # -------------------------------------------------------

    # Just get the minimum of the hours-per-week column
    # Summary statistics

    Q6_ans = df['hours-per-week'].min()

    # -------------------------------------------------------

    # We will use the result of last query on this.
    # We need the mask of:
    # >    People working at minimum hour per week
    # >    People working at salary more than 50K

    min_hour = df['hours-per-week'].min()
    min_mask = df['hours-per-week'] == min_hour

    salary_mask = df.salary == '>50K'

    Q7_ans = len(df[min_mask & salary_mask]) / len(df[min_mask]) * 100

    # -------------------------------------------------------

    # This is a more complex query. We will approach this in series of steps
    # 1.    We need a frequency table for people in each country
    # 2.    We need a frequency table for people in each country earning
    #       >50K.
    # 3.    Divide those corresponding datas together. We will get percentage from
    #       it

    Nonefilter = df['native-country'] != '?'

    pop_country = df[Nonefilter]['native-country'].value_counts()

    salary_mask = df[Nonefilter].salary == '>50K'

    pop_country_rich = df[Nonefilter][salary_mask]['native-country'].value_counts()

    print(pop_country)
    print(pop_country_rich)

    country_percentage = pop_country_rich / pop_country * 100
    country_percentage.sort_values(ascending=False, inplace=True)

    Q8_1_ans = country_percentage.index[0];
    Q8_2_ans = country_percentage.max()

    # -------------------------------------------------------

    # We need:
    # >    Salary mask for those >50K
    # >    Country mask for India
    # >    Count values for occupation. Get the top value
    salary_mask = df.salary == '>50K'

    country_mask = df['native-country'] == 'India'

    occupations_series = df[salary_mask & country_mask].occupation

    Q9_ans = occupations_series.value_counts().index[0]

    #================================================

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = Q1_ans

    # What is the average age of men?
    average_age_men = Q2_ans

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = Q3_ans

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # percentage with salary >50K
    higher_education_rich = Q4_ans
    lower_education_rich = Q5_ans

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = Q6_ans


    rich_percentage = Q7_ans

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = Q8_1_ans
    highest_earning_country_percentage = Q8_2_ans

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = Q9_ans

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }



calculate_demographic_data(print_data=True)