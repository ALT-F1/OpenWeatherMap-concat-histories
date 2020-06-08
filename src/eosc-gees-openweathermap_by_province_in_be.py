# %% [code]
# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import pandas as pd
from altf1be_helpers import AltF1BeHelpers
from bpost_be_postal_code_helpers import BPost_postal_codes
import time
import datetime
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 5GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All"
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

# %% [markdown]
# # FEAT: requirements
#
# Pour gerer la variabilité on pourrait stocker par jour plusieurs quantiles de la variable: par exemple si en province de Antwerp on prend 10 villes, on stocke les quantiles à 25-50-75% . L’important est que j’aie une valeur par jour et par province
#
# See https://covid19analyt-oho5182.slack.com/archives/C013F1FUDME/p1590487917005000

# %% [code]
# import libraries

# %% [code]
# Set the directories where the extract are

history_city_dir = "/kaggle/input/openweathermap-historical"

# %% [code]
# instanciate required classes

bpost_postal_codes = BPost_postal_codes()
df_postal_codes_in_be = bpost_postal_codes.df_postal_codes_in_be

# %% [markdown]
# # TRANSFORM:Translate the provinces from NL to FR

# %% [code]


def translate_provinces_in_french(df_postal_codes_in_be):
    df_postal_codes_in_be.loc[df_postal_codes_in_be['Province'] == 'ANTWERPEN', [
        'Province']] = 'ANVERS'
    df_postal_codes_in_be.loc[df_postal_codes_in_be['Province'] == 'BRUSSEL', [
        'Province']] = 'BRUXELLES'
    df_postal_codes_in_be.loc[df_postal_codes_in_be['Province'] == 'HENEGOUWEN', [
        'Province']] = 'HAINAUT'
    df_postal_codes_in_be.loc[df_postal_codes_in_be['Province'] == 'LIMBURG', [
        'Province']] = 'LIMBOURG'
    df_postal_codes_in_be.loc[df_postal_codes_in_be['Province'] == 'LUIK', [
        'Province']] = 'LIEGE'
    df_postal_codes_in_be.loc[df_postal_codes_in_be['Province'] == 'LUXEMBURG', [
        'Province']] = 'LUXEMBOURG'
    df_postal_codes_in_be.loc[df_postal_codes_in_be['Province'] == 'NAMEN', [
        'Province']] = 'NAMUR'
    df_postal_codes_in_be.loc[df_postal_codes_in_be['Province']
                              == 'OOST-VLAANDEREN', ['Province']] = 'FLANDRE-ORIENTALE'
    df_postal_codes_in_be.loc[df_postal_codes_in_be['Province']
                              == 'WEST-VLAANDEREN', ['Province']] = 'FLANDRE-OCCIDENTALE'
    df_postal_codes_in_be.loc[df_postal_codes_in_be['Province']
                              == 'VLAAMS-BRABANT', ['Province']] = 'BRABANT FLAMAND'
    df_postal_codes_in_be.loc[df_postal_codes_in_be['Province']
                              == 'WAALS-BRABANT', ['Province']] = 'BRABANT WALLON'
    return df_postal_codes_in_be

# %% [code]
# group by province


df_postal_codes_in_be = translate_provinces_in_french(df_postal_codes_in_be)
df_grouped_by_province = df_postal_codes_in_be.groupby(['Province'])[
    'Code postal'].apply(set)
df_grouped_by_province

# %% [markdown]
# # INITIALIZATIONS: filenames pattern

# %% [code]
openweathermap_org_weather_directory = "kaggle/input/openweathermap-org/"

# %% [code]
df_postal_codes_in_be.columns

# %% [code]
# concatenate the cities in each province


