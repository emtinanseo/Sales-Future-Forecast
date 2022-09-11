# Sales-Future-Forecast

## Introduction
The goal of this challenge is to use Machine Learning to forecast sales of Rossmann Pharmaceuticals’ stores six weeks ahead of time.

### Business Need & Benefits
Sales forecast is needed for planning (inventory, promotions, .. etc ) across storess. Correct planning ahead of time could reduce losses or capture oppotunities of increasing profits. The current system at Rossmann Pharmaceutical relies on the experience and intiuition of managers. Machine learning has the capability to provide much more accurate and comprehensive forecasts. This is what we aim to do though this challenge.

### Data
Data is taken from https://www.kaggle.com/competitions/rossmann-store-sales/data

Data used for analysis is historical sales data for 1,115 Rossmann stores, across several cities. Data includes information on promotions, competition, school and state holidays, seasonality, and locality; factors identified as necessary for sales prediction. 

Data is devided in four files:
* train.csv - historical data including Sales
* test.csv - historical data excluding Sales
* sample_submission.csv - a sample submission file in the correct format
* store.csv - supplemental information about the stores





## Repo Structure
### Folders
#### Notebooks
* EDA is done in notebook [eda_indepth.ipynb](https://github.com/emtinanseo/Sales-Future-Forecast/blob/main/notebooks/eda_indepth.ipynb)
* Data preprocessing is done in notebook [data_preprocess.ipynb](https://github.com/emtinanseo/Sales-Future-Forecast/blob/main/notebooks/data_preprocess.ipynb)


## Installation Guide
'''
git clone https://github.com/emtinanseo/Sales-Future-Forecast.git

cd Sales-Future-Forecast

pip install -r requirements.txt
'''