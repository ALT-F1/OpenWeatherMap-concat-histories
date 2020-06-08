# Concatenate weather data histories in CSV format collected from OpenWeatherMap for the Belgian communes

The software concatenates the histories Weather data of the Belgian communes collected by using this repository [https://github.com/ALT-F1/OpenWeatherMap](https://github.com/ALT-F1/OpenWeatherMap)

The histories are extracted from the OpenWeatherMap database. See [https://www.openweathermap.org](https://www.openweathermap.org)

The weather data will be linked to other data to answer one question: "Does the usage of the Weather data influence (or not) the model forecasting the spread of the COVID-19?"

It takes 250 seconds to concatenate 742 files in a OpenWeatherMap CSV files on a Intel(R) Core(TM) i7-2640M CPU @ 2.80GHz.

# The context

Given the consequences of the COVID-19 pandemic for public health, many stakeholders in public and private sectors engage in global efforts to treat and understand those exposed to the virus and to contain the outbreak.

Universities and private companies contribute to the analysis of data useful to forecast the spread of the "Severe Acute Respiratory Syndrome CoronaVirus 2" (SARS-CoV-2).

Those persons include researchers and consultants who share their analysis to the public administration and members of governments who will shape the rules and regulations describing how the citizens should behave during the pandemic.

# Why collecting the weather data?

In Belgium, the  Group of Experts for an Exit Strategy (GEES) drafts proposals to envisage a gradual deconfinement. The GEES supports the [Belgian Federal Government](https://www.belgium.be/en/about_belgium/government/federal_authorities/federal_government).

See also [https://www.info-coronavirus.be/en](https://www.info-coronavirus.be/en)

The GEES uses data from researchers, amongst others. Those researchers build models of the spread of the virus by using diverse data: mobility, health, beds in hospitals, fatalities, current regulation ...

One question remains: **does the usage of the Weather data influence (or not) the spread of the virus?**

One of those groups of researchers includes the [Machine Learning Group](https://mlg.ulb.ac.be) (MLG) from the [Université Libre de Bruxelles](https://www.ulb.be). The MLG supports the initiative by providing models made of Artificial Intelligence/Machine Learning algorithms. The models built by the MLG influence the Exit Strategy.

# The tools used to build the software

* Pandas https://pandas.pydata.org
* Python https://www.python.org 
* Numpy https://numpy.org
* Kaggle https://www.kaggle.com
* Visual Studio Code https://code.visualstudio.com

# The sponsors of the project

The **EOSC Secretariat** supports the governance of the **E**uropean **O**pen **S**cience **C**loud (EOSC). See [https://www.eoscsecretariat.eu/](https://www.eoscsecretariat.eu)

The EOSC supports projects aiming to make data **F**indable, **A**ccessible, **I**nteroperable, and **R**eproducible (FAIR) for scientists; these combinations would lead to (unforeseen) reuse and faster development of science. 

EOSC Secretariat granted funds to [http://www.alt-f1.be](http://www.alt-f1.be) to create a "Crossroads Data Bank for COVID-19".

Latest news from the European Commission: [https://ec.europa.eu/research/openscience/index.cfm?pg=open-science-cloud](https://ec.europa.eu/research/openscience/index.cfm?pg=open-science-cloud) 

**OpenWeatherMap** provides, free-of-charge, access to weather data to its historical weather data [https://openweathermap.org/api](https://openweathermap.org/api)

OpenWeather Ltd is a British-based tech company that provides weather and satellite data worldwide. OpenWeather collects and processes raw data from a variety of sources, and gives its customers access to the archive. See [https://openweathermap.org/](https://openweathermap.org/)

See [Openweather LTD Helps The Fight To Overcome COVID-19](https://bit.ly/2ZohgFF)

# The supporters of the project

**The Machine Learning Group**, founded in 2004 by [Gianluca Bontempi](https://mlg.ulb.ac.be/wordpress/members-2/gianluca-bontempi),  is a research unit of the Computer Science Department of the ULB (Université Libre de Bruxelles, Brussels, Belgium), Faculty of Sciences, currently co-headed by Prof. Gianluca Bontempi and Prof. [Tom Lenaerts](https://mlg.ulb.ac.be/wordpress/members-2/tom-lenaerts).

MLG targets machine learning and behavioral intelligence research focusing on time series analysis, big data mining, causal inference, network inference, decision-making models, and behavioral analysis with applications in data science, medicine, molecular biology, cybersecurity and social dynamics related to cooperation, emotions, and others.

See [https://mlg.ulb.ac.be/](https://mlg.ulb.ac.be/)

# Legal matters

The current software digests data that do not contain personal data.

The output of this project is linked to data that do not contain Personally Identifiable Information (PII). See [https://en.wikipedia.org/wiki/Personal_data](https://en.wikipedia.org/wiki/Personal_data)

# the data models

## OpenWeatherMap Historical data

OpenWeatherMap provides an API returning the hourly Weather. A call to the API returns a maximum of 7 consecutive days of data.
[https://openweathermap.org/history](https://openweathermap.org/history) 

Here is an example of a call: `http://history.openweathermap.org/data/2.5/history/city?id={id}&type=hour&start={start}&end={end}&appid={YOUR_API_KEY}`

### the response from the history of OpenWeatherMap

The documentation of the **response from the history** of OpenWeatherMap is here: [https://openweathermap.org/weather-data](https://openweathermap.org/weather-data)

``` json
{
    "dt": 1587312000,
    "main": {
        "temp": 287.44,
        "feels_like": 284.3,
        "pressure": 1015,
        "humidity": 76,
        "temp_min": 287.04,
        "temp_max": 288.15
    },
    "wind": {
        "speed": 4.6,
        "deg": 40
    },
    "clouds": {
        "all": 77
    },
    "weather": [
        {
            "id": 500,
            "main": "Rain",
            "description": "light rain",
            "icon": "10d"
        }
    ],
    "rain": {
        "1h": 0.3
    }
},
```
## OpenWeatherMap historical data in CSV format

The project [https://github.com/ALT-F1/OpenWeatherMap](https://github.com/ALT-F1/OpenWeatherMap) generates either CSV or JSON files containing the Weather of one Belgian city per day hour by hour.

The current project concatenates the historical data into one single file.

Historical data collected from March 01, 2020, to May 22, 2020, weights 231,9 MB in a CSV format and 251,9 MB in a pickle format.

CSV and Pickle files are available in `src/kaggle/output/kaggle/working`.

Here is an extract of the CSV format:

``` csv
message,cod,city_id,calctime,cnt,dt,main.temp,main.feels_like,main.pressure,main.humidity,main.temp_min,main.temp_max,wind.speed,wind.deg,clouds.all,weather.id,weather.main,weather.description,weather.icon

Count: 168,200,2787356,0.005035309,168,1583017200,278.11,271.54,995,86,277.04,279.15,7.2,210,40,802,Clouds,scattered clouds,03n

Count: 168,200,2787356,0.005035309,168,1583020800,278.31,270.13,995,80,277.04,279.82,9.3,210,20,801,Clouds,few clouds,02n

Count: 168,200,2787356,0.005035309,168,1583024400,278.31,270.4,995,75,277.04,279.82,8.7,210,20,801,Clouds,few clouds,02n
```

The concatenation of the historical data augmented by some transformations generate this format:

``` csv
,message,cod,city_id,calctime,cnt,dt,main.temp,main.feels_like,main.pressure,main.humidity,main.temp_min,main.temp_max,wind.speed,wind.deg,clouds.all,weather.id,weather.main,weather.description,weather.icon,Province,Postal code,date

0,Count: 168,200,2795949,0.037120004,168,1583017200,278.15,271.58,995,86,277.04,279.26,7.2,210,40,802,Clouds,scattered clouds,03n,LIEGE,4217,2020-02-29

1,Count: 168,200,2795949,0.037120004,168,1583020800,278.22,270.02,995,80,277.04,279.26,9.3,210,87,500,Rain,light rain,10n,LIEGE,4217,2020-03-01

2,Count: 168,200,2795949,0.037120004,168,1583024400,278.25,270.33,995,75,277.04,279.26,8.7,210,66,500,Rain,light rain,10n,LIEGE,4217,2020-03-01

```


# How to contribute to software development

* run `npm install` to install the standard-conventions package. A utility for versioning using semver [https://semver.org/](https://semver.org/) and CHANGELOG generation powered by Conventional Commits [https://conventionalcommits.org](https://conventionalcommits.org).

* commit your changes by using the scripts. read the specifications [https://www.conventionalcommits.org/en/v1.0.0/#specification](https://www.conventionalcommits.org/en/v1.0.0/#specification)
    * run `git commit -m "{build}{chore}{ci}{docs}{feat}{fix}{perf}{refactor}{revert}{style}{test}: xxx"`

* set the version of the code and amend the CHANGELOG with
    * `npm run patch` (from 0.0.0 to 0.0.1)
    * `npm run minor` (from 0.0.0 to 0.1.0)
    * `npm run major` (from 0.0.0 to 1.0.0)

* push the code including the tags
    * `npm run push`


# Acronyms

* ETL: Extract-Transform-Load https://en.wikipedia.org/wiki/Extract,_transform,_load