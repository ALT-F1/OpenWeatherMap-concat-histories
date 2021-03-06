# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

from datetime import timedelta, datetime
from pathlib import Path
from os import path
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

# constants
MISSING_LIBRARY = -1

# import libraries

class AltF1BeHelpers:
    def is_interactive(self):
        # return True if running on Kaggle
        try:
            return 'runtime' in get_ipython().config.IPKernelApp.connection_file
        except NameError:
            if (path.exists('/kaggle/working')):
                return True
            else:
                return False


    def unicode_to_ascii(self, a):
        """
        remove accents and apostrophes
        """
        try:
            import unidecode
        except ModuleNotFoundError:
            print(f"unidecode library is missing in you environment. Install unidecode or use conda or venv to set the right environment")
            exit(MISSING_LIBRARY)
        # def remove_accents_apostrophe(a):
        a = unidecode.unidecode(a)  # remove accent
        a = a.replace("'", '')  # remove apostrophe
        return a


    def output_directory(self, directories=[]) -> str:
        output_directory = '/kaggle/working'
        if self.is_interactive():
            output_directory = os.path.join(
                output_directory, os.path.sep.join(directories))
        else:
            output_directory = os.path.join(os.path.abspath(
                os.getcwd()), "output_directory", "data", os.path.sep.join(directories))

        Path(output_directory).mkdir(parents=True, exist_ok=True)
        return output_directory

    def daterange(self, start_date, end_date):
        for n in range(int((end_date - start_date).days)):
            yield start_date + timedelta(n)

    def get_first_and_last_day_of_the_month(year, month):
    
        first_day_datetime = datetime.datetime(year=year, month=month, day=1, hour=0, minute=0)
        printable_start_datetime = first_day_datetime.strftime("%Y-%m-%d_%Hh%M")
        
        last_day_datetime = datetime.datetime(year=year, month=month, day=calendar.monthrange(year,month)[1], hour=23, minute=0)
        printable_last_datetime = last_day_datetime.strftime("%Y-%m-%d_%Hh%M")
        
        print(f"{printable_start_datetime}, {printable_last_datetime}")

        return first_day_datetime, last_day_datetime

if __name__ == "__main__":

    altF1BeHelpers = AltF1BeHelpers()
    text = "éè à iïî où &é'(§è!çàaQwxs $ µ `"
    print(
        f"unicode_to_ascii(text): '{text}' becomes '{altF1BeHelpers.unicode_to_ascii(text)}'")
    print(f"is_interactive(): {altF1BeHelpers.is_interactive()}")
    print(f"output_directory(): {altF1BeHelpers.output_directory(['new_directory'])}")

    for single_date in altF1BeHelpers.daterange(datetime.now() - timedelta(5), datetime.now() - timedelta(1)):
            #print(single_date.strftime("%Y-%m-%d"))
            print(f'daterange(): {single_date.strftime("%Y-%m-%d")}')

