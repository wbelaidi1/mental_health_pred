"""
Simple model tests
"""
import pytest
import pandas as pd
import joblib
from pathlib import Path

class TestModel:
    """Basic model tests"""
    
    @pytest.fixture
    def model(self):
        """Load the trained model"""
        model_path = Path(__file__).parent.parent / "mental_wellness_model.pkl"
        if not model_path.exists():
            pytest.skip("Model file not found")
        return joblib.load(model_path)
    
    def test_model_loading(self, model):
        """Test that model loads successfully"""
        assert model is not None
        assert hasattr(model, 'predict')
    
    def test_model_prediction(self, model):
        """Test that model can make predictions"""
        sample_input = pd.DataFrame([{
            "age": 30,
            "screen_time_hours": 8.0,
            "work_screen_hours": 5.0,
            "leisure_screen_hours": 3.0,
            "sleep_hours": 7.0,
            "sleep_quality_1_5": 4,
            "stress_level_0_10": 5,
            "productivity_0_100": 75,
            "exercise_minutes_per_week": 150,
            "social_hours_per_week": 10
        }])
        
        prediction = model.predict(sample_input)[0]
        assert 0 <= prediction <= 100