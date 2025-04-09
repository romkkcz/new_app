import streamlit as st
import matplotlib.pyplot as plt
from streamlit_drawable_canvas import st_canvas
from io import BytesIO

st.set_page_config(layout="wide")

col1, col2 = st.columns([1, 2])

with col1:
    st.header("Romans App")

    name = st.text_input("Name")
    address = st.text_input("Address")
    length = st.number_input("Length", min_value=1.0)
    width = st.number_input("Width", min_value=1.0)
    gap = st.number_input("Gap between panels", min_value=0.0)
    num_panels = st.slider("Number of panels", 1, 10, 3)

with col2:
    st.header("Free Drawing Area ✏️")
    stroke_color = st.color_picker("Choose drawing color", "#000000")


    # Canvas for freehand drawing
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",  # Optional fill color
        stroke_width=2,
        stroke_color=stroke_color,  # 👈 Use chosen color here
        background_color="#ffffff",
        height=200,
        width=800,
        drawing_mode="freedraw",
        key="canvas"
    )

    st.header("Panel Layout")

    # Draw rectangles
    fig, ax = plt.subplots(figsize=(10, 3))
    for i in range(num_panels):
        x = i * (length + gap)
        rect = plt.Rectangle((x, 0), length, width, edgecolor='blue', facecolor='skyblue')
        ax.add_patch(rect)

    ax.set_xlim(0, num_panels * (length + gap))
    ax.set_ylim(0, width + 20)
    ax.set_aspect('equal')
    ax.axis('off')

    st.pyplot(fig)

    # Save as PDF button
    buf = BytesIO()
    fig.savefig(buf, format="pdf")
    st.download_button("📄 Save Panel Layout as PDF", buf.getvalue(), file_name="panel_layout.pdf", mime="application/pdf")
