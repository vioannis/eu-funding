#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv


# In[2]:


# Read local .csv dataset
source = pd.read_csv('EU_Database.csv')


# In[3]:


source


# In[4]:


# 1 
# Each year's funding amount and spend
# Create 2 dictionaries, key is year, value is total funding each year
# and total expense each year, respectively
di_fund = {}
di_spend = {}
for i in range(len(source)):
  if source.iloc[i]['Year'] not in di_fund:
    di_fund[source.iloc[i]['Year']] = source.iloc[i]['EU_Payment_annual']
  else:
    di_fund[source.iloc[i]['Year']] += source.iloc[i]['EU_Payment_annual']
  if source.iloc[i]['Year'] not in di_spend:
    di_spend[source.iloc[i]['Year']] = source.iloc[i]['Modelled_annual_expenditure']
  else:
    di_spend[source.iloc[i]['Year']] += source.iloc[i]['Modelled_annual_expenditure']


# In[5]:


di_fund


# In[6]:


di_spend


# In[7]:


# Plot fund vs. year
di_fund_names = sorted(list(di_fund.keys()))
di_fund_values = sorted(list(di_fund.values()))

plt.bar(range(len(di_fund)), di_fund_values, tick_label=di_fund_names)
plt.xticks(rotation=45)
plt.xlabel("Year")
plt.ylabel("Funding Amount")
plt.title('Funding vs Year')
plt.show()


# In[8]:


# Plot spend vs. year
di_spend_names = sorted(list(di_spend.keys()))
di_spend_values = sorted(list(di_spend.values()))

plt.bar(range(len(di_spend)), di_spend_values, tick_label=di_spend_names)
plt.xticks(rotation=45)
plt.xlabel("Year")
plt.ylabel("Spend Amount")
plt.title('Spend vs Year')
plt.show()


# In[9]:


# 2
# Top 10 fund ID and payment
di_id_payment = {}
for i in range(len(source)):
  if source.iloc[i]['NUTS2_ID'] not in di_id_payment:
    di_id_payment[source.iloc[i]['NUTS2_ID']] = source.iloc[i]['EU_Payment_annual']
  else:
    di_id_payment[source.iloc[i]['NUTS2_ID']] += source.iloc[i]['EU_Payment_annual']


# In[10]:


# Sort di_id_payment based on value from the largest to the smallest
di_id_payment_sorted = sorted(di_id_payment.items(),key=lambda di_id_payment:di_id_payment[1], reverse = True)
di_id_payment_sorted


# In[11]:


# Plot Top 10 fund vs. id
di_id_payment_top10 = di_id_payment_sorted[:10]
top10_id = []
top10_fund = []
for i in range(len(di_id_payment_top10)):
    top10_id.append(di_id_payment_top10[i][0])
    top10_fund.append(di_id_payment_top10[i][1])

plt.bar(range(10), top10_fund, tick_label=top10_id)
plt.xticks(rotation=45)
plt.xlabel("ID")
plt.ylabel("Fund")
plt.title('Top 10 Fund vs ID')
plt.show()


# In[12]:


# 3
# Fund usage analysis, check whether each fund is nearly 100% used
di_id_spend = {}
for i in range(len(source)):
  if source.iloc[i]['NUTS2_ID'] not in di_id_spend:
    di_id_spend[source.iloc[i]['NUTS2_ID']] = source.iloc[i]['Modelled_annual_expenditure']
  else:
    di_id_spend[source.iloc[i]['NUTS2_ID']] += source.iloc[i]['Modelled_annual_expenditure']


# In[13]:


di_id_usage = {}
for id in di_id_spend.keys():
    di_id_usage[id] = round(di_id_payment[id] / di_id_spend[id], 3)
di_id_usage


# In[14]:


# 4
# Which country receives the most amount of funds? (i.e. which country is preferred by the funding giver?)
country_fund_amount = {}
for i in range(len(source)):
    if source.iloc[i]['Country'] not in country_fund_amount:
        country_fund_amount[source.iloc[i]['Country']] = source.iloc[i]['EU_Payment_annual']
    else:
        country_fund_amount[source.iloc[i]['Country']] += source.iloc[i]['EU_Payment_annual']


# In[15]:


# Sort country_fund_amount based on value from the largest to the smallest
country_fund_amount_sorted = sorted(country_fund_amount.items(),key=lambda country_fund_amount:country_fund_amount[1], reverse = True)
country_fund_amount_sorted


# In[16]:


# Plot Countries with Top 10 fund
country_fund_amount_top10 = country_fund_amount_sorted[:10]
top10_country = []
top10_amount = []
for i in range(len(country_fund_amount_top10)):
    top10_country.append(country_fund_amount_top10[i][0])
    top10_amount.append(country_fund_amount_top10[i][1])

plt.bar(range(10), top10_amount, tick_label=top10_country)
plt.xticks(rotation=45)
plt.xlabel("Country Code")
plt.ylabel("Fund Amount")
plt.title('Top 10 Countries with Most Total Funds')
plt.show()

