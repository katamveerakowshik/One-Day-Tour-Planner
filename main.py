import streamlit as st
import datetime
from Agents.Iternary_Generator_Agent import generate_itinerary
from streamlit_folium import st_folium
import folium

user_memory = {}

st.title("🗺️ One-Day Tour Planning Assistant")

# Initialize session state
if "form_submitted" not in st.session_state:
    st.session_state.form_submitted = False

with st.form("tour_form"):
    st.header("✏️ Trip Details")

    # Using columns for better layout
    col1, col2 = st.columns(2)
    with col1:
        city = st.text_input("📍 City to Visit", help="Enter the city you want to explore")
        date = st.date_input("📅 Trip Date", min_value=datetime.date.today())
        interests = st.multiselect(
            "❤️ Interests",
            ["Historical Sites", "Food", "Religion", "Nature", "Adventure", "Sports", "Shopping"],
            help="Select at least 1 interest"
        )

    with col2:
        start_time = st.slider("⏰ Start Time", value=datetime.time(9, 0), format="HH:mm")
        end_time = st.slider("⏱️ End Time", value=datetime.time(21, 0), format="HH:mm")
        starting_point = st.text_input("🏨 Starting Location")

    # Form validation
    if st.form_submit_button("✨ Generate Perfect Itinerary"):
        if not city:
            st.error("Please enter a city to visit")
        elif start_time >= end_time:
            st.error("End time must be after start time")
        elif len(interests) < 1:
            st.error("Please select at least one interest")
        else:
            st.session_state.form_submitted = True
            # Store values in user_memory
            user_memory.update({
                "city": city,
                "date": date,
                "start_time": start_time,
                "end_time": end_time,
                "interests": interests,
                "starting_point": starting_point
            })

if st.session_state.form_submitted:
    st.success("✅ Great choices! Crafting your perfect day...")

    with st.spinner("⚡ Optimizing your itinerary..."):
        itinerary, places_in_city, lat, lon = generate_itinerary(
            user_memory["city"],
            user_memory["date"],
            user_memory["start_time"],
            user_memory["end_time"],
            user_memory["interests"],
            user_memory["starting_point"]
        )

    # Display map with places
    map = folium.Map(location=[lat, lon], zoom_start=13)
    for place in places_in_city:
        folium.Marker([place[2], place[1]], popup=place[0]).add_to(map)
    st_folium(map, width=700, height=500)

    # Display itinerary
    st.balloons()
    st.subheader(f"🗓️ Your {user_memory['date'].strftime('%B %d')} Itinerary for {user_memory['city']}")
    for item in itinerary:
        st.markdown(f"- 🕒 **{item['time']}**: {item['activity']} at {item['location']}")





