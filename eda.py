import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import config
import os
import re



# load the data,lets start with one dataset
Data1 = pd.read_csv(os.path.join(config.path_dataset,'1- mental-illnesses-prevalence.csv'))
Data2=pd.read_csv(os.path.join(config.path_dataset,'4- adult-population-covered-in-primary-data-on-the-prevalence-of-mental-illnesses.csv'))
Data3 = pd.read_csv(os.path.join(config.path_dataset,"6- depressive-symptoms-across-us-population.csv"))
Data4 = pd.read_csv(os.path.join(config.path_dataset,"7- number-of-countries-with-primary-data-on-prevalence-of-mental-illnesses-in-the-global-burden-of-disease-study.csv"))


df1 = pd.DataFrame(Data1)
df2 = pd.DataFrame(Data2)
df3 = pd.DataFrame(Data3)
df4 = pd.DataFrame(Data4)

#print(df1.shape)
#(df1.columns.tolist())


#print(df2.shape)
#print(df2.columns.tolist())



#print(df3.shape)
#print(df3.columns.tolist())
# תצוגה ראשונית
#print(df4.shape)
#print(df4.columns.tolist())

#df = df[['Age', 'Gender', 'Country', 'self_employed', 'family_history', 'treatment']]
#df = df.dropna()


#print(df1.columns)
#print(df1.dtypes)
#print('is na sum is: ',df1.isna().sum())

# תיאור כללי של משתנים מספריים
#print(df1.describe())
# גרף: גיל לפי טיפול

def describe(df):
    return pd.DataFrame({
        'variable': df.columns,
        'dtype': df.dtypes.values,
        'count': df.count().values,
        'unique': [df[col].nunique() for col in df.columns],
        'missing': df.isna().sum().values
    })

print(describe(df1))

#i think we need to drop the use of the code, too much NA values.

df1 = df1.drop(columns=['Code'])

# פונקציה שמנקה כל שם עמודה
def clean_column(col):
    return re.sub(r"(disorders\b).*", r"\1", col)

pd.set_option('display.max_columns', None)  # תראה את כל העמודות
# מחליף שמות עמודות בטבלה
df1.columns = [clean_column(col) for col in df1.columns]
numeric_cols = df1.select_dtypes(include='float').columns

#print(describe(df1))



#print(df1[numeric_cols].describe())



print(df1[numeric_cols].describe())

