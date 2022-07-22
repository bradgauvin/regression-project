# Regression-project

https://github.com/bradgauvin/regression-project/blob/main/zillow-com-logo.png?raw=true

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
### 6. Exploration & modeling notebooks (eda.ipynb)
### 7. Functions to support modeling work ()

## Project Goals


## Initial Questions and Hypotheses




## Data Dictionary
<details>


</details>

## Project Plan

- Planning:
    - [x] Review project expectations from Codeup & Rubric
    - [x] Draft project goal to include measures of success
    - [x] Create questions related to the project
    - [x] Create questions related to the data
    - [x] Create a plan for completing the project using the data science pipeline
    - [x] Create a data dictionary to define variables and data context
    - [x] Draft starting hypothesis

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
 - [x] Autopay, Paperless billing, Fiber internet, and Electronic Check payments effct churn
 - [x] KNN model showed a 3% increase in predicting churn
 - [x] Recommend additional exploritory analysis for different features

 
## Errors and Limitations
 - Didn't split dataset before explortation.  Data set was rerun splitting into train, validate, and test with train being renamed to df2.  This was to ensure that all df2 codes didn't have to be updated. 
     - Recommend splitting data before exploration
     - Find additional ways to highlight features.  I used eli5, but may need to explore dtale, featurewix, or feature_selection from sklearn.
 
 - Adjusted features multiple times.  This caused some errors while writing the codes.  If you see features re-defined in the code, this is where I had trouble due to adjusting features.
   - Recommend future features are identified and not changed until modeling is completed

- Copying code from Modeling stage to final notebook caused errors.
   - Recommend restarting and rerunning kernel before coping code from one notebook to another.
   - Recommend validating variables are the same or in the same format before copy and pasting.  

## Future Work 
 - Recommend combing modleing results into dataframe and allowing the notebook to choose the highest accurcay/recall values
 - Try to write and test code out of your notebook and put final results in the notebook you're using.
 - Focus on key questions.  New insight will come when doing EDA, but keeping the project questions in mind will keep you focused.  
      - Keep customer's focus
      - SHow where you answer the questions
