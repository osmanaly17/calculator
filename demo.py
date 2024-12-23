import streamlit as st

# Title of the app
st.title("Streamlit Calculator")

# Input fields for the two numbers
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Dropdown for selecting the operation
operation = st.selectbox(
    "Select an operation",
    ["Add", "Subtract", "Multiply", "Divide"]
)

# Function to perform the calculation
def calculate(num1, num2, operation):
    if operation == "Add":
        return num1 + num2
    elif operation == "Subtract":
        return num1 - num2
    elif operation == "Multiply":
        return num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Cannot divide by zero"

# Perform the calculation
result = calculate(num1, num2, operation)

# Display the result
st.write(f"Result: {result}")
