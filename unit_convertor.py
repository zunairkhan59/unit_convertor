import streamlit as st

st.title("🌐 Unit Converter")

option = st.sidebar.selectbox(
    "Select conversion category",
    ("Length", "Weight", "Temperature")
)

def length_converter():
    conversion = st.radio("Choose conversion", ("Kilometers to Miles", "Miles to Kilometers"))
    value = st.number_input("Enter value:")
    if conversion == "Kilometers to Miles":
        result = value * 0.621371
        st.success(f"{value} km = {result:.2f} miles")
    else:
        result = value / 0.621371
        st.success(f"{value} miles = {result:.2f} km")

def weight_converter():
    conversion = st.radio("Choose conversion", ("Kilograms to Pounds", "Pounds to Kilograms"))
    value = st.number_input("Enter value:")
    if conversion == "Kilograms to Pounds":
        result = value * 2.20462
        st.success(f"{value} kg = {result:.2f} lbs")
    else:
        result = value / 2.20462
        st.success(f"{value} lbs = {result:.2f} kg")

def temperature_converter():
    conversion = st.radio("Choose conversion", ("Celsius to Fahrenheit", "Fahrenheit to Celsius"))
    value = st.number_input("Enter temperature:")
    if conversion == "Celsius to Fahrenheit":
        result = (value * 9/5) + 32
        st.success(f"{value}°C = {result:.2f}°F")
    else:
        result = (value - 32) * 5/9
        st.success(f"{value}°F = {result:.2f}°C")

if option == "Length":
    length_converter()
elif option == "Weight":
    weight_converter()
elif option == "Temperature":
    temperature_converter()
