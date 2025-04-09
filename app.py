import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

# Create two columns: input (left) and output (right)
col1, col2 = st.columns([1, 2])

with col1:
    st.header("Panel Input")
    
    name = st.text_input("Name")
    address = st.text_input("Address")
    length = st.number_input("Length (e.g. 100)", min_value=1.0)
    width = st.number_input("Width (e.g. 50)", min_value=1.0)
    gap = st.number_input("Gap between panels (e.g. 10)", min_value=0.0)

    num_panels = st.slider("Number of panels", min_value=1, max_value=10, value=3)

with col2:
    st.header("Panel Layout")

    fig, ax = plt.subplots(figsize=(10, 4))
    
    for i in range(num_panels):
        x = i * (length + gap)
        y = 0
        rect = plt.Rectangle((x, y), length, width, edgecolor='blue', facecolor='skyblue')
        ax.add_patch(rect)

    ax.set_xlim(0, num_panels * (length + gap))
    ax.set_ylim(0, width + 20)
    ax.set_aspect('equal')
    ax.axis('off')

    st.pyplot(fig)
