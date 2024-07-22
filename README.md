# Software Development Tool Project
This project is aimed at analyzing and visualizing the price distribution of used vehicles of different types and model years using a dataset of used cars for sale.

Dataset
The dataset used in this project contains information about various used cars for sale. Before analyzing the data, we made sure to review it for any duplicate rows and find missing values and fill them accordingly; for the "is_4wd" column we replaced missing values with 0 since it is boolean type, for "cylinders" and "model year", we take the median value for each with the "type" column and replaced all the missing values with that median value. Lastly, for the odometer, we replaced the missing values with the mean odometer within each model year, however, there is still 1 missing odometer value due to model year 1929 only have 1 row of information. 

Analysis
To analyze and visualize the price distribution, we utilized several libraries. The main libraries used in the project are:
1. Pandas for data cleaning and manipulation.
2. Plotly Express for creating scatterplots to visualize the relationship between vehicle price and other columns
3. Matplotlib for creating histograms 
4. Streamlit to create interactive widgets that allows users to input different vehicle model years and types to view corresponding histograms of the cost distribution.

Instructions to run locally 
1. clone this repository to local machine
2. navigate to projec directory 
3. download/ make sure all necessay libraries are installed (pandas, plotly express, matplotlib, streamlit)
4. run the main python file app.py (streamlit run app.py)

View deployed version
link to render: https://used-vehicle-project.onrender.com/
