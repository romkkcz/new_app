import streamlit as st
import matplotlib.pyplot as plt
from streamlit_drawable_canvas import st_canvas

st.set_page_config(layout="wide")

# Initialize rectangle list
if "rectangles" not in st.session_state:
    st.session_state.rectangles = []

# Controls
st.sidebar.header("Rectangle Settings")
rect_width = st.sidebar.number_input("Width", value=100)
rect_height = st.sidebar.number_input("Height", value=50)
x_gap = st.sidebar.number_input("X Offset from previous", value=10)
y_gap = st.sidebar.number_input("Y Offset from previous", value=0)
clear = st.sidebar.button("Clear Rectangles")

if clear:
    st.session_state.rectangles = []

# Canvas (just to detect clicks)
st.subheader("Click anywhere to trigger new rectangle")
canvas_result = st_canvas(
    stroke_width=0,
    stroke_color="#000000",
    background_color="#ffffff",
    height=400,
    width=800,
    drawing_mode="point",
    key="canvas_trigger"
)

# Detect click (used just to trigger rectangle placement)
if canvas_result.json_data is not None:
    clicked = len(canvas_result.json_data["objects"])
    if "last_click_count" not in st.session_state:
        st.session_state.last_click_count = 0

    if clicked > st.session_state.last_click_count:
        # Determine new rectangle position
        if st.session_state.rectangles:
            last_x, last_y, _, _ = st.session_state.rectangles[-1]
            new_x = last_x + rect_width + x_gap
            new_y = last_y + y_gap
        else:
            new_x, new_y = 0, 0

        # Add rectangle
        st.session_state.rectangles.append((new_x, new_y, rect_width, rect_height))
        st.session_state.last_click_count = clicked

# Draw rectangles
st.subheader("📐 Rectangle Layout")
fig, ax = plt.subplots(figsize=(10, 5))

for x, y, w, h in st.session_state.rectangles:
    rect = plt.Rectangle((x, y), w, h, edgecolor='black', facecolor='skyblue')
    ax.add_patch(rect)

ax.set_xlim(0, 1000)
ax.set_ylim(400, 0)  # Invert y-axis to match canvas
ax.set_aspect("equal")
ax.axis("off")

st.pyplot(fig)
