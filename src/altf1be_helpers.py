# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
import datetime
import calendar

# for dirname, _, filenames in os.walk('/kaggle/input'):
#    for filename in filenames:
#        print(os.path.join(dirname, filename))

# You can write up to 5GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All"
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

def is_interactive():
    # return True if running on Kaggle
    try:
        return 'runtime' in get_ipython().config.IPKernelApp.connection_file
    except NameError:
        return False

def unicode_to_ascii(a):
    """
    remove accents and apostrophes
    """
    import unidecode
    # def remove_accents_apostrophe(a):
    a = unidecode.unidecode(a)  # remove accent
    a = a.replace("'", '')  # remove apostrophe
    return a

def get_first_and_last_day_of_the_month(year, month):
   
    first_day_datetime = datetime.datetime(year=year, month=month, day=1, hour=0, minute=0)
    printable_start_datetime = first_day_datetime.strftime("%Y-%m-%d_%Hh%M")
      
    last_day_datetime = datetime.datetime(year=year, month=month, day=calendar.monthrange(year,month)[1], hour=23, minute=0)
    printable_last_datetime = last_day_datetime.strftime("%Y-%m-%d_%Hh%M")
    
    print(f"{printable_start_datetime}, {printable_last_datetime}")

    return first_day_datetime, last_day_datetime
