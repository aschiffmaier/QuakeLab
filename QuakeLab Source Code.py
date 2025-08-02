# streamlit_app.py

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px

# ---- Load Data ----
@st.cache_data
def load_data():
    return pd.read_csv("fdhi_groups1_25.csv")

df = load_data()

# ---- Load Trained Model ----
@st.cache_resource
def load_model():
    return joblib.load("your_model.pkl")  # <-- Replace with your actual filename

model = load_model()

# ---- Sidebar: User Input ----
st.sidebar.header("🧠 Enter Fault Parameters")
slip = st.sidebar.slider("Max Slip (m)", 0.0, 10.0, 2.5)
rupture_length = st.sidebar.slider("Rupture Length (km)", 0.0, 300.0, 75.0)

# ---- Predict Magnitude ----
user_input = np.array([[slip, rupture_length]])
predicted_mag = model.predict(user_input)[0]

st.sidebar.markdown(f"### 🔮 Predicted Magnitude: `{predicted_mag:.2f}`")

# ---- Add User Point to Map ----
user_point = pd.DataFrame({
    "lat": [34.5],  # <-- optional static location or user input
    "lon": [-117.0],
    "predicted_mag": [predicted_mag],
    "event_id": ["User Prediction"],
    "frame_id": [1]
})
df["frame_id"] = 0
plot_df = pd.concat([df, user_point], ignore_index=True)

# ---- Plot Map ----
st.title("🌍 QuakeLab: Earthquake Magnitude Predictor")

fig = px.scatter_geo(
    plot_df,
    lat="lat",
    lon="lon",
    color="predicted_mag",
    size="predicted_mag",
    hover_name="event_id",
    color_continuous_scale="Inferno",
    size_max=20,
    animation_frame="frame_id"
)

fig.update_geos(
    projection_type="natural earth",
    showland=True,
    landcolor="rgb(10,10,10)",
    bgcolor="black"
)

fig.update_layout(
    geo_bgcolor="black",
    paper_bgcolor="black",
    plot_bgcolor="black",
    font_color="white",
    title="Predicted vs Historical Seismic Events",
    margin={"r":0,"t":30,"l":0,"b":0}
)

st.plotly_chart(fig, use_container_width=True)
