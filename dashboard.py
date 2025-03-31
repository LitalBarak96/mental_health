import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import config
import os
import re


df1 = pd.read_csv(os.path.join(config.path_dataset,'1- mental-illnesses-prevalence.csv'))

df1 = df1.drop(columns=['Code'])
def clean_column(col):
    return re.sub(r"(disorders\b).*", r"\1", col)

pd.set_option('display.max_columns', None)  # תראה את כל העמודות
# מחליף שמות עמודות בטבלה
df1.columns = [clean_column(col) for col in df1.columns]

# כותרת לדאשבורד
st.title("mental health dashboard")

# תפריט בחירה של מדינה
countries = sorted(df1['Entity'].dropna().unique())
selected_country = st.selectbox("choose country", countries)

# סינון לפי מדינה
country_df = df1[df1['Entity'] == selected_country]

# גרף: דיכאון לאורך זמן
fig, ax = plt.subplots()
sns.lineplot(data=country_df, x="Year", y="Depressive disorders", ax=ax)
ax.set_title(f'Depression rate over time in {selected_country}')
ax.set_ylabel("Depression (%)")
st.pyplot(fig)