def concatenate_cities_in_each_province(postal_codes, year=2020, months=[3]):
    df = pd.DataFrame()

    first_day_of_the_month, last_day_of_the_month = AltF1BeHelpers.get_first_and_last_day_of_the_month(
        year=year, month=months[len(months)-1])

    for city_postal_code in postal_codes:
        print(f"city_postal_code: {city_postal_code}")
        city_name = df_postal_codes_in_be.loc[df_postal_codes_in_be['Code postal']
                                              == city_postal_code]['Commune principale normalized']
        print(f"Commune city_name: {city_name}")
        city_name = df_postal_codes_in_be.loc[df_postal_codes_in_be['Code postal']
                                              == city_postal_code]['Localité normalized']
        print(f"Localité city_name: {city_name}")

        filename = (f'{city_postal_code.zfill(4)}_{city_name}_from_{first_day_of_the_month.strftime("%Y-%m-%d_%Hh%M")}_to_{last_day_of_the_month.strftime("%Y-%m-%d_%Hh%M")}-{first_day_of_the_month.strftime("%s")}_to_{last_day_of_the_month.strftime("%s")}')
        print(f"filename: {filename}")
        csv_path = os.path.join(openweathermap_org_weather_directory,
                                f'{city_postal_code.zfill(4)}_{city_name}_from_{first_day_of_the_month.strftime("%Y-%m-%d_%Hh%M")}_to_{last_day_of_the_month.strftime("%Y-%m-%d_%Hh%M")}-{first_day_of_the_month.strftime("%s")}_to_{last_day_of_the_month.strftime("%s")}')
        print(f"{csv_path}")
        df_new_cities_per_province = pd.read_csv(f"{csv_path}.csv", sep=',')

        df = pd.concat([df, df_postal_codes_in_be])
    df
    return df

# %% [code]
# compute the quantiles

# %% [markdown]
# # LOAD : for each Postal code we look for the quantile

# %% [code]
# LOAD: for each file in input/openweathermap_org


# %% [code]
df_grouped_by_province.index

# %% [code]
PROVINCE_NOT_FOUND = -1  # const


def get_province_from(postal_code):
    """
    if the Belgian province for a postal code
    """
    index = 0
    # print(type(df_grouped_by_province))
    for cities_in_province in df_grouped_by_province:
        is_postal_code_in_list = True if postal_code in cities_in_province else False
        if is_postal_code_in_list:
            # print(df_grouped_by_province)
            # print(type(cities_in_province))
            # print(f"{cities_in_province}")
            # print(f"{is_postal_code_in_list}")
            # print(f"{df_grouped_by_province.index}")
            return df_grouped_by_province.index[index]
        index = index + 1

    return PROVINCE_NOT_FOUND


# %% [code]
# keep: test from which province comes this postal code
print(get_province_from(1932))

# %% [code]


def get_normalized_province(province):
    return province.replace('-', '')

# %% [code]
# keep the code


def append_df_per_province(df, filename):
    postal_code = filename[:4]
    province = get_province_from(postal_code=int(postal_code))
    df['Province'] = province
    df['Postal code'] = postal_code
    df['date'] = df['dt'].apply(
        lambda x: time.strftime('%Y-%m-%d', time.localtime(x)))
    print(f"{postal_code}-{province}")
    # print(df)
    # df.columns
    #current_province = df_postal_codes_in_be.loc[df_postal_codes_in_be['Code postal'] == df.loc['Province']]
    return df


# %% [code]
# keep the code: create one DataFrame containing all CSV containing March 01 to May 22, 2020
t0 = time.clock()
index = 0
df_provinces_collection = pd.DataFrame()  # one dataframe per province

dir_data = os.path.join(os.path.abspath(
    os.getcwd()), "src", openweathermap_org_weather_directory
)
for dirname, _, filenames in os.walk(dir_data):
    for filename in filenames:
        print(f"loading: {index}/{len(filenames)}")
        csv_path = os.path.join(dirname, filename)
        print(filename)
        df_provinces_collection = pd.concat(
            [df_provinces_collection, append_df_per_province(
                pd.read_csv(csv_path, sep=','), filename)]
        )
        index = index+1
t1 = time.clock() - t0
print("Time elapsed: ", t1 - t0)  # CPU seconds elapsed (floating point)
print("finished\n")
df_provinces_collection

# %% [code]
# store current dataframe containing the weather of all cities from March 01 to May 22, 2020
df_provinces_collection.to_csv("df_provinces_collection.csv")
# too long df_provinces_collection.to_excel("df_provinces_collection.xlsx")
df_provinces_collection.to_pickle("df_provinces_collection.pkl")
# with pd.HDFStore('df_provinces_collection_01.h5', mode='w') as f:
#    f.append(df_provinces_collection, key='df', format='fixed', data_columns=df_provinces_collection.columns)

