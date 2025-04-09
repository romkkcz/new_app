import streamlit as st
import matplotlib.pyplot as plt
from io import BytesIO

# Track rectangles in session state
if "rectangles" not in st.session_state:
    st.session_state.rectangles = []

st.set_page_config(layout="wide")
col1, col2 = st.columns([1, 2])

with col1:
    st.header("Rectangle Controls")
    length = st.number_input("Length", min_value=10.0, value=100.0)
    width = st.number_input("Width", min_value=10.0, value=50.0)
    gap = st.number_input("Gap between rectangles", min_value=0.0, value=10.0)

    if st.button("➕ Add Rectangle"):
        count = len(st.session_state.rectangles)
        x = count * (length + gap)
        st.session_state.rectangles.append((x, 0, length, width))  # x, y, w, h

    if st.button("🗑️ Clear All"):
        st.session_state.rectangles = []

with col2:
    st.header("Generated Rectangle Layout")

    fig, ax = plt.subplots(figsize=(10, 3))

    for rect in st.session_state.rectangles:
        x, y, w, h = rect
        ax.add_patch(plt.Rectangle((x, y), w, h, edgecolor='black', facecolor='skyblue'))

    ax.set_xlim(0, max(1, (len(st.session_state.rectangles) + 1) * (length + gap)))
    ax.set_ylim(0, width + 20)
    ax.set_aspect('equal')
    ax.axis('off')

    st.pyplot(fig)

    # Save to PDF
    buf = BytesIO()
    fig.savefig(buf, format="pdf")
    st.download_button("📄 Save to PDF", buf.getvalue(), "rectangles.pdf", mime="application/pdf")
