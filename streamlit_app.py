#Streamlit: Airbnb Data Analytics

# Importing necessary libraries
import streamlit as st 
import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def main():
    st.title("Airbnb Data Analytics")
    st.text("")

    st.subheader("Individual Airbnb Data")
    Jim = pd.read_csv("jim_airbnb_data.csv")
    st.write(Jim)
    
    Alex = pd.read_csv("alex_airbnb_data.csv")
    st.write(Alex)
    
    Glenda = pd.read_csv("glenda_airbnb_data.csv")
    st.write(Glenda)
    
    Joshua = pd.read_csv("joshua_airbnb_data.csv")
    st.write(Joshua)
    
    Prince = pd.read_csv("prince_airbnb_data.csv")
    st.write(Prince)
    
    Tiffany = pd.read_csv("tiffany_airbnb_data.csv")
    st.write(Tiffany)
    
    Michael = pd.read_csv("michael_airbnb_data.csv")
    st.write(Michael)
    
    Noorani = pd.read_csv("noorani_airbnb_data.csv")
    st.write(Noorani)
    
    Andy = pd.read_csv("Andy_airbnb_data.csv")
    st.write(Andy)
    
    Donghong = pd.read_csv("Donghong_airbnb_data.csv")
    st.write(Donghong)
    
    st.subheader("Merged Airbnb Data")
    AirbnbData = pd.concat([Jim, Alex, Glenda, Joshua, Prince, Tiffany, Michael, Noorani, Andy], ignore_index=True)
    AirbnbData.drop(columns=["URL"], inplace=True)  # Drop the "URL" column
    AirbnbData.fillna(0, inplace=True)  # Fill NaN values with 0
    st.write(AirbnbData)
    
    
    st.subheader("Comparison between Jim's Price and Other Listings' Prices")
    for name in ["Alex", "Glenda", "Joshua", "Prince", "Tiffany", "Michael", "Noorani", "Andy"]:
    st.write(f"## Scatter Plot: Jim vs {name}")
    scatter_chart = st.pyplot()  # Create a placeholder for the plot
    scatter_chart.pyplot(plt.scatter(AirbnbData["Jim"], AirbnbData[name], alpha=0.5))
    scatter_chart.pyplot(plt.xlabel("Jim"))
    scatter_chart.pyplot(plt.ylabel(name))
    
    
    st.subheader("Average Price Trend")
    
    st.subheader("Cosine Similarity Matrix")
     
    st.subheader("Prices Across All Listings Over 90 Days of Unbooked Data")
  
  
if __name__ == "__main__":
    main()

