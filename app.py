import streamlit as st
from inference_engine import recommend_laptop

st.title("Student Laptop Recommendation Expert System")

processing = st.slider(
    "Processing Power Requirement",
    1, 5
)

graphics = st.slider(
    "Graphics Performance Requirement",
    1, 5
)

portability = st.slider(
    "Portability Priority",
    1, 5
)

budget = st.selectbox(
    "Budget Category",
    ["Low", "Medium", "Medium-High", "High"]
)

if st.button("Generate Recommendation"):

    recommendations, reasons = recommend_laptop(
        processing,
        graphics,
        portability,
        budget
    )

    st.header("Recommended Laptops")

    for laptop in recommendations:
        st.subheader(laptop["name"])
        st.write(f"CPU: {laptop['cpu']}")
        st.write(f"GPU: {laptop['gpu']}")
        st.write(f"RAM: {laptop['ram']} GB")

    st.header("Reasoning")

    for reason in reasons:
        st.write("- " + reason)