import streamlit as st
from datetime import datetime
from streamlit_extras.colored_header import colored_header  
from streamlit_lottie import st_lottie  
import requests
from flow_import import GPT_insight

# Function to fetch Lottie animations
def load_lottie_url(url: str):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

# Load Lottie animation
lottie_stars = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_9uyf77v8.json")

# Main app function
def main():
    # Set background color and font
    st.markdown(
        """
        <style>
        body {
            background-color: #121212;
            color: #FFD700;
            font-family: 'Comic Sans MS', cursive;
        }
        .stTextInput > div > div > input {
            color: white;
            background-color: #333;
        }
        .stSelectbox > div > div > select {
            color: white;
            background-color: #333;
        }
        .stDateInput input, .stTimeInput input {
            color: white;
            background-color: #333;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Lottie animation at the top
    if lottie_stars:
        st_lottie(lottie_stars, height=200, key="stars")

    # Add a header with a colorful gradient
    colored_header(
        label="🌌 SoulBuddy🌌",
        description="AI-Powered Spiritual Guide",
        color_name="orange-70"
    )

    # Input fields
    name = st.text_input("🌟 Enter your name:")

    # Date input with cosmic vibes
    date = st.date_input(
        "📅 Enter your date YY/MM/DD"
    )

    # Time input with cosmic vibes
    time = st.time_input("⏳ Enter your birth time:")

    gender = st.selectbox(
        "👤 Select your gender:",
        ("Male", "Female", "Other", "Prefer not to say")
    )

    place_of_birth = st.text_input("🌍 Enter your place of birth:")

    context = """\
    The date is 01-01-2006. Mercury's RA is 17.68, its Dec is -23.53, and its distance is 1.33117 AU. Venus' RA is 20.12, its Dec is -17.84, and its
    distance is 0.28794 AU. Mars' RA is 2.54, its Dec is 16.59, and its distance is 0.7752 AU. Jupiter's barycenter RA is 14.74, its Dec is -14.76, and
    its distance is 5.9107 AU. Saturn's barycenter RA is 8.83, its Dec is 18.39, and its distance is 8.23831 AU. Uranus' barycenter RA is 22.64, its Dec
    is -9.4, and its distance is 20.58887 AU. Neptune's barycenter RA is 21.23, its Dec is -16.22, and its distance is 30.85266 AU. Pluto's barycenter
    RA is 17.64, its Dec is -15.88, and its distance is 31.99032 AU.
    """
    
    if st.button("✨ Submit Your Details ✨"):
        st.balloons()
        try:
            atro_insight = GPT_insight(name=name, dob=date, location=place_of_birth, context=context)
            st.write("SoulBuddy Insights", atro_insight)
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
