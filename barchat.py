import streamlit as st
import pandas as pd
import altair as alt

# Title of the app
st.title("Simple Bar Chart Creator")

# Input section for data
st.header("Enter Your Data")

# Input number of bars
num_bars = st.number_input("Number of bars", min_value=1, max_value=10, value=3)

# Input for bar labels and values
labels = []
values = []
for i in range(int(num_bars)):
    label = st.text_input(f"Label for bar {i + 1}", value=f"Label {i + 1}")
    value = st.number_input(f"Value for bar {i + 1}", value=1)
    labels.append(label)
    values.append(value)

# Create a DataFrame
data = pd.DataFrame({
    'Label': labels,
    'Value': values
})

# Display the DataFrame
st.subheader("Data Table")
st.write(data)

# Create the bar chart
st.subheader("Bar Chart")
chart = alt.Chart(data).mark_bar().encode(
    x='Label',
    y='Value'
).properties(width=600)

st.altair_chart(chart)
