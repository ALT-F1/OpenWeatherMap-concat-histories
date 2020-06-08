# Changelog

All notable changes to this project will be documented in this file. See [standard-version](https://github.com/conventional-changelog/standard-version) for commit guidelines.

## [2.0.0](https://github.com/ALT-F1/OpenWeatherMap/compare/v1.1.0...v2.0.0) (2020-06-08)


### Features

* build dataframes grouping the weather data by province, date and including the quartiles ([b16deac](https://github.com/ALT-F1/OpenWeatherMap/commit/b16deac5c241d8f1f37e50c1978152fb3d13d574))

## 1.1.0 (2020-06-08)


### Features

* add alt-be.helper to check if Kaggle is running or not ([6905478](https://github.com/ALT-F1/OpenWeatherMap/commit/690547878b67877c8cf0dade202bc8b3583e8418))
* add OpenWeatherMap.org data in CSV format ([1b7b140](https://github.com/ALT-F1/OpenWeatherMap/commit/1b7b140ea242f77668fa879a9bdc6c99cbbaadc1))
* add zipcodes from Belgium in FR and NL to find the Provinces related to Postal Codes ([302427c](https://github.com/ALT-F1/OpenWeatherMap/commit/302427c4961702153c968157fd4e599834d13198))
* aggregate CSV files containing Weather data per day into a CSV and Pickle file ([89cc85f](https://github.com/ALT-F1/OpenWeatherMap/commit/89cc85fb3ad8be1dae81416d49e5699ef83f5f74))
* prepare the Belgian postal codes database from BPost before ETL ([d0f61c1](https://github.com/ALT-F1/OpenWeatherMap/commit/d0f61c1629f5a9f2679ffcfcd28cf0de1e4dbbea))


### Documentations

* add a closed LICENSE ([50c4c64](https://github.com/ALT-F1/OpenWeatherMap/commit/50c4c64367fb07d172e845ff2405cc929bcd4893))
* add README ([3dc5b3b](https://github.com/ALT-F1/OpenWeatherMap/commit/3dc5b3b4ba48f0b2000144789fabc190859708f2))
* remove some text ([632b916](https://github.com/ALT-F1/OpenWeatherMap/commit/632b916872ece536eb636c5e8115a04379641931))


### Chores

* add .gitattributes including csv files ([61e9d73](https://github.com/ALT-F1/OpenWeatherMap/commit/61e9d73a7e11f955e0d19cca6c6492433dc7bf4d))
* add .gitignore for node, python, jupyter notebooks, visual studio code ([d203d3d](https://github.com/ALT-F1/OpenWeatherMap/commit/d203d3d8a6a9f8a522c346a0f3328b9528a521b2))
* add vscode configurations ([e1443ce](https://github.com/ALT-F1/OpenWeatherMap/commit/e1443ce5d6383de7ccd692a685aa0a76296d122e))
* **release:** 1.0.0 ([dcb85e1](https://github.com/ALT-F1/OpenWeatherMap/commit/dcb85e14da219a26ea3174fccc97a685be3e2fe2))
* ignore files greater than 100 MB due to gihutb constraint : remove df_provinces_collection.pkl and df_provinces_collection.csv ([87f27d9](https://github.com/ALT-F1/OpenWeatherMap/commit/87f27d93063a4e0190ed2c9a738eb7520809ae5e))
* set the types recognized during the generation of the CHANGELOG ([39f01a9](https://github.com/ALT-F1/OpenWeatherMap/commit/39f01a90543c1a49fa0dd9f13e92b8c6b86284aa))
* **release:** 1.0.1 ([c081503](https://github.com/ALT-F1/OpenWeatherMap/commit/c081503754a60a24a9f8cf8d48eb398fc712623c))


### Tests

* add concatenated CSV and Pickle files containing all Weather data from Belgian cities ([735ee0e](https://github.com/ALT-F1/OpenWeatherMap/commit/735ee0ea968b9035680fb779e5bd569b99bcec78))
* add zipped version of df_provinces_collection.pkl and df_provinces_collection.csv ([b6c97ac](https://github.com/ALT-F1/OpenWeatherMap/commit/b6c97ac26b25441a9994d64f048299b8884f852f))


### Builds

* add package.json ([a3c5eeb](https://github.com/ALT-F1/OpenWeatherMap/commit/a3c5eeb64c17b8b44b4ff95d3d3e71f85ba9e673))
* add requirements.txt ([f5cfdaa](https://github.com/ALT-F1/OpenWeatherMap/commit/f5cfdaafe72c81142c6548b3ca0a50c40e733ac7))


### Styles

* add the github social preview ([5d23a71](https://github.com/ALT-F1/OpenWeatherMap/commit/5d23a717803d95f2e4d172b5de7ee4e87ecf9061))
* add the github social preview ([d516523](https://github.com/ALT-F1/OpenWeatherMap/commit/d516523843154e845cd16190d30690ffff3847fd))

### [1.0.1](https://github.com/ALT-F1/OpenWeatherMap/compare/v1.0.0...v1.0.1) (2020-06-05)


### Tests

* add zipped version of df_provinces_collection.pkl and df_provinces_collection.csv ([13ed0cb](https://github.com/ALT-F1/OpenWeatherMap/commit/13ed0cb44aec8b4c81a04bafedebaa2c6d9c05d8))


### Chores

* ignore files greater than 100 MB due to gihutb constraint : remove df_provinces_collection.pkl and df_provinces_collection.csv ([67aef5b](https://github.com/ALT-F1/OpenWeatherMap/commit/67aef5ba1e0ded5e52acc644d86c70cda652ad18))

## 1.0.0 (2020-06-05)


### Features

* add alt-be.helper to check if Kaggle is running or not ([6905478](https://github.com/ALT-F1/OpenWeatherMap/commit/690547878b67877c8cf0dade202bc8b3583e8418))
* add OpenWeatherMap.org data in CSV format ([1b7b140](https://github.com/ALT-F1/OpenWeatherMap/commit/1b7b140ea242f77668fa879a9bdc6c99cbbaadc1))
* add zipcodes from Belgium in FR and NL to find the Provinces related to Postal Codes ([302427c](https://github.com/ALT-F1/OpenWeatherMap/commit/302427c4961702153c968157fd4e599834d13198))
* aggregate CSV files containing Weather data per day into a CSV and Pickle file ([89cc85f](https://github.com/ALT-F1/OpenWeatherMap/commit/89cc85fb3ad8be1dae81416d49e5699ef83f5f74))
* prepare the Belgian postal codes database from BPost before ETL ([d0f61c1](https://github.com/ALT-F1/OpenWeatherMap/commit/d0f61c1629f5a9f2679ffcfcd28cf0de1e4dbbea))


### Tests

* add concatenated CSV and Pickle files containing all Weather data from Belgian cities ([456f6c1](https://github.com/ALT-F1/OpenWeatherMap/commit/456f6c1dcbc2360582360e11777f83149e41400f))


### Documentations

* add a closed LICENSE ([50c4c64](https://github.com/ALT-F1/OpenWeatherMap/commit/50c4c64367fb07d172e845ff2405cc929bcd4893))
* add README ([3dc5b3b](https://github.com/ALT-F1/OpenWeatherMap/commit/3dc5b3b4ba48f0b2000144789fabc190859708f2))


### Chores

* add .gitattributes including csv files ([61e9d73](https://github.com/ALT-F1/OpenWeatherMap/commit/61e9d73a7e11f955e0d19cca6c6492433dc7bf4d))
* add .gitignore for node, python, jupyter notebooks, visual studio code ([d203d3d](https://github.com/ALT-F1/OpenWeatherMap/commit/d203d3d8a6a9f8a522c346a0f3328b9528a521b2))
* add vscode configurations ([e1443ce](https://github.com/ALT-F1/OpenWeatherMap/commit/e1443ce5d6383de7ccd692a685aa0a76296d122e))
* set the types recognized during the generation of the CHANGELOG ([39f01a9](https://github.com/ALT-F1/OpenWeatherMap/commit/39f01a90543c1a49fa0dd9f13e92b8c6b86284aa))


### Builds

* add package.json ([a3c5eeb](https://github.com/ALT-F1/OpenWeatherMap/commit/a3c5eeb64c17b8b44b4ff95d3d3e71f85ba9e673))
* add requirements.txt ([f5cfdaa](https://github.com/ALT-F1/OpenWeatherMap/commit/f5cfdaafe72c81142c6548b3ca0a50c40e733ac7))


### Styles

* add the github social preview ([5d23a71](https://github.com/ALT-F1/OpenWeatherMap/commit/5d23a717803d95f2e4d172b5de7ee4e87ecf9061))
* add the github social preview ([d516523](https://github.com/ALT-F1/OpenWeatherMap/commit/d516523843154e845cd16190d30690ffff3847fd))
