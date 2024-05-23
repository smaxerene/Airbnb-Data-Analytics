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
    st.write("Modern Private · Albany Centre · WiFi · 2 Garage")
    st.write("Entire townhouse in Auckland, New Zealand")
    st.write("5 guests, 3 bedrooms, 4 beds, 2 baths")
    st.write(Jim)
    
    Alex = pd.read_csv("alex_airbnb_data.csv")
    st.write("Modern Private Home, Full kitchen with 2bathroom")
    st.write("Entire home in Auckland, New Zealand")
    st.write("6 guests, 2 bedrooms, 3 beds, 2 baths")
    st.write(Alex)
    
    Glenda = pd.read_csv("glenda_airbnb_data.csv")
    st.write("Sleek Urban Oasis In Albany")
    st.write("Entire rental unit in Auckland, New Zealand")
    st.write("5 guests, 3 bedrooms, 4 beds, 2 baths")
    st.write(Glenda)
    
    Joshua = pd.read_csv("joshua_airbnb_data.csv")
    st.write("Luxury 2 BDR apartment w/ designer interior")
    st.write("Entire rental unit in Auckland, New Zealand")
    st.write("4 guests, 2 bedrooms, 2 beds, 1 bath")
    st.write(Joshua)
    
    Prince = pd.read_csv("prince_airbnb_data.csv")
    st.write("7 mins drive to Albany Centre, Private & elegant")
    st.write("Entire home in Auckland, New Zealand")
    st.write("4 guests, 2 bedrooms, 2 beds, 1 bath")
    st.write(Prince)
    
    Tiffany = pd.read_csv("tiffany_airbnb_data.csv")
    st.write("Pinehill 2 Bedroom Unit")
    st.write("Entire home in Auckland, New Zealand")
    st.write("4 guests, 2 bedrooms, 4 beds, 1 bath")
    st.write(Tiffany)
    
    Michael = pd.read_csv("michael_airbnb_data.csv")
    st.write("Luxury brand new house with free parking")
    st.write("Entire home in Auckland, New Zealand")
    st.write("6 guests, 2 bedrooms, 2 beds, 2.5 baths")
    st.write(Michael)
    
    Noorani = pd.read_csv("noorani_airbnb_data.csv")
    st.write("Delightful Double Bedroom Unit")
    st.write("Entire home in Auckland, New Zealand")
    st.write("3 guests, 2 bedrooms, 1 bath")
    st.write(Noorani)
    
    Andy = pd.read_csv("andy_airbnb_data.csv")
    st.write("Top Schoolzone+Top Golf+Top Location - By the Bay！")
    st.write("Entire home in Auckland, New Zealand")
    st.write("5 guests, 2 bedrooms, 3 beds, 1 bath")
    st.write(Andy)
    
    Donghong = pd.read_csv("donghong_airbnb_data.csv")
    st.write("Harbour View Guesthouse")
    st.write("Entire rental unit in Auckland, New Zealand")
    st.write("3 guests, 2 bedrooms, 5 beds, 1 bath")
    st.write(Donghong)
    
    st.subheader("Merged Airbnb Data")
    AirbnbData = pd.concat([Jim, Alex, Glenda, Joshua, Prince, Tiffany, Michael, Noorani, Andy], ignore_index=True)
    AirbnbData.drop(columns=["URL"], inplace=True)  # Drop the "URL" column
    AirbnbData.fillna(0, inplace=True)  # Fill NaN values with 0
    st.write(AirbnbData)
    
    st.subheader("Scatter Plots")
    fig, axes = st.pyplot(return_figure=True)
    axes = fig.subplots(3, 3, figsize=(15, 15)).flatten()
    for i, col in enumerate(AirbnbData.columns[1:]):  # Skip the first column which is 'Jim'
        axes[i].scatter(AirbnbData['Jim'], AirbnbData[col])
        axes[i].set_title(f'Comparison of Prices between Jim and {col.split()[0]} Listings')
        axes[i].set_xlabel("Jim's Price")
        axes[i].set_ylabel(f"{col.split()[0]}'s Price")
        axes[i].grid(True)

    fig.tight_layout()
    
    st.subheader("Average Price Trend")
    average_price_trend = AirbnbData.mean(axis=1)
    st.line_chart(average_price_trend)
    
    st.subheader("Cosine Similarity Matrix")
     
    st.subheader("Prices Across All Listings Over 90 Days of Unbooked Data")
  
  
if __name__ == "__main__":
    main()

