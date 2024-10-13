import streamlit as st
import pickle

# Streamlit UI
st.title('Mobile Price Range Prediction')

# Input fields
battery_power = st.text_input('Battery Power')
blue = st.text_input('Bluetooth (0 or 1)')
clock_speed = st.text_input('Clock Speed (GHz)')
dual_sim = st.text_input('Dual SIM (0 or 1)')
int_memory = st.text_input('Internal Memory (GB)')
mobile_wt = st.text_input('Mobile Weight (g)')
ram = st.text_input('RAM (GB)')
talk_time = st.text_input('Talk Time (hours)')
touch_screen = st.text_input('Touch Screen (0 or 1)')
wifi = st.text_input('WiFi (0 or 1)')

# Prediction button
if st.button('Predict'):
    try:
        # Load the trained model
        with open('model.pkl', 'rb') as f:
            model = pickle.load(f)

        # Convert input values to appropriate data types
        battery_power = float(battery_power)
        blue = int(blue)
        clock_speed = float(clock_speed)
        dual_sim = int(dual_sim)
        int_memory = float(int_memory)
        mobile_wt = float(mobile_wt)
        ram = float(ram)
        talk_time = float(talk_time)
        touch_screen = int(touch_screen)
        wifi = int(wifi)

        # Make prediction
        data = [[battery_power, blue, clock_speed, dual_sim, int_memory, mobile_wt, ram, talk_time, touch_screen, wifi]]
        result = model.predict(data)[0]

        # Display result
        if result <= 1:
            st.success('Price Range: Low')
        
        elif result == 2:
            st.success('Price Range: Medium')
        elif result == 3:
            st.success('Price Range: High')
        else:
            st.error('Invalid prediction')
    except ValueError:
        st.error('Please enter valid numeric values for all inputs.')