#df_provinces_collection.to_hdf("df_provinces_collection.hdf5", format='table', key='/provinces')

# %% [code]

df_quantiles = df_provinces_collection.copy(deep=True)

# %% [code]

df_quantiles.columns

# %% [code]
# keep: add a column with a date based on dt
df_quantiles['date'] = df_quantiles['dt'].apply(
    lambda x: time.strftime('%Y-%m-%d', time.localtime(x)))

# %% [code]
df_quantiles

# %% [code]
total = 0
for province in df_quantiles['Province'].unique():
    total = total + df_quantiles[df_quantiles['Province'] == province].shape[0]
    print(
        f"{province}-{df_quantiles[df_quantiles['Province'] == province].shape}")
print(f"{total}")

# %% [code]
current_province = df_quantiles.loc[df_quantiles['Province'] == "BRUXELLES"]
current_province

# %% [code]
current_province.columns

# %% [code]
current_date_df = current_province.loc[current_province['date']
                                       == '2020-03-01']
current_date_df.head(3)

# %% [code]
current_province.shape

# %% [code]
new_df = pd.DataFrame(columns=['message', 'cod', 'city_id', 'dt', 'main.temp25',
                               'main.temp50', 'main.temp75',
                               'main.feels_like25', 'main.feels_like50', 'main.feels_like75',
                               'main.pressure25', 'main.pressure50', 'main.pressure75',
                               'main.humidity25', 'main.humidity50', 'main.humidity75',
                               'main.temp_min25', 'main.temp_min50', 'main.temp_min75',
                               'main.temp_max25', 'main.temp_max50', 'main.temp_max75',
                               'wind.speed25', 'wind.speed50', 'wind.speed75',
                               'wind.deg25', 'wind.deg50', 'wind.deg75',
                               'Province',
                               'date'])
# 'clouds.all', 'weather.id',
#'weather.main', 'weather.description', 'weather.icon',

# %% [code]
current_date_df['main.temp'].quantile(.25)

# %% [code]
new_df.loc[0, 'main.temp25'] = current_date_df['main.temp'].quantile(.25)
new_df.loc[0, 'main.temp50'] = current_date_df['main.temp'].quantile(.50)

# %% [code]
new_df

# %% [code]


def add_quantiles(new_df):
    # per province
    columns = ['message', 'cod', 'dt',
               'Province',
               'date',
               'main.temp25', 'main.temp50', 'main.temp75',
               'main.feels_like25', 'main.feels_like50', 'main.feels_like75',
               'main.pressure25', 'main.pressure50', 'main.pressure75',
               'main.humidity25', 'main.humidity50', 'main.humidity75',
               'main.temp_min25', 'main.temp_min50', 'main.temp_min75',
               'main.temp_max25', 'main.temp_max50', 'main.temp_max75',
               'wind.speed25', 'wind.speed50', 'wind.speed75',
               'wind.deg25', 'wind.deg50', 'wind.deg75',
               ]
    new_df = pd.DataFrame(columns=columns)
    lines = 0

    df_quantiles_sorted = df_quantiles.sort_values(['Province', 'dt'])

    for province in df_quantiles_sorted['Province'].unique():
        # per day
        # print(f"************************************************************************")
        # print(f"************************************************************************")
        # print(f"************************************************************************")
        print(f"************************************************************************")

        print(f"PROVINCE: {province}")
        for date in df_quantiles_sorted['date'].unique():
            print(f"LINES: {lines} - {new_df.shape}")
            lines = lines+1
            print(
                f"************************************************************************")
            # print(f"************************************************************************")
            # print(f"************************************************************************")
            print(f"DATE : {date}")
            #new_row = pd.DataFrame(columns=columns)
            # compute quantile
            current_date_df = df_quantiles_sorted.loc[df_quantiles_sorted['date'] == date]

            new_row = pd.DataFrame([[
                current_date_df.iloc[0]['message'], current_date_df.iloc[0]['cod'], current_date_df.iloc[0]['dt'], province, date, current_date_df['main.temp'].quantile(.25), current_date_df['main.temp'].quantile(.50), current_date_df['main.temp'].quantile(.75), current_date_df['main.feels_like'].quantile(.25), current_date_df['main.feels_like'].quantile(.50), current_date_df['main.feels_like'].quantile(.75), current_date_df['main.pressure'].quantile(.25), current_date_df['main.pressure'].quantile(.50), current_date_df['main.pressure'].quantile(.75), current_date_df['main.humidity'].quantile(.25), current_date_df['main.humidity'].quantile(
                    .50), current_date_df['main.humidity'].quantile(.75), current_date_df['main.temp_min'].quantile(.25), current_date_df['main.temp_min'].quantile(.50), current_date_df['main.temp_min'].quantile(.75), current_date_df['main.temp_max'].quantile(.25), current_date_df['main.temp_max'].quantile(.50), current_date_df['main.temp_max'].quantile(.75), current_date_df['wind.speed'].quantile(.25), current_date_df['wind.speed'].quantile(.50), current_date_df['wind.speed'].quantile(.75), current_date_df['wind.deg'].quantile(.25), current_date_df['wind.deg'].quantile(.50), current_date_df['wind.deg'].quantile(.75)
            ]],
                columns=columns)

            #new_row = pd.DataFrame([date], columns=['message'])
            print(f"new_row.shape : {new_row.shape}")
            print(f"new_row : {new_row}")
            #print(f"new_row.columns : {new_row.columns}")
            new_df = new_df.append(new_row, ignore_index=True)
    return new_df

