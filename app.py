import seaborn as sns
import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

#load Titanic dataset
@st.cache_data
def load_data():
    data = pd.read_csv(r"C:\Users\vemer\Documents\Naresh Technology\New\21st FEB EDA\titanic dataset.csv")
    return data

data = load_data()

#Title and description
st.title('Exploratoy data analysis of Titan Dataset')
st.write(" This is an EDA on the titanic dataset")
st.write("First few rows of dataset:")
st.dataframe(data.head())

#data cleaning section
st.subheader('Missing values')
missing_data=data.isnull().sum()
st.write(missing_data)

if st.checkbox('Fill missing Age with median'):
    data['Age'].fillna(data['Age'].mean(), inplace=True)

if st.checkbox('Fill missing Embarked with mode'):
    data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)

if st.checkbox('Drop duplicates'):
    data.drop_duplicates(inplace=True)

st.subheader('Cleaned Dataset')
st.dataframe(data.head())

# EDA Section
st.subheader('Statistical Summary of the Data')
st.write(data.describe())

# Age Distribution
st.subheader('Age Distribution')
fig, ax = plt.subplots()
sns.histplot(data['Age'], kde=True, ax=ax)
ax.set_title('Age Distribution')
st.pyplot(fig)

# Gender Distribution
st.subheader('Gender Distribution')
fig, ax = plt.subplots()
sns.countplot(x='Sex', data=data, ax=ax)
ax.set_title('Gender Distribution')
st.pyplot(fig)

# Pclass vs Survived
st.subheader('Pclass vs Survived')
fig, ax = plt.subplots()
sns.countplot(x='Pclass', hue='Survived', data=data, ax=ax)
ax.set_title('Pclass vs Survived')
st.pyplot(fig)

'''
# Correlation Heatmap
st.subheader('Correlation Heatmap')
fig, ax = plt.subplots()
data = pd.get_dummies(data)
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', ax=ax)
#sns.heatmap(data.corr(), annot=True, cmap='coolwarm', ax=ax)
ax.set_title('Correlation Heatmap')
st.pyplot(fig)

'''

# Feature Engineering Section
st.subheader('Feature Engineering: Family Size')
data['FamilySize'] = data['SibSp'] + data['Parch']
fig, ax = plt.subplots()
sns.histplot(data['FamilySize'], kde=True, ax=ax)
ax.set_title('Family Size Distribution')
st.pyplot(fig)

# Conclusion Section
st.subheader('Key Insights')
insights = """
- Females have a higher survival rate than males.
- Passengers in 1st class had the highest survival rate.
- The majority of passengers are in Pclass 3.
- Younger passengers tended to survive more often.
"""
st.write(insights)

