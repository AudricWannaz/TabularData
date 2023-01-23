import streamlit as st
import pandas as pd


st.image('tower.jpg')
st.title('Tabular Data - Streamlit')


@st.cache
def load_data(choice):
	df1 = pd.read_csv('toy_dataset_aeneid.csv')
	df2 = pd.read_csv('toy_dataset_inscriptionsLong.csv')
	df3 = pd.read_csv('toy_dataset_papyriLetters.csv')
	df4 = pd.read_csv('toy_dataset_tragedy.csv')
	if choice == 1:
		return df1
	elif choice == 2:
		return df2
	elif choice == 3:
		return df3
	elif choice == 4:
		return df4

#some strange typing happened with the inscriptions data

st.sidebar.header('1. First, select a dataset')
choice = st.sidebar.selectbox('Choose one: ',[1,2,3,4])
df = load_data(choice)


st.header('2. Voilà, this is the dataset you chose!')
st.write(df)

st.header('3. Streamlit is way more than that. Have a look at https://streamlit.io/gallery')