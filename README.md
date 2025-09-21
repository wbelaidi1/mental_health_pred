# 🧠 Mental Wellness Prediction App

A machine learning-powered web application that predicts mental wellness scores based on lifestyle, work habits, sleep patterns, and social activities. Built with Streamlit and scikit-learn, this app provides personalized wellness insights and population comparisons.

## 🌟 Features

- **Interactive Prediction Interface**: User-friendly sliders and inputs for lifestyle factors
- **Real-time Wellness Scoring**: Predicts mental wellness index (0-100) based on 10 key factors
- **Population Comparison**: Shows how your score compares to others in the dataset
- **Visual Analytics**: Interactive histograms and distribution plots
- **Wellness Interpretation**: Categorized feedback (low, moderate, high wellness)
- **Docker Support**: Easy deployment with containerization

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd mental_health_pred
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:8501`

### Docker Deployment

1. **Build the Docker image**
   ```bash
   docker build -t mental-wellness-app .
   ```

2. **Run the container**
   ```bash
   docker run -p 8501:8501 mental-wellness-app
   ```

3. **Access the app**
   Open `http://localhost:8501` in your browser

## 📊 Model Details

### Features Used for Prediction

The model analyzes 10 key lifestyle factors:

| Feature | Description | Range |
|---------|-------------|-------|
| `age` | User's age | 10-100 years |
| `screen_time_hours` | Total daily screen time | 0-24 hours |
| `work_screen_hours` | Work-related screen time | 0-24 hours |
| `leisure_screen_hours` | Leisure screen time | 0-24 hours |
| `sleep_hours` | Hours of sleep per night | 0-24 hours |
| `sleep_quality_1_5` | Sleep quality rating | 1-5 scale |
| `stress_level_0_10` | Self-reported stress level | 0-10 scale |
| `productivity_0_100` | Productivity rating | 0-100 scale |
| `exercise_minutes_per_week` | Weekly exercise duration | 0-1000 minutes |
| `social_hours_per_week` | Weekly social interaction | 0-100 hours |

### Model Performance

- **Algorithm**: Linear Regression with StandardScaler preprocessing
- **R² Score**: 0.937 (93.7% variance explained)
- **Training Data**: 400+ samples with complete lifestyle profiles

### Key Model Insights

The model reveals important relationships:
- **Sleep quality** has the strongest positive impact (+5.94 coefficient)
- **Stress level** has the strongest negative impact (-10.46 coefficient)
- **Productivity** significantly improves wellness (+4.64 coefficient)
- **Exercise** contributes positively (+1.55 coefficient)
- **Screen time** generally reduces wellness scores

## 🎯 How to Use

1. **Open the app** in your web browser
2. **Adjust the sliders** in each category:
   - 👤 **Lifestyle**: Age and exercise habits
   - 💻 **Work & Screen Time**: Screen usage and productivity
   - 😴 **Sleep**: Sleep duration and quality
   - 🫂 **Social & Stress**: Social interaction and stress levels
3. **Click "🚀 Predict My Wellness"** to get your score
4. **View your results**:
   - Your predicted wellness index (0-100)
   - Wellness category interpretation
   - Population percentile comparison
   - Visual distribution chart

## 📁 Project Structure

```
mental_health_pred/
├── app.py                          # Main Streamlit application
├── data.csv                        # Training dataset
├── mental_wellness_model.pkl       # Trained ML model
├── eda.ipynb                       # Exploratory data analysis
├── requirements.txt                # Python dependencies
├── Dockerfile                      # Docker configuration
├── README.md                       # This file
└── tests/                          # Test suite
    ├── test_data.py               # Data validation tests
    └── test_model.py              # Model validation tests
```

## 🔬 Data Analysis

The project includes comprehensive EDA (`eda.ipynb`) covering:

- **Data Quality**: Missing value analysis and data cleaning
- **Feature Distributions**: Histograms and count plots for all variables
- **Correlation Analysis**: Heatmaps showing feature relationships
- **Model Training**: Pipeline development and evaluation
- **Performance Visualization**: Actual vs predicted scatter plots

## 🧪 Testing

Run the test suite to validate data and model integrity:

```bash
python -m pytest tests/
```

### Test Coverage

- **Data Tests** (`test_data.py`): Validates data quality and structure
- **Model Tests** (`test_model.py`): Ensures model performance and consistency

## 📈 Wellness Score Interpretation

| Score Range | Category | Interpretation |
|-------------|----------|----------------|
| 0-39 | Low Wellness | ⚠️ Stress management or lifestyle changes recommended |
| 40-69 | Moderate Wellness | 🙂 Room for improvement in certain areas |
| 70-100 | High Wellness | 🎉 Excellent habits! Keep up the good work |

## 🛠️ Technical Stack

- **Frontend**: Streamlit
- **Backend**: Python 3.11
- **ML Framework**: scikit-learn
- **Data Processing**: pandas, numpy
- **Visualization**: matplotlib, seaborn
- **Model Persistence**: joblib
- **Containerization**: Docker

## 📋 Requirements

```
pandas
streamlit
matplotlib
scikit-learn
joblib
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Disclaimer

This application is for educational and informational purposes only. The mental wellness predictions are based on statistical patterns in the training data and should not replace professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare professionals for mental health concerns.

## 📞 Support

For questions, issues, or contributions, please open an issue in the repository or contact the development team.

---

**Built with ❤️ for mental wellness awareness**

