import streamlit as st

st.set_page_config(
    page_title="Gurgaon Real Estate Analytics App",
    page_icon="🏠",
)

st.title("Welcome to the Real Estate Data Science Application")
st.markdown("---")
st.markdown("**Introduction:**")
st.markdown("Welcome to our comprehensive Real Estate Data Science Application! In this project, we've combined the power of data science techniques with real-world real estate data to provide you with valuable insights, predictions, and recommendations in the dynamic world of property markets.")
st.image("house-with-garden.jpg", caption='House with Garden', use_column_width=True)
st.markdown("**What to Expect:**")
st.markdown("- **Data Gathering:** We kickstarted our journey by collecting a diverse range of real estate data from various sources, ensuring we have a comprehensive understanding of the market.")
st.markdown("- **Data Cleaning and Merging:** With meticulous care, we cleaned and merged the collected data, ensuring consistency and reliability for our analyses.")
st.markdown("- **Feature Engineering:** Enhancing the richness of our dataset, we engineered new features to provide a detailed representation of properties, including room indicators, possession age, and even a luxury score.")
st.markdown("- **Exploratory Data Analysis (EDA):** Unveiling the hidden patterns within the data, our EDA phase allowed us to understand the market dynamics and trends better.")
st.markdown("- **Model Selection & Productionalization:** Through a rigorous process, we selected the most effective regression model for predicting property prices. This model was then seamlessly integrated into our user-friendly web application using Streamlit, allowing you to effortlessly access its power.")
st.markdown("- **Analytics Module:** Dive deep into key insights about the real estate market with our analytics module, featuring interactive geographical maps, word clouds, scatter plots, and more.")
st.markdown("- **Recommender System:** Tailored to your preferences, our recommender system offers personalized recommendations on facilities, price details, and location advantages, ensuring you find the perfect property.")
st.markdown("- **Deployment on AWS:** For scalability and accessibility, our entire application is deployed on Amazon Web Services (AWS), ensuring you can access it anytime, anywhere.")
st.markdown("---")
st.markdown("**Get Started:**")
st.markdown("Whether you're a home buyer, seller, or just curious about the real estate market, our application is here to empower you with valuable insights and recommendations. Dive in, explore, and make informed decisions with our Real Estate Data Science Application!")
st.markdown("---")
st.markdown("*Disclaimer: The data and insights provided in this application are for informational purposes only and should not be considered as professional financial or real estate advice. Always consult with a qualified expert before making any significant decisions.*")