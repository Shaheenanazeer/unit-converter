import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

# Title of the app
st.title('Unit Converter')

# Define unit options for each category
unit_options = {
    'Length': ['Meters', 'Kilometers', 'Miles', 'Feet', 'Inches', 'Centimeters'],
    'Weight': ['Grams', 'Kilograms', 'Pounds', 'Ounces', 'Stones'],
    'Temperature': ['Celsius', 'Fahrenheit', 'Kelvin']
}

# Dropdowns for unit categories with icons
unit_category = option_menu(
    menu_title="Select Category",
    options=['Length', 'Weight', 'Temperature'],
    icons=['ruler', 'weight', 'thermometer'],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
)

# Dropdowns for selecting units
from_unit = st.selectbox('From', unit_options[unit_category])
to_unit = st.selectbox('To', unit_options[unit_category])

# Input field for value to convert
value = st.number_input('Enter value to convert', min_value=0.0, format='%f')

# Conversion logic
def convert_units(value, from_unit, to_unit):
    if unit_category == 'Length':
        # Length conversion logic
        if from_unit == 'Meters' and to_unit == 'Kilometers':
            return value / 1000
        elif from_unit == 'Kilometers' and to_unit == 'Meters':
            return value * 1000
        elif from_unit == 'Miles' and to_unit == 'Kilometers':
            return value * 1.60934
        elif from_unit == 'Kilometers' and to_unit == 'Miles':
            return value / 1.60934
        # Add more length conversions here
    elif unit_category == 'Weight':
        # Weight conversion logic
        if from_unit == 'Grams' and to_unit == 'Kilograms':
            return value / 1000
        elif from_unit == 'Kilograms' and to_unit == 'Grams':
            return value * 1000
        elif from_unit == 'Pounds' and to_unit == 'Kilograms':
            return value * 0.453592
        elif from_unit == 'Kilograms' and to_unit == 'Pounds':
            return value / 0.453592
        # Add more weight conversions here
    elif unit_category == 'Temperature':
        # Temperature conversion logic
        if from_unit == 'Celsius' and to_unit == 'Fahrenheit':
            return (value * 9/5) + 32
        elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
            return (value - 32) * 5/9
        elif from_unit == 'Celsius' and to_unit == 'Kelvin':
            return value + 273.15
        elif from_unit == 'Kelvin' and to_unit == 'Celsius':
            return value - 273.15
        # Add more temperature conversions here
    return value

# Display conversion result
converted_value = convert_units(value, from_unit, to_unit)
st.write(f'Converted value: {converted_value}')

# Add some styling for better UI
st.markdown("""
    <style>
    .stApp {
        background-color: #d4edda;
        font-family: 'Arial', sans-serif;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        padding: 10px 24px;
        font-size: 16px;
    }
    .stSelectbox, .stNumberInput {
        margin-bottom: 20px;
    }
    .stTitle {
        color: #2e7d32;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)
