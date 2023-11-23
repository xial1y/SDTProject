import streamlit as st
import pandas as pd
import plotly.express as px
from matplotlib import pyplot as plt

df = pd.read_csv("file:///Users/sallyhuang/SDTProject/vehicles_us.csv")

#header 

st.header('Used Vehicles for Sale')

#data viewer 

st.header("Data Viewer")
@st.cache 
def load_data(): 
    return df

def main():
    st.write(df)

if __name__ == "__main__": 
    main()  


#histogram

#general price distribution
st.title("Histogram of Price Distrubution")
hist_price = px.histogram(df, x = "price", nbins = 70, range_x = 
[0, 80000])
st.plotly_chart(hist_price)

#scatterplots 
st.title("Scatterplot of Price VS. Model Year Distrubution")
model_year_price = px.scatter(df, x = "price", y = "model_year")
st.plotly_chart(model_year_price)

st.title("Scatterplot of Price VS. Vehicle Type Distrubution")
price_type = px.scatter(df, x = "price", y = "type")
st.plotly_chart(price_type)


#interactive histograms

#added to remove warning that was on webpage after running app.py 
st.set_option('deprecation.showPyplotGlobalUse', False) 

#price vs car types histogram
def price_type(df): 

    #making sidebar widget to take different car type as input 
    select_type = st.sidebar.selectbox("select vehicle types", df["type"].unique())

    #filter to get the car type selected
    filtered_type = df[df["type"] == select_type]

    #histogram of price column of selected vehicle 
    plt.hist(filtered_type["price"], bins = 20, color = "lightblue")
    plt.title("Price Distribution for {}".format(select_type))
    plt.xlabel("Price in USD")
    plt.ylabel("Frequency")
    #added range limit since distribution is right skewed 
    plt.xlim(0, 200000)

    #displaying message 
    st.title("Vehicle Price VS. Vehicle Type")
    st.write("select different vehicle type to visualize price distribution")

    #displaying
    st.pyplot()

#interactive hiatogram of vehicle price for model year

def price_year(df):

    #sidebar widget to input model year user want to see 
    select_year = st.sidebar.selectbox("select a Model Year", df['model_year'].unique())

    #filter to display model years that matches the selected year
    filter_price_year = df[df["model_year"] == select_year]

    #histogram of price distribution for different car models of the selected year
    plt.hist(filter_price_year['price'], bins = 10, color = "lightgreen")

    #checkbox widget to normalize histogram if checked
    show_normal_hist = st.sidebar.checkbox("Display as normalize histogram")
    if show_normal_hist:
        _, bins, _ = plt.hist(filter_price_year['price'], bins = 10, color = "lightgreen")
    else:
        plt.hist(filter_price_year['price'], bins = 5, color = "green")

    
    plt.title("Price distribution for vehicles model year {}".format(select_year))
    plt.xlabel("Price (in USD)")
    plt.ylabel("Frequency")

    st.title("Distribution of price for different Vehicle model year")
    st.write("select different years to visualize cost distribution for vehicle models of that year")
    st.pyplot()


if __name__ == '__main__':
    price_type(df)
    price_year(df)