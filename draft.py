#Streamlit: Airbnb Data Analytics

# Importing necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import re
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Title of the Streamlit app
st.title("Airbnb Data Analytics")

# Function to scrape availability and pricing data for a listing
def scrape_listing_pricing(listing_url, guests, num_days):
    response = requests.get(listing_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    df = pd.DataFrame(columns=['Check-in Date', 'Check-out Date', 'Price in NZD', 'URL'])

    start_date = pd.Timestamp.now()
    current_date = start_date
    days_scraped = 0
    
    while days_scraped < num_days:
        checkin_date = current_date.strftime('%Y-%m-%d')
        checkout_date = (current_date + pd.Timedelta(days=1)).strftime('%Y-%m-%d')
        url = f"{listing_url}?check_in={checkin_date}&guests={guests}&adults={guests}&check_out={checkout_date}"

        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        price_element = soup.find(class_='_1y74zjx')
        
        if price_element:
            price_text = price_element.text.strip()
            price = re.search(r'\d+', price_text).group()
            new_row = pd.DataFrame({
                'Check-in Date': [checkin_date],
                'Check-out Date': [checkout_date],
                'Price in NZD': [price],
                'URL': [url]
            })
            df = pd.concat([df, new_row], ignore_index=True)
            days_scraped += 1

        current_date += pd.Timedelta(days=1)

    return df

# Function to scrape and save data
def scrape_and_save_data(listing_url, guests, num_days, filename):
    if os.path.exists(filename):
        df = pd.read_csv(filename)
        if len(df) >= num_days:
            return df.head(num_days)
    df = scrape_listing_pricing(listing_url, guests, num_days)
    df.to_csv(filename, index=False)
    return df

# Function to merge and process data
def merge_and_process_data(listings):
    Jim = pd.read_csv(listings["Jim"][1])
    Alex = pd.read_csv(listings["Alex"][1])
    Glenda = pd.read_csv(listings["Glenda"][1])
    Joshua = pd.read_csv(listings["Joshua"][1])
    Prince = pd.read_csv(listings["Prince"][1])
    Tiffany = pd.read_csv(listings["Tiffany"][1])
    Michael = pd.read_csv(listings["Michael"][1])
    Noorani = pd.read_csv(listings["Noorani"][1])
    Andy = pd.read_csv(listings["Andy"][1])
    Donghong = pd.read_csv(listings["Donghong"][1])

    # Merge Airbnb Data
    Jim.columns = ['Jim Check-in Date', 'Jim Check-out Date', 'Jim Price in NZD', 'URL']
    Alex.columns = ['Alex Check-in Date', 'Alex Check-out Date', 'Alex Price in NZD', 'URL']
    Glenda.columns = ['Glenda Check-in Date', 'Glenda Check-out Date', 'Glenda Price in NZD', 'URL']
    Joshua.columns = ['Joshua Check-in Date', 'Joshua Check-out Date', 'Joshua Price in NZD', 'URL']
    Prince.columns = ['Prince Check-in Date', 'Prince Check-out Date', 'Prince Price in NZD', 'URL']
    Tiffany.columns = ['Tiffany Check-in Date', 'Tiffany Check-out Date', 'Tiffany Price in NZD', 'URL']
    Michael.columns = ['Michael Check-in Date', 'Michael Check-out Date', 'Michael Price in NZD', 'URL']
    Noorani.columns = ['Noorani Check-in Date', 'Noorani Check-out Date', 'Noorani Price in NZD', 'URL']
    Andy.columns = ['Andy Check-in Date', 'Andy Check-out Date', 'Andy Price in NZD', 'URL']
    Donghong.columns = ['Donghong Check-in Date', 'Donghong Check-out Date', 'Donghong Price in NZD', 'URL']

    Airbnb = pd.concat([Jim, Alex, Glenda, Joshua, Prince, Tiffany, Michael, Noorani, Andy, Donghong], axis=1)
    Airbnb = Airbnb.drop(columns=[col for col in Airbnb.columns if 'URL' in col])
    
    names = sorted(set(col.split()[0] for col in Airbnb.columns))
    new_columns = []
    for name in names:
        new_columns.extend([f"{name} Check-in Date", f"{name} Check-out Date", f"{name} Price in NZD"])
    
    Airbnb = Airbnb[new_columns]
    AirbnbData = Airbnb.fillna(0)
    
    return AirbnbData

# Function to visualize comparison between Jim's price and other listings' prices
def visualize_price_comparison(data):
    st.subheader("Comparison between Jim's Price and Other Listings' Prices")
    
    # Visualization code
    fig, axes = plt.subplots(3, 3, figsize=(15, 15))
    axes = axes.flatten()
    for i, col in enumerate(data.columns[1:]):
        sns.scatterplot(x='Jim Price in NZD', y=col, data=data, ax=axes[i])
        axes[i].set_title(f'Comparison of Prices between Jim and {col.split()[0]} Listings')
        axes[i].set_xlabel("Jim's Price")
        axes[i].set_ylabel(f"{col.split()[0]}'s Price")
        axes[i].grid(True)

    plt.tight_layout()
    st.pyplot(fig)

# Function to visualize average price trend
def visualize_average_price_trend(data):
    st.subheader("Average Price Trend")
    average_price_trend = data.mean(axis=1)
    st.line_chart(average_price_trend)

# Function to calculate cosine similarity
def calculate_cosine_similarity(data):
    st.subheader("Cosine Similarity Matrix")
    price_columns = [col for col in data.columns if 'Price in NZD' in col]
    price_df = data[price_columns]
    similarity_matrix = np.corrcoef(price_df.values.T)
    sns.heatmap(similarity_matrix, annot=True, cmap='coolwarm', square=True, fmt=".2f", xticklabels=price_columns, yticklabels=price_columns)
    st.pyplot()

# Function to visualize prices across all listings
def visualize_prices_across_listings(data):
    st.subheader("Prices Across All Listings Over 90 Days of Unbooked Data")
    price_columns = [col for col in data.columns if 'Price in NZD' in col]
    all_prices = pd.DataFrame()
    for col in price_columns:
        temp_df = data[[col]].rename(columns={col: 'Price'})
        temp_df['Listing'] = col
        all_prices = pd.concat([all_prices, temp_df])
    sorted_prices = all_prices.sort_values(by='Price').reset_index(drop=True)
    fig, ax = plt.subplots(figsize=(14, 10))
    sns.lineplot(data=sorted_prices, x=sorted_prices.index, y='Price', hue='Listing', ax=ax)
    ax.set_xlabel('Number of Days')
    ax.set_ylabel('Price in NZD')
    ax.set_title('Prices Across All Listings Over 90 Days of Unbooked Data')
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
    st.pyplot(fig)

# Function to visualize Jim's listing price trend compared to average price trend
def visualize_jim_listing_price_trend(data):
    st.subheader("Jim's Listing Price Trend Compared to Average Price Trend")
    jim_price = data['Jim Price in NZD']
    average_price = data.mean(axis=1)
    plt.figure(figsize=(10, 6))
    plt.plot(jim_price, label="Jim's Listing Price", color='blue')
    plt.plot(average_price, label="Average Price", linestyle='--', color='red')
    plt.scatter(jim_price.index, jim_price, color='blue')
    plt.xlabel('Number of Days')
    plt.ylabel('Price in NZD')
    plt.title("Jim's Listing Price Trend Compared to Average Price Trend")
    plt.legend()
    plt.grid(True)
    st.pyplot()

# Main function to display Airbnb data and visualizations
def main():
    st.title("Airbnb Data Analytics")

    listings = {
        "Jim":('https://www.airbnb.co.nz/rooms/1125096139567330802', 'jim_airbnb_data.csv'),
        "Alex":('https://www.airbnb.co.nz/rooms/49525122', 'alexa_airbnb_data.csv'),
        "Glenda":('https://www.airbnb.co.nz/rooms/1044551981539410265','glenda_airbnb_data.csv'),
        "Joshua":('https://www.airbnb.co.nz/rooms/566193144075100847','joshua_airbnb_data.csv'), 
        "Prince":('https://www.airbnb.co.nz/rooms/1115473858923244250','prince_airbnb_data.csv'), 
        "Tiffany":('https://www.airbnb.co.nz/rooms/1017748763616316098','tiffany_airbnb_data.csv'), 
        "Michael":('https://www.airbnb.co.nz/rooms/1008128615688965304','michael_airbnb_data.csv'), 
        "Noorani":('https://www.airbnb.co.nz/rooms/698990872569498801','noorani_airbnb_data.csv'), 
        "Andy":('https://www.airbnb.co.nz/rooms/1141075033936083504','andy_airbnb_data.csv'), 
        "Donghong":('https://www.airbnb.co.nz/rooms/31574846','donghong_airbnb_data.csv')  
    }

    for name, (listing_url, filename) in listings.items():
        data = scrape_and_save_data(listing_url, guests=3, num_days=90, filename=filename)
        st.write(f"{name}'s Airbnb Data:")
        st.write(data)

    # Merge Airbnb Data
    st.subheader("Merged Airbnb Data")
    AirbnbData = merge_and_process_data(listings)
    st.write("Merged Airbnb Data:")
    st.write(AirbnbData)

    # Visualizations
    visualize_price_comparison(AirbnbData)
    visualize_average_price_trend(AirbnbData)
    calculate_cosine_similarity(AirbnbData)
    visualize_prices_across_listings(AirbnbData)
    visualize_jim_listing_price_trend(AirbnbData)

if __name__ == "__main__":
    main()

