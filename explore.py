#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_histograms(df, columns):
    """ Plots multiple histograms of specified columns argument using data from input df """
    # List of columns
    cols = columns
    plt.figure(figsize=(25, 10))
    for i, col in enumerate(cols):

        # i starts at 0, but plot nos should start at 1
        plot_number = i + 1 

        # Create subplot.
        plt.subplot(1, len(cols), plot_number)

        # Title with column name.
        plt.title(col)

        # Display boxplot for column.
        sns.histplot(data=df[col], bins=10)

        # Hide gridlines.
        plt.grid(False)

    plt.show()

def plot_boxplots(df, columns):
    """ Plots multiple boxplots of specified columns argument using data from input df """
    # List of columns
    cols = columns
    plt.figure(figsize=(16, 6))
    for i, col in enumerate(cols):

        # i starts at 0, but plot nos should start at 1
        plot_number = i + 1 

        # Create subplot.
        plt.subplot(1, len(cols), plot_number)

        # Title with column name.
        plt.title(col)

        # Display boxplot for column.
        sns.boxplot(data=df[col])

        # Hide gridlines.
        plt.grid(False)

    plt.show()

def plot_variable_pairs(df, numerics, categoricals, targets, sample_amt):
    """ Plots pairwise relationships between numeric variables in df along with regression line for each pair. Uses categoricals for hue."""
    # Sampling allows for faster plotting with large datasets at the expense of not seeing all datapoints
    # Checks if a sample amount was inputted
    if sample_amt:
        df = df.sample(sample_amt)
    # Checks if any categorical variables were given to determine how to set the lmplot regression line parameters
    if len(categoricals)==0:
        categoricals = [None]
        # Setting to red makes it easier to see against the default color
        line_kws = {'lw':4, 'color':'red'}
    else:
        line_kws = {'lw':4}
    for cat in categoricals:    
        for col in numerics:
            for y in targets:
                if y == col:
                    continue
                sns.lmplot(data = df, 
                           x=col, 
                           y=y, 
                           hue=cat, 
                           palette='Set1',
                           scatter_kws={"alpha":0.2, 's':10}, 
                           line_kws=line_kws,
                           ci = None)
            

def plot_categorical_and_continuous_vars(df, categorical, continuous, sample_amt):
    """ Accepts dataframe and lists of categorical and continuous variables and outputs plots to visualize the variables"""
    sns.set(font_scale=1.2)
    # Sampling allows for faster plotting with large datasets at the expense of not seeing all datapoints
    if sample_amt:
        df = df.sample(sample_amt)
    # Outputs 3 plots showing high level summary of the inputted data
    for num in continuous:
        for cat in categorical:
            _, ax = plt.subplots(1,3,figsize=(20,8))
            print(f'Generating plots {num} by {cat}')
            # Strip plot
            p = sns.barplot(data = df, x=cat, y=num, ax=ax[0])
            # Mean line
            p.axhline(df[num].mean())
            # Boxplot
            p = sns.boxplot(data = df, x=cat, y = num, ax=ax[1])
            # mean line
            p.axhline(df[num].mean())
            # Violine plot
            p = sns.violinplot(data = df, x=cat, y=num, hue = cat, ax=ax[2])
            #mean line
            p.axhline(df[num].mean())
            plt.suptitle(f'{num} by {cat}', fontsize = 18)
            plt.show()

def plot_pairplot_pairs(df):
    return sns.pairplot(df, corner = True, kind='reg', plot_kws={'line_kws':{'color':'red'}, 'scatter_kws':{'s': 1, 'alpha': 0.5}})

# for hypothesis test
def stats_result(p,null_h,**kwargs):
    """
    Compares p value to alpha and outputs whether or not the null hypothesis
    is rejected or if it failed to be rejected.
    DOES NOT HANDLE 1-TAILED T TESTS
    
    Required inputs:  p, null_h (str)
    Optional inputs: alpha (default = .05), chi2, r, t, corr
    
    """
    #Get alpha value - Default to .05 if not provided
    alpha=kwargs.get('alpha',.05)
    #get any additional statistical values passed (for printing)
    t=kwargs.get('t',None)
    r=kwargs.get('r',None)
    chi2=kwargs.get('chi2',None)
    corr=kwargs.get('corr',None)
    
    #Print null hypothesis
    print(f'\n\033[1mH\u2080:\033[0m {null_h}')
    #Test p value and print result
    if p < alpha: print(f"\033[1mWe reject the null hypothesis\033[0m, p = {p} | α = {alpha}")
    else: print(f"We failed to reject the null hypothesis, p = {p} | α = {alpha}")
    #Print any additional values for reference
    if 't' in kwargs: print(f'  t: {t}')
    if 'r' in kwargs: print(f'  r: {r}')
    if 'chi2' in kwargs: print(f'  chi2: {chi2}')
    if 'corr' in kwargs: print(f'  corr: {corr}')

    return None