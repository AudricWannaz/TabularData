import streamlit as st
import pandas as pd
import streamlit_pandas as sp

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

st.header('1. First, select a dataset')
choice = st.selectbox('Choose one: ',[1,2,3,4])
df = load_data(choice)

create_data = {
	"speaker":"select",
	"play":"select"

}



st.header('2. View the complete dataset')
st.write(df)

st.sidebar.header('3. Filter with sidebar options')

all_widgets = sp.create_widgets(df,
	create_data,
	ignore_columns=[])
	#ignore_columns=["glem_report"]) 
res = sp.filter_df(df, all_widgets)

st.header('4. View the modified table')
st.write(res)


#https://github.com/wjbmattingly/streamlit-pandas
#came at perfect time for workshop

#depencies installed on bologna
#1 streamlit
#2 pandas streamlit
