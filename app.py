import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

# ------------------------------
# 🎯 Load trained model and data
# ------------------------------
model = joblib.load("mental_wellness_model.pkl")
df = pd.read_csv("data.csv")  # must contain 'mental_wellness_index_0_100'
wellness_scores = df["mental_wellness_index_0_100"].dropna()

# ------------------------------
# 🛠️ App Configuration
# ------------------------------
st.set_page_config(
    page_title="Mental Wellness Predictor",
    page_icon="🧠",
    layout="wide"
)

st.markdown(
    """
    <style>
        .big-font { font-size:22px !important; }
        .stButton button { 
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
            padding: 0.5em 1em;
            font-weight: bold;
        }
        .stButton button:hover {
            background-color: #45a049;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🧠 Mental Wellness Prediction App")
st.markdown(
    """
    Welcome! This app predicts your **Mental Wellness Index (0–100)**  
    based on lifestyle, work, sleep, and social habits.  
    Use the sliders and inputs below 👇
    """
)

# ------------------------------
# 📥 User Input (modern layout)
# ------------------------------
with st.expander("👤 Lifestyle", expanded=True):
    age = st.slider("Age", 10, 100, 30)
    exercise_minutes_per_week = st.slider("Exercise minutes per week", 0, 1000, 120, step=10)

with st.expander("💻 Work & Screen Time", expanded=True):
    screen_time_hours = st.slider("Total screen time per day (hours)", 0, 24, 6)
    work_screen_hours = st.slider("Work screen time per day (hours)", 0, 24, 5)
    leisure_screen_hours = st.slider("Leisure screen time per day (hours)", 0, 24, 2)
    productivity_0_100 = st.slider("Productivity (0–100)", 0, 100, 70)

with st.expander("😴 Sleep", expanded=True):
    sleep_hours = st.slider("Sleep hours per night", 0, 24, 7)
    sleep_quality_1_5 = st.slider("Sleep quality (1–5)", 1, 5, 3)

with st.expander("🫂 Social & Stress", expanded=True):
    stress_level_0_10 = st.slider("Stress level (0–10)", 0, 10, 5)
    social_hours_per_week = st.slider("Social hours per week", 0, 100, 10)

# Build input DataFrame
input_df = pd.DataFrame([{
    "age": age,
    "screen_time_hours": screen_time_hours,
    "work_screen_hours": work_screen_hours,
    "leisure_screen_hours": leisure_screen_hours,
    "sleep_hours": sleep_hours,
    "sleep_quality_1_5": sleep_quality_1_5,
    "stress_level_0_10": stress_level_0_10,
    "productivity_0_100": productivity_0_100,
    "exercise_minutes_per_week": exercise_minutes_per_week,
    "social_hours_per_week": social_hours_per_week
}])

# ------------------------------
# 🔮 Prediction
# ------------------------------
if st.button("🚀 Predict My Wellness"):
    prediction = model.predict(input_df)[0]
    st.markdown(f"<p class='big-font'>🧾 Predicted Mental Wellness Index: <b>{prediction:.2f} / 100</b></p>", unsafe_allow_html=True)

    # Interpretation
    if prediction < 40:
        st.error("⚠️ This score indicates **low wellness**. Stress management or lifestyle changes may help.")
    elif prediction < 70:
        st.warning("🙂 This score indicates **moderate wellness**. There is room for improvement.")
    else:
        st.balloons()
        st.success("🎉 This score indicates **high wellness**! Keep up the good habits.")

    # ------------------------------
    # 📊 Compare with population
    # ------------------------------
    st.subheader("📊 How do you compare with others?")
    percentile = (wellness_scores < prediction).mean() * 100
    st.markdown(
        f"Your wellness score is **better than {percentile:.1f}% of people** in the dataset."
    )

    # Plot histogram
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.hist(wellness_scores, bins=30, color="#69b3a2", edgecolor="white", alpha=0.8)
    ax.axvline(prediction, color="red", linestyle="--", linewidth=2, label="Your score")
    ax.set_title("Distribution of Mental Wellness Scores")
    ax.set_xlabel("Wellness Index")
    ax.set_ylabel("Number of People")
    ax.legend()
    st.pyplot(fig)

# ------------------------------
# ℹ️ Footer
# ------------------------------
st.markdown("---")
st.caption("Built with ❤️ using Streamlit, scikit-learn and matplotlib")