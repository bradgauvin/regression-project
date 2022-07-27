# Regression-project

![zillow-com-logo](https://user-images.githubusercontent.com/103786599/180569261-3dfdd644-5ab2-4d38-9eee-6e443c6d3023.png)

This repository contains the code for the Regression project completed as part of the Codeup Data Science curriculum.

## Repo contents:

### <summary>1. Readme File</summary>
<details>

```- project description with goals
- initial hypotheses and/or questions you have of the data, ideas
- data dictionary
- project planning (lay out your process through the data science pipeline)
- instructions or an explanation of how someone else can reproduce your project and findings (What would someone need to be able to recreate your project on their own?)
- key findings, recommendations, and takeaways from your project,
```
</details>

### 2. Final report (zillow_report.ipynb)
### 3. Acquire module (acquire.py)
### 4. Prepare module (prepare.py)
### 5. Modeling module (model.py)
### 5. Predictions.csv
### 6. Exploration & modeling notebooks (zillow-eda-modeling.ipynb)
### 7. Functions to support modeling work ()
### 8. Final Report

## Purpose
The purpose of this notebook is to explore the data to identify which variables are primarily responsible for the changes in home prices from the data set.

### Goal/Aim
 - Your goal is to predict the values of single unit properties using the observations from 2017.
 - Find which features variable pairs impact values
 - Find which categorical and continuous variables impact value
 - Build regression models to meet stakeholder questions
 - Compare models and select best performing model

## Initial Questions and Hypotheses
1. Find which features variable pairs impact values?
     - What's the role of location (counties) in value?
     - How does space affect value?
     - What's the relationship between age, square_feet, age, and value (Continuous variables)



## Data Dictionary
<details>
|Feature Name|	Description|	Data Type| Updated to|
|:---|:---|---:|:----|
|parcel| Lot number |Key - unique identifier| |
|bedrooms| number of bedrooms| categorical| deleted|
|bathrooms| number of bathrooms| categorical| deleted|
|square_feet| size of home| continuous| deleted|
|garage| number of garages on lot| categorical| deleted|
|pool| number of pools on lot| categorical| deleted|
|lot_size| area of lot in square feet| continuous| deleted|
|year_built| year home was built| continuous| deleted|
|tax_value| value of property| target variable| deleted|
|quality| Overall assessment of condition of building from best (lowest number) to worst (highest)| categorical| deleted|
|fed_code| federal code relating to county| categorical| deleted|
|age| age of home in 2017| categorical| deleted|
|living_space| square foot of house minus avg. size of bedroom and bathrooms| continuous deleted|
|county| categorical county 0 =LA, 1 = Orange, 2 = Ventura| categorical| deleted|

</details>

## Project Plan

- Planning:
    - [x] Review project expectations from Codeup & Rubric
    - [x] Draft project goal to include measures of success
    - [x] Create questions related to the project
    - [x] Create questions related to the data
    - [x] Create a plan for completing the project using the data science pipeline
    - [x] Create a data dictionary to define variables and data context
    - [x] Draft starting hypothesis in EDA

- Acquire:
   - [x] Create .gitignore
   - [x] Create env file with log-in credentials
   - [x] Store env file in .gitignore to ensure security of sensitive data
   - [x] Create acquire.py module
   - [x] Store functions needed to acquire the Telco dataset from mySQL
   - [x] Ensure all imports needed to run the functions are inside the acquire.py document
   - [x] Using Jupyter Notebook
   - [x] Run all required imports
   - [x] Import functions from aquire.py module
   - [x] Summarize dataset using methods and document observations

- Prepare:
   - [x] Create prepare.py module
   - [x] Store functions needed to prepare the Telco data such as:
          - [x] Split Function: to split data into train, validate, and test
          - [x] Cleaning Function: to clean data for exploration
          - [x] Encoding Function: to create numeric columns for object column
          - [x] Feature Engineering Function: to create new features
   - [x] Ensure all imports needed to run the functions are inside the prepare.py document Using Jupyter Notebook
   - [x] Import functions from prepare.py module
   - [x] Summarize dataset using methods and document observations
   - [x] Clean data
   - [x] Features need to be turned into numbers
   - [x] Categorical features or discrete features need to be numbers that represent those categories
   - [x] Continuous features may need to be standardized to compare like datatypes
   - [x] Address missing values, data errors, unnecessary data, renaming
   - [x] Split data into train, validate, and test samples
   
- Explore:
  - [x] Answer key questions about hypotheses and find drivers of churn
      - Run at least two statistical tests
      - Document findings
  - [x] Create visualizations with intent to discover variable relationships
      - Identify variables related to churn
      - Identify any business features related to churn
  - [x] Summarize conclusions, provide clear answers, and summarize takeaways
  - [x] Explain plan of action as deduced from work to this point

- Model:
** Using Jupter Notebook:
  - [x] Establish Baseline Accuracy
  - [x] Train and fit 3 Models 
  - [x] Remove unnecessary features
  - [x] Evaluate Best Performing Models
  - [x] Choose Best performing model for test
  - [x] Test Final Model on out-of-sample dataset
  - [x] Summarize Performance
  - [x] Interpret and document findings

- Delivery:
  - [ ] 5 min presentation in jupyter notebook
      - Introduction and Proj. Goals
      - Executive summary of findings, takeaways, and recommendations
      - Analysis Walkthrough
          -  Visualize relationships
          -  Document Takeaways
          -  Highlight where Project questions are answered
      -  Final takeaway and COAs 
  - [ ] Ready for questions 

## Steps to Reproduce

 - [x] You need an env.py file with hostname, username, and password for mySQL database that contains the telco_churn database
 - [x] Store env file in local repository
 - [x] Make .gitignore and validate env.py file is part of .gitignore
 - [x] Clone my repo
 - [x] Import python libraries: pandas, matplotlib, seaborn, numpy, scipy, eli5 and sklearn
 - [x] modeling.py is available for reference - codes had to be adjusted for telco data set, but used as a reference point
 - [x] follow steps outlined in README.md and churn_report.ipynb
 

## Key Findings and Recommendations
 - [x] Features: 
 - [x] Polynomial regression had highest R2 and lowest RMSE scores
 - [x] Recommend additional exploritory analysis for different features
   - May want to look at separating by county
   - May want to look at binning continuous variables

 
## Errors and Limitations
 - Started analysis by county, but didn't get to getting a good product available
 - Tried to get a final visualization to show comparison between baseline, train, validate, and test sets but did not accomplish
 
 - Created a loop error in my .py files.  model and explore file reference each other.  Had to bring in functions to this notebook to get it all to run correctly.
    - would recommend breaking functions up to more manageable sections
    - Would recommend having one file of functions rather than multiple to bring in
  

## Future Work 
 - Recommend combing modleing results into dataframe and allowing the notebook to choose the highest accurcay/recall values
 - Try to write and test code out of your notebook and put final results in the notebook you're using.

