# One-Day Tour Planner

The **One-Day Tour Planner** is an intelligent application designed to create personalized one-day travel itineraries. It leverages multiple APIs and advanced AI models for itinerary generation, weather updates, local attractions, and news highlights. The app is built using **Streamlit** for the frontend and integrates the **DeepSeekr1:1.5b** model for itinerary creation.

## Features
- **Itinerary Generation**: Powered by the DeepSeekr1:1.5b model, which uses real-time data to craft customized travel plans.
- **Weather Updates**: Fetches accurate weather information from OpenWeather API.
- **Explore Local Attractions**: Retrieves details of nearby places using Geoapify API.
- **News Highlights**: Provides relevant news updates from NewsAPI.org.

## How It Works
1. The app collects data such as weather conditions, local attractions, and news.
2. The DeepSeekr model processes this data to generate a tailored one-day itinerary.
3. Results are displayed in an interactive and user-friendly interface powered by Streamlit.

## Installation Guide
Follow these steps to set up the application on your local machine:

### 1. Clone the Repository
git clone https://github.com/katamveerakowshik/One-Day-Tour-Planner.git

### 2. Install Dependencies
Ensure that Python and pip are installed on your system. Then, navigate to the project directory and install all required packages:
pip install -r requirements.txt

### 3. Run the Application
Launch the app using Streamlit with the following command:
streamlit run main.py

## Requirements
- Python 3.x
- Internet connection for fetching API data

## APIs Used
- **OpenWeather API**: For real-time weather updates.
- **Geoapify API**: For discovering nearby places and attractions.
- **NewsAPI.org**: For fetching relevant news updates.

This application combines cutting-edge technology with real-time data to provide an efficient and enjoyable travel planning experience!