# %% [markdown]
# # load the df_provinces_collection and work


# %% [code]
df_with_quantiles = pd.DataFrame()
df_with_quantiles = add_quantiles(df_with_quantiles)

# %% [code]
df_with_quantiles.shape

# %% [code]
df_with_quantiles

# %% [code]
df_with_quantiles_cleaned = df_with_quantiles[df_with_quantiles['Province'] != -1]

# %% [code]
df_with_quantiles_cleaned.shape

# %% [code]
df_with_quantiles.to_csv(
    "openweather_map-belgium-per_province_per_day_with_quantiles.csv")
df_with_quantiles.to_excel(
    "openweather_map-belgium-per_province_per_day_with_quantiles.xlsx")

# %% [code]
df_with_quantiles_cleaned.to_csv(
    "openweather_map-belgium-per_province_per_day_with_quantiles_cleaned.csv")
df_with_quantiles_cleaned.to_excel(
    "openweather_map-belgium-per_province_per_day_with_quantiles_cleaned.xlsx")

# %% [markdown]
# # FINISH - THIS IS THE END

# %% [code]
df_quantiles_sorted = df_quantiles.sort_values(['Province', 'dt'])

# %% [code]
df_quantiles_sorted.shape

# %% [code]
province = "ANVERS"
df_for_one_day_one_province = df_quantiles_sorted.loc[df_quantiles_sorted['Province'] == province]

# %% [code]
df_for_one_day_one_province.shape

# %% [code]
date = "2020-03-01"
df_current_date = df_for_one_day_one_province.loc[df_for_one_day_one_province['date'] == date]

# %% [code]
df_current_date.shape

# %% [code]
current_date_df['main.temp'].quantile(.25)

# %% [code]
columns = ['message', 'cod', 'dt',
           'Province',
           'date',
           'main.temp25', 'main.temp50', 'main.temp75',
           'main.feels_like25', 'main.feels_like50', 'main.feels_like75',
           'main.pressure25', 'main.pressure50', 'main.pressure75',
           'main.humidity25', 'main.humidity50', 'main.humidity75',
           'main.temp_min25', 'main.temp_min50', 'main.temp_min75',
           'main.temp_max25', 'main.temp_max50', 'main.temp_max75',
           'wind.speed25', 'wind.speed50', 'wind.speed75',
           'wind.deg25', 'wind.deg50', 'wind.deg75',
           ]
