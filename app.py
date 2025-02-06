import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Data Visualization web application")

# TODO: Load and describe dataset
co2_df = pd.read_csv('data/CO2_per_capita.csv', delimiter=';')

st.dataframe(co2_df)


st.dataframe(co2_df.describe())

#construction top 10
# TODO: Transform your data so that you can easily plot it
co2_df_filtered = co2_df[co2_df["Year"]>=2008]
co2_df_by_country = co2_df_filtered[["Country Name", "CO2 Per Capita (metric tons)"]].groupby("Country Name", as_index=False).mean()
co2_df_top = co2_df_by_country.sort_values("CO2 Per Capita (metric tons)", ascending=False)[:10]

fig = px.bar(co2_df_top, x="Country Name", y="CO2 Per Capita (metric tons)")
st.plotly_chart(fig)

def top_n_emitters(df, start_year=2008, end_year=2011, nb_displayed=10):
    
    co2_df_filtered = df[(df["Year"]>=start_year)&(df["Year"]<=end_year)]
    
    co2_df_by_country = co2_df_filtered[["Country Name", "CO2 Per Capita (metric tons)"]].groupby("Country Name", as_index=False).mean()

    co2_df_top = co2_df_by_country.sort_values("CO2 Per Capita (metric tons)", ascending=False)[:nb_displayed]
    
    fig = px.bar(co2_df_top, x="Country Name", y="CO2 Per Capita (metric tons)")
    
    return fig, co2_df_top


start_year, end_year = st.slider('choose years',  min_value=1970, max_value=2011,value=(2000, 2011))
n_displayed = st.selectbox("Select number of country to diplay", [3,5,10,20,30], index=2)

fig1, df= top_n_emitters(co2_df, start_year, end_year, n_displayed)
st.dataframe(df)
st.plotly_chart(fig1)
