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

This app builds upon findings from:

**"A Reexamination of Scaling Relationships for Earthquake Source Parameters With a Consideration of Potential Biases"**  
K. R. Felzer, E. E. Brodsky, and J. R. Kanamori (2024)  
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

