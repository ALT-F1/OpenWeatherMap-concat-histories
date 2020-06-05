# %% [code]
# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
# for dirname, _, filenames in os.walk('/kaggle/input'):
#     for filename in filenames:
#         print(os.path.join(dirname, filename))

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
import datetime
import time
from time import perf_counter
from bpost_be_postal_code import BPost_postal_codes
from altf1be_helpers import is_interactive

# %% [code]
# variable initializations
output_directory = ""
output_kaggle_directory = os.path.join(
    "kaggle", "output", "kaggle", "working"
)

if (not is_interactive()):
    output_directory = os.path.join(
        os.path.abspath(os.getcwd()),
        "src",
        output_kaggle_directory)

print(f"output_directory : {output_directory}")

# create directories
from pathlib import Path

Path(output_directory).mkdir(parents=True, exist_ok=True)

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
t1_start = perf_counter()
index = 0
df_provinces_collection = pd.DataFrame()  # one dataframe per province

if (not is_interactive()):

    openweathermap_org_weather_directory = os.path.join(
        os.path.abspath(os.getcwd()),
        "src",
        openweathermap_org_weather_directory)

print(
    f"openweathermap_org_weather_directory: {openweathermap_org_weather_directory}")

for dirname, _, filenames in os.walk(openweathermap_org_weather_directory):
    for filename in filenames:
        if filename.endswith('.csv'):
            print(f"loading: {index}/{len(filenames)}")
            csv_path = os.path.join(dirname, filename)
            print(filename)
            df_provinces_collection = pd.concat(
                [df_provinces_collection, append_df_per_province(
                    pd.read_csv(csv_path, sep=','), filename)]
            )
        index = index+1

t1_stop = perf_counter()

print("Elapsed time:", t1_stop, t1_start)


print("Elapsed time during the whole program in seconds:",
      t1_stop-t1_start)
print(f"Just finished concatenating the files")
df_provinces_collection

# %% [code]

output_filename = f"{os.path.join(output_directory, 'df_provinces_collection')}"
print(f"We are storing CSV and Pickle files, wait a few seconds...")
# store current dataframe containing the weather of all cities from March 01 to May 22, 2020
df_provinces_collection.to_csv(f"{output_filename}.csv")
# too long df_provinces_collection.to_excel("df_provinces_collection.xlsx")
df_provinces_collection.to_pickle(f"{output_filename}.pkl")
print(f"file are stored here : {output_directory}")