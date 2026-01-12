import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="Aadhaar Pulse Dashboard", layout="wide")

st.title("📊 Aadhaar Pulse – Stress Intelligence Dashboard")
st.markdown("Decision-support dashboard for UIDAI based on Aadhaar Stress Intelligence")

image_path = "../outputs"

# Sidebar
st.sidebar.header("Select Analysis")
view = st.sidebar.radio(
    "Choose Insight",
    [
        "Future Stress Projection",
        "Demographic Stress (Top 10)",
        "Biometric Stress (Top 10)",
        "Demographic Stress (All States)",
        "Biometric Stress (All States)",
        "Demographic vs Biometric",
        "Stress Share Index",
        "Stress Quadrant"
    ]
)

def show_image(filename, caption):
    file = os.path.join(image_path, filename)
    if os.path.exists(file):
        img = Image.open(file)
        st.image(img, caption=caption, use_column_width=True)
    else:
        st.error(f"❌ Image not found: {filename}")

if view == "Future Stress Projection":
    st.subheader("🔮 Future Aadhaar Stress Risk Projection")
    show_image("future_stress_projection.png",
               "Scenario-based future Aadhaar stress for Uttar Pradesh and Maharashtra")

elif view == "Demographic Stress (Top 10)":
    st.subheader("👥 Demographic Update Stress – Top 10 States")
    show_image("demographic_stress_top10.png",
               "Top states with highest life-event driven Aadhaar update stress")

elif view == "Biometric Stress (Top 10)":
    st.subheader("🧬 Biometric Update Stress – Top 10 States")
    show_image("biometric_stress_top10.png",
               "Top states with highest biometric system load")

elif view == "Demographic Stress (All States)":
    st.subheader("👥 Demographic Update Stress – All States")
    show_image("demographic_stress_all_states.png",
               "Nationwide demographic update stress distribution")

elif view == "Biometric Stress (All States)":
    st.subheader("🧬 Biometric Update Stress – All States")
    show_image("biometric_stress_all_states.png",
               "Nationwide biometric update stress distribution")

elif view == "Demographic vs Biometric":
    st.subheader("⚖ Demographic vs Biometric Stress Comparison")
    show_image("comparison_demographic_vs_biometric.png",
               "Life-event vs system-driven Aadhaar stress")

elif view == "Stress Share Index":
    st.subheader("📊 Aadhaar Stress Share Index")
    show_image("aadhaar_stress_share_index.png",
               "Proportional contribution of demographic and biometric stress")

elif view == "Stress Quadrant":
    st.subheader("🧭 Aadhaar Stress Quadrant Classification")
    show_image("aadhaar_stress_quadrant_bar.png",
               "State classification into Critical, System, Life-Event and Stable regions")

st.markdown("---")
st.markdown("**Aadhaar Stress Intelligence – UIDAI Hackathon Submission**")
st.markdown("This dashboard presents actionable insights derived from Aadhaar enrolment and update behaviour.")
