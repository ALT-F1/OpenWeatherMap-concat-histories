# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

from pathlib import PurePath

from altf1be_helpers import unicode_to_ascii
    
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
# for dirname, _, filenames in os.walk('/kaggle/input'):
#    for filename in filenames:
#        print(os.path.join(dirname, filename))

# You can write up to 5GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All"
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

def is_interactive():
    return False

class BPost_postal_codes():
    """ 
        The class provides a read-to-use dataframe to manipulate the postal codes 
        made available by the Belgian postal office
    """

    # source https://www.bpost.be/site/fr/envoyer/adressage/rechercher-un-code-postal
    postal_codes_in_be_from_bpost_be_in_fr_path = "kaggle/input/bpost-postal-codes/zipcodes_alpha_fr_new.csv"

    # source https://www.bpost.be/site/nl/verzenden/adressering/zoek-een-postcode
    postal_codes_in_be_from_bpost_be_in_nl_path = "kaggle/input/bpost-postal-codes/zipcodes_alpha_nl_new.csv"

    if (is_interactive()):
        postal_codes_in_be_from_bpost_be_in_fr_path = f"/{postal_codes_in_be_from_bpost_be_in_fr_path}"
        postal_codes_in_be_from_bpost_be_in_nl_path = f"/{postal_codes_in_be_from_bpost_be_in_nl_path}"
    else:
        # source https://www.bpost.be/site/fr/envoyer/adressage/rechercher-un-code-postal
        postal_codes_in_be_from_bpost_be_in_fr_path = os.path.join(
            os.path.abspath(os.getcwd()),
            "src",
            postal_codes_in_be_from_bpost_be_in_fr_path
        )

        # source https://www.bpost.be/site/nl/verzenden/adressering/zoek-een-postcode
        postal_codes_in_be_from_bpost_be_in_nl_path = os.path.join(
            os.path.abspath(os.getcwd()),
            "src",
            postal_codes_in_be_from_bpost_be_in_nl_path
        )
    
    print(f"postal_codes_in_be_from_bpost_be_in_fr_path: {postal_codes_in_be_from_bpost_be_in_fr_path}")
    print(f"postal_codes_in_be_from_bpost_be_in_nl_path: {postal_codes_in_be_from_bpost_be_in_nl_path}")
    
    missing_english_cities = pd.DataFrame(
        {"Code postal": [1000, 1342],
            "Localité": ["Brussels", "Ottignies"],
            "Commune principale": ["Brussels", "Ottignies"],
            "Province": ["BRUXELLES", "BRABANT WALLON"]
         }
    )

    def extract_postal_codes(self):
        """
            Extract the Belgian postal codes from the BPOST.BE database
        """
        # source https://www.bpost.be/site/fr/envoyer/adressage/rechercher-un-code-postal
        columns = {
            'Postcode': 'Code postal',
            'Plaatsnaam':  'Localité',
            'Deelgemeente': 'Sous-commune',
            'Hoofdgemeente': 'Commune principale',
            'Provincie': 'Province'
        }
        self.postal_codes_in_be_from_bpost_be_in_fr = pd.read_csv(
            self.postal_codes_in_be_from_bpost_be_in_fr_path,
            sep=',',
            header=0
        )
        self.postal_codes_in_be_from_bpost_be_in_nl = pd.read_csv(
            self.postal_codes_in_be_from_bpost_be_in_nl_path,
            sep=',',
            header=0
        )

        # rename the columns in NL to facilitate the concatenation
        self.postal_codes_in_be_from_bpost_be_in_nl = self.postal_codes_in_be_from_bpost_be_in_nl.rename(
            columns=columns,
            errors='raise'
        )

        self.df_postal_codes_in_be = pd.concat([
            self.postal_codes_in_be_from_bpost_be_in_nl,
            self.postal_codes_in_be_from_bpost_be_in_fr
        ])

    def keep_certain_columns_in_df(self):
        """
        Reduce the amount of columns in final self.df_postal_codes_in_be
        """

        # keep fewer columns
        self.df_postal_codes_in_be = self.df_postal_codes_in_be[
            ['Code postal', 'Commune principale', 'Localité', 'Province']
        ]

    def add_missing_names_in_en(self):
        """
        Transform: Add missing names in English in BPOST database
        """

        # add missing cities
        self.df_postal_codes_in_be = self.df_postal_codes_in_be.append(
            self.missing_english_cities
        )
        # self.df_postal_codes_in_be.shape

    def columns_in_lowercase(self):
        """        
        Transform: change columns in lower case
        """
        # change column to lowercase
        self.df_postal_codes_in_be['Localité'] = self.df_postal_codes_in_be['Localité'].str.lower(
        )
        self.df_postal_codes_in_be['Commune principale'] = self.df_postal_codes_in_be['Commune principale'].str.lower(
        )

    def remove_non_ascii_characters(self):
        """
        Transform: remove accents and apostophes and use 'normalized' columns
        """
        self.df_postal_codes_in_be['Commune principale normalized'] = self.df_postal_codes_in_be['Commune principale'].apply(
            unicode_to_ascii
        )

        self.df_postal_codes_in_be['Localité normalized'] = self.df_postal_codes_in_be['Localité'].apply(
            unicode_to_ascii
        )

    def drop_duplicates(self):
        """
        Transform: drop all duplicates from self.df_postal_codes_in_be
        """

        # drop duplicates and keep the first one
        self.df_postal_codes_in_be = self.df_postal_codes_in_be.drop_duplicates(
            keep='first')

    def __init__(self):
        self.extract_postal_codes()
        self.keep_certain_columns_in_df()
        self.add_missing_names_in_en()
        self.columns_in_lowercase()
        self.remove_non_ascii_characters()
        self.drop_duplicates()


if __name__ == "__main__":
    print(f"is_interactive() : {is_interactive()}")
    bpost_postal_codes = BPost_postal_codes()
    # print(bpost_postal_codes.df_postal_codes_in_be)
