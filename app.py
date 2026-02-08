import streamlit as st
import requests

# -----------------------------
# Road Accident Prediction Page
# -----------------------------
def road_accident_prediction():
    st.title(" Road Accident Risk Prediction")

    st.subheader("Enter Road Conditions")


    # Boolean fields
    public_road = st.selectbox("Public Road", [True, False])
    road_signs_present = st.selectbox("Road Signs Present", [True, False])
    holiday = st.selectbox("Holiday", [True, False])
    school_season = st.selectbox("School Season", [True, False])

    # Categorical fields (must match dataset)
    lighting = st.selectbox("Lighting Condition", ["daylight", "dim", "night"])
    weather = st.selectbox("Weather", ["rainy", "clear", "foggy"])
    road_type = st.selectbox("Road Type", ["rural", "urban", "highway"])
    time_of_day = st.selectbox("Time of Day", ["morning", "afternoon", "evening"])

    # Numerical fields
    num_reported_accidents = st.number_input("Reported Accidents in Area", min_value=0, max_value=10, step=1)
    num_lanes = st.number_input("Number of Lanes", min_value=1, max_value=10, step=1)
    curvature = st.number_input("Road Curvature", min_value=0.00, max_value=1.00, step=0.01, format="%.2f")
    speed_limit = st.number_input("Speed Limit (km/h)", min_value=0, max_value=200, step=5, format="%.2f")

    # Call FastAPI
    def predict():
        url = "http://127.0.0.1:8000/predict"
        data = {
            "public_road": public_road,
            "road_signs_present": road_signs_present,
            "lighting": lighting,
            "weather": weather,
            "road_type": road_type,
            "time_of_day": time_of_day,
            "holiday": holiday,
            "school_season": school_season,
            "num_reported_accidents": num_reported_accidents,
            "num_lanes": num_lanes,
            "curvature": curvature,
            "speed_limit": speed_limit
        }

        try:
            response = requests.post(url, json=data)
            result = response.json()
            return result
        except:
            st.error("❌ FastAPI server not running!")

    if st.button("Predict Accident Risk"):
        result = predict()
        if result:
            st.success(f"Risk Level: {result['risk_level']}")
            st.info(f"Risk Score: {round(result['accident_risk_score'], 3)}")


# -----------------------------
# Home Page
# -----------------------------
def home():
    st.title("🚦 Road Accident Risk Prediction System")
    image_path = "road.jpg"  # Update this to your image path if necessary
    st.image(image_path, caption=" Road Accidents Risks")

    st.markdown("""
    This system predicts the **risk of road accidents** based on road, weather and traffic conditions.

    ### How it works
    1. Enter road and traffic conditions
    2. Click Predict
    3. Get risk level (Low, Medium or High)

    Powered by Machine Learning & FastAPI
    """)


# About Page
# -----------------------------
def about():
    st.title("About This Project")
    image_path = "Road1.jpg"  # Update this to your image path if necessary
    st.image(image_path, caption="Road Accidents Risks")

    st.write("""
    This project is an **Intelligent Road Accident Risk Prediction System** developed using
    **Machine Learning, Python, and Streamlit**.The goal of this system is to **analyze road conditions and environmental factors**
    to predict the **risk of road accidents**, helping drivers, authorities, and city planners
    take preventive measures.
    """)

    st.subheader("Dataset Overview")
    st.write("""
    The system was trained using historical road accident data. Each record in the dataset contains information about road characteristics, traffic, weather, and accident history.

    **Key Features in the Dataset:**
    - **road_type:** Type of road (rural, urban, highway)
    - **num_lanes:** Number of lanes on the road
    - **curvature:** Road curvature (0 = straight, 1 = very curvy)
    - **speed_limit:** Speed limit of the road (km/h)
    - **lighting:** Lighting condition (daylight, dim, night)
    - **weather:** Weather condition (rainy, clear, foggy)
    - **road_signs_present:** Whether road signs are present (True / False)
    - **public_road:** Whether the road is public (True / False)
    - **time_of_day:** Time when the data was recorded (morning, afternoon, evening)
    - **holiday:** Whether it was a holiday (True / False)
    - **school_season:** Whether it was school season (True / False)
    - **num_reported_accidents:** Number of reported accidents in the area
    - **accident_risk:** Target variable representing accident risk score (0 to 1)
    """)

    st.subheader("How the System Works")
    st.write("""
    1. The user enters road and environmental details in the input form.
    2. Inputs are preprocessed and converted into numerical form suitable for the model.
    3. The trained machine learning model predicts a **risk score**.
    4. The risk score is classified into categories:
       - **Low Risk** (score < 0.3)
       - **Medium Risk** (0.3 ≤ score < 0.6)
       - **High Risk** (score ≥ 0.6)
    """)

    st.subheader("Purpose of the System")
    st.write("""
    This system aims to:
    - Increase road safety awareness
    - Help city planners identify high-risk areas
    - Reduce accident rates through preventive measures
    - Support data-driven traffic management
    """)

    st.subheader("Technologies Used")
    st.write("""
    - **Python** for data processing and modeling  
    - **Scikit-Learn / CatBoost** for machine learning  
    - **FastAPI** for backend API services  
    - **Streamlit** for the user interface  
    - **Pandas & Joblib** for data handling and model storage
    """)

    st.subheader("Target Users")
    st.write("""
    - Road safety authorities and planners  
    - Traffic management professionals  
    - Drivers seeking real-time risk assessment  
    - Research and educational purposes
    """)

    st.subheader("Future Improvements")
    st.write("""
    - Integrate **real-time traffic and weather data** for dynamic predictions  
    - Add **visual risk maps** for city planners  
    - Use **more advanced models** (e.g., Deep Learning) to improve accuracy  
    - Expand dataset with data from multiple regions for better generalization
    """)


# -----------------------------
# Sidebar Navigation
# -----------------------------
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a page", ["Home", "About", "Road Accident Prediction"])

if page == "Home":
    home()
elif page == "About":
    about()
elif page == "Road Accident Prediction":
    road_accident_prediction()


# streamlit run app.py