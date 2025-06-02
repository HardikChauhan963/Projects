import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from scipy.stats import chi2_contingency
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, precision_recall_fscore_support
import warnings
import os

a1 = pd.read_excel("E:\Course\Data Science\Projects\Credit Risk Modelling\case_study1.xlsx")
a2 = pd.read_excel("E:\Course\Data Science\Projects\Credit Risk Modelling\case_study2.xlsx")

df1 = a1.copy()
df2 = a2.copy()


#In case_study_1, Age_Oldest_TL column conatins 40 null values (which is negligible as compared to 51336 rows, so we can remove those rows)
df1 = df1.loc[df1['Age_Oldest_TL'] != -99999]                           # -9999 is the placeholder of null values

#In case_study_2, there are a lot of null values in different columns and imputing the null values with mean, median mode will be risky. 
#So, if any column conains >20% null values (~ 10000) then we will remove that column and if it contains < 20% null values then we will remove rows conatining those null values. 

#Dropping columns
columns_to_be_removed = []
for i in df2.columns:
    if df2.loc[df2[i] == -99999].shape[0]>10000:
        columns_to_be_removed.append(i)
        
df2 = df2.drop(columns_to_be_removed, axis = 1)


#Dropping rows
for i in df2.columns:
    df2 = df2.loc[df2[i] != -99999]

df2.isna().sum().sum()


#Now we have to merge both the tables on the common column name
for i in df1.columns:
    if i in df2.columns:
        print (i)

df = pd.merge(df1, df2, on = 'PROSPECTID', how = 'inner',)



#We will treat categorical and numerical columns separately. 
cat_cols = [i for i in df.columns if df[i].dtype == 'object']
print (cat_cols)

# In the cat_cols we have 6 categorical columns out of which 6th is our target column.
# Now we have to see which cat_cols are significant for our target variable.
# To check the association of categorical column ['MARITALSTATUS', 'EDUCATION', 'GENDER', 'last_prod_enq2', 'first_prod_enq2'] with categorical column (Approved flag) we will do Chi-square test
#If p_value in Chi-square test <= 0.05 then we can say there is association between particular column and target variable.

#Chi-square test
#H0: categorical columns are not associated with target column. 

for i in cat_cols: 
    if i == 'Approved_Flag':
        continue
    chi2, pval, _, _ = chi2_contingency(pd.crosstab(df[i], df['Approved_Flag']))
    print( i,'-----' ,pval)

# Since all categorical columns have pval < 0.05 therefore we will reject H0 and accept all columns for further analysis.




#Now we will check for numerical columns
numeric_columns = []
for i in df.columns:
    if df[i].dtype != 'object' and (i != 'PROSPECTID' and i != 'Approved_Flag'):
        numeric_columns.append(i)
print (numeric_columns)

# Now we will check which of these 72 numerical columns are associated with target columns.
# Since it is numerical vs categorical (> 2 categories) so we will use Anova test.
# Before, that we will check whether these independent columns are associated to each other or not. So we will check VIF
# VIF stands for "Variance Inflation Factor," which is a metric used to detect and quantify the severity of multicollinearity. 

#VIF sequentially check

vif_data = df[numeric_columns]
total_columns = vif_data.shape[1]
columns_to_be_kept = []
column_index = 0



for i in range (0,total_columns):
    
    vif_value = variance_inflation_factor(vif_data, column_index)
    print (column_index,'---',vif_value)
    
    
    if vif_value <= 6:
        columns_to_be_kept.append( numeric_columns[i] )
        column_index = column_index+1
            
    else:
       vif_data = vif_data.drop([numeric_columns[i]], axis = 1)        

    
#Now we will do ANOVA check for the 39 variables from columns_to_be_kept list
#If p_value in ANOVA test <= 0.05 then we can say there is association between particular column and target variable. 

from scipy.stats import f_oneway

columns_to_be_kept_numerical = []
for i in columns_to_be_kept:
    a = list(df[i])
    b = list(df['Approved_Flag'])
    
    group_P1 = [value for value, group in zip(a,b) if group == 'P1']
    group_P2 = [value for value, group in zip(a,b) if group == 'P2']
    group_P3 = [value for value, group in zip(a,b) if group == 'P3']
    group_P4 = [value for value, group in zip(a,b) if group == 'P4']
    
    f_statistics, p_value = f_oneway(group_P1, group_P2, group_P3, group_P4)
    
    if p_value <= 0.05:
        columns_to_be_kept_numerical.append(i)

