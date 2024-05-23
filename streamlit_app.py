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
    
    st.write("1. Jim's Listing: 5 guests, 3 bedrooms, 4 beds, 2 baths")
    Jim = pd.read_csv("jim_airbnb_data.csv")
    st.write(Jim)
    
    st.write("2. Alex's Listing: 6 guests, 2 bedrooms, 3 beds, 2 baths")
    Alex = pd.read_csv("alex_airbnb_data.csv")
    st.write(Alex)
    
    st.write("3. Glenda's Listing: 5 guests, 3 bedrooms, 4 beds, 2 baths")
    Glenda = pd.read_csv("glenda_airbnb_data.csv")
    st.write(Glenda)
    
    
    st.write("4. Joshua's Listing: 4 guests, 2 bedrooms, 2 beds, 1 bath")
    Joshua = pd.read_csv("joshua_airbnb_data.csv")
    st.write(Joshua)
    
    st.write("5. Prince's Listing: 4 guests, 2 bedrooms, 2 beds, 1 bath")
    Prince = pd.read_csv("prince_airbnb_data.csv")
    st.write(Prince)
    
    
    st.write("6. Tiffany's Listing: 4 guests, 2 bedrooms, 4 beds, 1 bath")
    Tiffany = pd.read_csv("tiffany_airbnb_data.csv")
    st.write(Tiffany)
    
    
    st.write("7. Michael's Listing: 6 guests, 2 bedrooms, 2 beds, 2.5 baths")
    Michael = pd.read_csv("michael_airbnb_data.csv")
    st.write(Michael)
    
    st.write("8. Noorani's Listing: 3 guests, 2 bedrooms, 1 bath")
    Noorani = pd.read_csv("noorani_airbnb_data.csv")
    st.write(Noorani)
    
    
    st.write("9. Andy's Listing: 5 guests, 2 bedrooms, 3 beds, 1 bath")
    Andy = pd.read_csv("andy_airbnb_data.csv")
    st.write(Andy)
    
    st.write("10. Donghong's Listing: 3 guests, 2 bedrooms, 5 beds, 1 bath")
    Donghong = pd.read_csv("donghong_airbnb_data.csv")
    st.write(Donghong)
    
    st.subheader("Merged Airbnb Data")
    hosts = ["Jim", "Alex", "Glenda", "Joshua", "Prince", "Tiffany", "Michael", "Noorani", "Andy"]
    
    dfs = [pd.read_csv(f"{host.lower()}_airbnb_data.csv") for host in hosts]
    for host, df in zip(hosts, dfs):
        df["Host"] = host
        
    AirbnbData = pd.concat(dfs, ignore_index=True)
    AirbnbData.drop(columns=["URL"], inplace=True)  # Drop the "URL" column and fill NaN values with 0
    AirbnbData.fillna(0, inplace=True)
   
    st.subheader("Merged Airbnb Data")
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

