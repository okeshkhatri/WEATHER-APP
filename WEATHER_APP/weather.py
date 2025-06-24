import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load trained model
w = pickle.load(open(r'WEATHER_APP/weather(logistic).sav', 'rb'))


def predict(input_data):
    input_array = np.asarray(input_data).reshape(1, -1)
    prediction = w.predict(input_array)

    if prediction[0] == 0:
        return 'Rainy'
    elif prediction[0] == 1:
        return 'Cloudy'
    elif prediction[0] == 2:
        return 'Sunny'
    else:
        return 'Snowy'

def main():
    st.title("🌤 Weather Data Prediction App")

    # Numeric inputs
    temperature = st.text_input("Temperature (°C)").strip()
    humidity = st.text_input("Humidity (%)").strip()
    wind_speed = st.text_input("Wind Speed (km/h)").strip()
    precipitation = st.text_input("Precipitation (%)").strip()
    pressure = st.text_input("Atmospheric Pressure (hPa)").strip()
    uv_index = st.text_input("UV Index").strip()
    visibility = st.text_input("Visibility (km)").strip()

    # Category inputs as numeric text
    cloud_cover_val = st.text_input("Cloud Cover (0=Overcast, 1=Partly Cloudy, 2=Clear, 3=Cloudy)").strip()
    season_val = st.text_input("Season (0=Winter, 1=Spring, 2=Autumn, 3=Summer)").strip()
    location_val = st.text_input("Location (0=Inland, 1=Mountain, 2=Coastal)").strip()

    if st.button("Get Weather Prediction"):
        try:
            # Convert to float
            input_list = [
                float(temperature), float(humidity), float(wind_speed), float(precipitation),
                float(pressure), float(uv_index), float(visibility),
                float(season_val), float(location_val), float(cloud_cover_val)
            ]

            # Call the labeled prediction function
            result = predict(input_list)
            st.success(f"✅ Predicted Weather: **{result}**")

        except Exception as e:
            st.error(f"❌ Error: {e}")

if __name__ == '__main__':
    main()
