# -*- coding: utf-8 -*-
"""
Created on Sat May  3 11:13:30 2025

@author: test_user

Airline Delay Threshold Test
"""

# Import packages
import pandas as pd

# Import Airline Data
df_2019 = pd.read_csv(r"C:\Users\test_user\Documents\datasets\Kaggle\Airline_Delay\2019.csv")

# Calculate Test Metric for Threshold
dep_exceptions = df_2019[df_2019.DEP_DELAY > 60].copy()
count_dep_exceptions = dep_exceptions.DEP_DELAY.count()
total_fights = df_2019.DEP_DELAY.count()
test_metric = count_dep_exceptions / total_fights
print(test_metric)

# Take Sample if Threshold Breeched
if test_metric > 0.05:
    sample_exceptions = dep_exceptions.sample(30)
    sample_exceptions.to_excel(r'C:\Users\test_user\Documents\output\sample_exceptions.xlsx')
    print("Threshold exceeded.  Sample of exceptions created.")