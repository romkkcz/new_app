import streamlit as st
import matplotlib.pyplot as plt
from streamlit_drawable_canvas import st_canvas

st.set_page_config(layout="wide")

# Session state to track rectangles
if "rectangles" not in st.session_state:
    st.session_state.rectangles = []

# Controls
st.sidebar.header("Rectangle Controls")
rect_width = st.sidebar.number_input("Width", value=100)
rect_height = st.sidebar.number_input("Height", value=50)
x_offset = st.sidebar.number_input("X Offset from click", value=10)
y_offset = st.sidebar.number_input("Y Offset from click", value=10)
clear = st.sidebar.button("Clear Rectangles")

if clear:
    st.session_state.rectangles = []

# Canvas for click detection
st.subheader("🖱️ Click on canvas to place a rectangle (with offset)")
canvas_result = st_canvas(
    stroke_width=0,
    stroke_color="#000000",
    background_color="#ffffff",
    height=400,
    width=800,
    drawing_mode="point",  # Just detects clicks
    key="canvas_click",
)

# Check for new point click
if canvas_result.json_data is not None:
    for obj in canvas_result.json_data["objects"]:
        if obj["type"] == "circle":  # Clicks are detected as small circles
            x = obj["left"]
            y = obj["top"]
            new_rect = (x + x_offset, y + y_offset, rect_width, rect_height)
            if new_rect not in st.session_state.rectangles:
                st.session_state.rectangles.append(new_rect)

# Draw rectangles with matplotlib
st.subheader("📐 Rectangle Preview")

fig, ax = plt.subplots(figsize=(10, 5))

for x, y, w, h in st.session_state.rectangles:
    rect = plt.Rectangle((x, y), w, h, edgecolor='blue', facecolor='skyblue')
    ax.add_patch(rect)

ax.set_xlim(0, 800)
ax.set_ylim(400, 0)  # Invert y-axis to match canvas
ax.set_aspect('equal')
ax.axis("off")

st.pyplot(fig)