new_row = pd.DataFrame([[
    current_date_df.iloc[0]['message'], current_date_df.iloc[0]['cod'], current_date_df.iloc[0]['dt'], province, date, current_date_df['main.temp'].quantile(.25), current_date_df['main.temp'].quantile(.50), current_date_df['main.temp'].quantile(.75), current_date_df['main.feels_like'].quantile(.25), current_date_df['main.feels_like'].quantile(.50), current_date_df['main.feels_like'].quantile(.75), current_date_df['main.pressure'].quantile(.25), current_date_df['main.pressure'].quantile(.50), current_date_df['main.pressure'].quantile(.75), current_date_df['main.humidity'].quantile(.25), current_date_df['main.humidity'].quantile(
        .50), current_date_df['main.humidity'].quantile(.75), current_date_df['main.temp_min'].quantile(.25), current_date_df['main.temp_min'].quantile(.50), current_date_df['main.temp_min'].quantile(.75), current_date_df['main.temp_max'].quantile(.25), current_date_df['main.temp_max'].quantile(.50), current_date_df['main.temp_max'].quantile(.75), current_date_df['wind.speed'].quantile(.25), current_date_df['wind.speed'].quantile(.50), current_date_df['wind.speed'].quantile(.75), current_date_df['wind.deg'].quantile(.25), current_date_df['wind.deg'].quantile(.50), current_date_df['wind.deg'].quantile(.75)
]],
    columns=columns)

# %% [code]
new_row.columns

# %% [code]
new_row

# %% [code]
new_row.shape

# %% [code]
new_df = pd.DataFrame(columns=columns)
new_df = new_df.append(new_row, verify_integrity=True,
                       ignore_index=True, sort=False)
new_df.shape

# %% [code]
new_df

# %% [code]
new_df.columns

# %% [code]

df1 = pd.DataFrame({'Name': ['Pankaj', 'Lisa'], 'ID': [1, 2]})
df2 = pd.DataFrame({'Name': ['David'], 'ID': [3]})

print(df1)
print(df2)

df3 = df1.append(df2)
print('\nResult DataFrame:\n', df3)

# %% [code]
df_final = pd.DataFrame(columns=['main.temp25'])

# %% [code]
df_final['main.temp25'] = current_date_df['main.temp'].quantile(.25)

# %% [code]
df_final.shape

# %% [code]
current_date_df['main.temp'].quantile(.50)

# %% [code]


# %% [code]
df_final['main.temp50'] = current_date_df['main.temp'].quantile(.50)
current_date_df['main.temp75'] = current_date_df['main.temp'].quantile(.75)

current_date_df['main.feels_like25'] = current_date_df['main.feels_like'].quantile(
    .25)
current_date_df['main.feels_like50'] = current_date_df['main.feels_like'].quantile(
    .50)
current_date_df['main.feels_like75'] = current_date_df['main.feels_like'].quantile(
    .75)

current_date_df['main.pressure25'] = current_date_df['main.pressure'].quantile(
    .25)
current_date_df['main.pressure50'] = current_date_df['main.pressure'].quantile(
    .50)
current_date_df['main.pressure75'] = current_date_df['main.pressure'].quantile(
    .75)

current_date_df['main.humidity25'] = current_date_df['main.humidity'].quantile(
    .25)
current_date_df['main.humidity50'] = current_date_df['main.humidity'].quantile(
    .50)
current_date_df['main.humidity75'] = current_date_df['main.humidity'].quantile(
    .75)

current_date_df['main.temp_min25'] = current_date_df['main.temp_min'].quantile(
    .25)
current_date_df['main.temp_min50'] = current_date_df['main.temp_min'].quantile(
    .50)
current_date_df['main.temp_min75'] = current_date_df['main.temp_min'].quantile(
    .75)

current_date_df['main.temp_max25'] = current_date_df['main.temp_max'].quantile(
    .25)
current_date_df['main.temp_max50'] = current_date_df['main.temp_max'].quantile(
    .50)
current_date_df['main.temp_max75'] = current_date_df['main.temp_max'].quantile(
    .75)

current_date_df['wind.speed25'] = current_date_df['wind.speed'].quantile(.25)
current_date_df['wind.speed50'] = current_date_df['wind.speed'].quantile(.50)
current_date_df['wind.speed75'] = current_date_df['wind.speed'].quantile(.75)

current_date_df['wind.deg25'] = current_date_df['wind.deg'].quantile(.25)
current_date_df['wind.deg50'] = current_date_df['wind.deg'].quantile(.50)
current_date_df['wind.deg75'] = current_date_df['wind.deg'].quantile(.75)

# %% [code]
current_date_df.columns

# %% [code]
