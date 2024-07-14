import streamlit as st
from add import add
from sub import subtract
from mult import multiply
from div import divide

# Title of the app
st.title("Simple Calculator")

# Input fields
num1 = st.number_input("Enter the 1st :blue[Number]", format="%.2f")
num2 = st.number_input("Enter the 2nd :blue[Number]", format="%.2f")

# Dropdown for selecting the operation
operation = st.selectbox("Select an :red[Operation]", ("Addition", "Subtraction", "Multiplication", "Division"))

# Perform the calculation
if st.button("Calculate"):
    if operation == "Addition":
        result = add(num1, num2)
    elif operation == "Subtraction":
        result = subtract(num1, num2)
    elif operation == "Multiplication":
        result = multiply(num1, num2)
    elif operation == "Division":
        result = divide(num1, num2)

    st.write(f"The :green[Result] is: {result}")

# Option to quit the calculator (not applicable in Streamlit, can refresh the page instead)
if st.button("Reset"):
    st.experimental_rerun()