# listing all the final features
features = columns_to_be_kept_numerical + ['MARITALSTATUS', 'EDUCATION', 'GENDER', 'last_prod_enq2', 'first_prod_enq2']
df = df[features + ['Approved_Flag']]

#Since, p_value for 37 numeric columns are less than 0.05. Therefore, we will keep them for further  analysis
    
# -----------------
## Now fetaure selection is done. In total we have 6 categorical columns and 37 numeric columns.
#------------------



# Now we cant feed categorical columns directly. Therefore, we will do encoding.
df['EDUCATION'].unique()
df['MARITALSTATUS'].unique()
df['GENDER'].unique()
df['last_prod_enq2'].unique()
df['first_prod_enq2'].unique()

# Since Education can be seen as good signal. Thereofre, we we do label encoding for it.
# For all other columns we will do one hot encoding.

# My rule for label encoding for Education is as follows-

## Ordinal feature -- EDUCATION
#--------------------------------
# SSC            : 1
# 12TH           : 2
# GRADUATE       : 3
# UNDER GRADUATE : 3
# POST-GRADUATE  : 4
# OTHERS         : 1- Considering others to be uneducated
# PROFESSIONAL   : 3


df["EDUCATION"] = df["EDUCATION"].replace({
    "SSC": 1,
   "12TH": 2,
   "GRADUATE": 3,
   "UNDER GRADUATE" : 3,
   "POST-GRADUATE"  : 4,
   "OTHERS" : 1,
   "PROFESSIONAL" :3 })


df['EDUCATION'].value_counts()
df['EDUCATION'] = df['EDUCATION'].astype(int)
df.info()


df_encoded = pd.get_dummies(df, columns = ['MARITALSTATUS','GENDER', 'last_prod_enq2', 'first_prod_enq2'])
#df_encoded is our new data set for further process.


# Machine Learning model fitting
# Data processing
#1. Random forest

y = df_encoded['Approved_Flag']
x = df_encoded.drop(['Approved_Flag'], axis =1)


x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2, random_state = 42)

rf_classifier = RandomForestClassifier(n_estimators = 200, random_state = 42)

rf_classifier.fit(x_train, y_train)

y_pred = rf_classifier.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)

print(f'Accuracy: {accuracy}')
      
precision, recall, f1_score, _ = precision_recall_fscore_support(y_test, y_pred)
    

for i, v in enumerate(['p1', 'p2', 'p3', 'p4']):
    print(f"Class {v}:")
    print(f"Precision: {precision[i]}")
    print(f"Recall: {recall[i]}")
    print(f"F1 Score: {f1_score[i]}")
    print()


#2: xgboost
import xgboost as xgb
from sklearn.preprocessing import LabelEncoder

xgb_classifier = xgb.XGBClassifier(objective='multi:softmax',  num_class=4)



y = df_encoded['Approved_Flag']
x = df_encoded. drop ( ['Approved_Flag'], axis = 1 )


label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)


x_train, x_test, y_train, y_test = train_test_split(x, y_encoded, test_size=0.2, random_state=42)




xgb_classifier.fit(x_train, y_train)
y_pred = xgb_classifier.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print ()
print(f'Accuracy: {accuracy:.2f}')
print ()

precision, recall, f1_score, _ = precision_recall_fscore_support(y_test, y_pred)

for i, v in enumerate(['p1', 'p2', 'p3', 'p4']):
    print(f"Class {v}:")
    print(f"Precision: {precision[i]}")
    print(f"Recall: {recall[i]}")
    print(f"F1 Score: {f1_score[i]}")
    print()

    

# 3. Decision Tree
from sklearn.tree import DecisionTreeClassifier


y = df_encoded['Approved_Flag']
x = df_encoded. drop ( ['Approved_Flag'], axis = 1 )

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


dt_model = DecisionTreeClassifier(max_depth=20, min_samples_split=10)
dt_model.fit(x_train, y_train)
y_pred = dt_model.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print ()
print(f"Accuracy: {accuracy:.2f}")
print ()

precision, recall, f1_score, _ = precision_recall_fscore_support(y_test, y_pred)

for i, v in enumerate(['p1', 'p2', 'p3', 'p4']):
    print(f"Class {v}:")
    print(f"Precision: {precision[i]}")
    print(f"Recall: {recall[i]}")
    print(f"F1 Score: {f1_score[i]}")
    print()


#Accuracy Score: 
   # Random forest = 0.76
   # xgboost = 0.78
   # Decision tree = 0.71


