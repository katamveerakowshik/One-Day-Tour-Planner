import streamlit as st
import datetime
from Agents.Iternary_Generator_Agent import generate_itinerary
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
        city = st.text_input("📍 City to Visit",
                             help="Enter the city you want to explore")
        date = st.date_input("📅 Trip Date",
                             min_value=datetime.date.today())
        interests = st.multiselect("❤️ Interests",
                                   ["Historical Sites", "Food", "Shopping", "Nature", "Adventure", "Sports"],
                                   help="Select at least 1 interest")
        starting_point = st.text_input("🏨 Starting Location")

    with col2:
        start_time = st.time_input("⏰ Start Time",
                                   datetime.time(9, 0))
        end_time = st.time_input("⏱️ End Time",
                                 datetime.time(21, 0),
                                 help="Must be later than start time")
        budget = st.number_input("💰 Budget (per person) in $")


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
                "budget": budget,
                "starting_point": starting_point
            })


print(user_memory)

if st.session_state.form_submitted:
    st.success("✅ Great choices! Crafting your perfect day...")

    with st.spinner("⚡ Optimizing your itinerary..."):
        itinerary = generate_itinerary(
            user_memory["city"],
            user_memory["start_time"],
            user_memory["end_time"],
            user_memory["interests"],
            user_memory["budget"],
            user_memory["starting_point"]
        )
        print(itinerary)

    st.balloons()
    st.subheader(f"🗓️ Your {date.strftime('%B %d')} Itinerary for {city}")
    st.write(itinerary)




