# QuakeLab - Earthquake Magnitude Prediction from Fault Displacement
QuakeLab is a lightweight web app that allows users to input key fault displacement metrics and predict the corresponding earthquake magnitude using a trained machine learning model. Built with Streamlit and Plotly, this tool offers interactive maps and visualizations using real data from the Southern California Earthquake Center (SCEC).
---

## 🔍 Features

- 🔮 Predict earthquake magnitude based on user-input slip, rupture length, and displacement
- 🗺️ View predictions and historical events on a full-color interactive map
- 📊 See similar past events and how they trend in your region
- 🧠 Powered by scikit-learn regression models trained on SCEC FDHI data

---

## 📚 Research Attribution

This app builds upon data and methodology from the following publication:

Sarmiento A, Madugo D, Shen A, et al.
Database for the Fault Displacement Hazard Initiative Project.
Earthquake Spectra. 2024;0(0). https://doi.org/10.1177/87552930241262766

[Read the paper →](https://journals.sagepub.com/doi/10.1177/87552930241262766)

This project is being conducted under the mentorship of **Dr. Alba Padilla** as part of the SCEC Summer Research Program (NSF REU).

**FDHI seismic data** sourced from the Southern California Earthquake Center (SCEC). Attribution belongs to SCEC and original data authors.

---

## 🚀 How to Run

1. Clone the repo  
2. Install dependencies: `pip install -r requirements.txt`  
3. Run locally: `streamlit run streamlit_app.py`

---

## 📜 License

This project is licensed under the MIT License.  
**FDHI data is used with attribution to SCEC.**

