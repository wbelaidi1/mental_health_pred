"""
Simple data validation tests
"""
import pytest
import pandas as pd
import numpy as np
from pathlib import Path

class TestData:
    """Basic data validation tests"""
    
    @pytest.fixture
    def df(self):
        """Load the dataset"""
        data_path = Path(__file__).parent.parent / "data.csv"
        if not data_path.exists():
            pytest.skip("Data file not found")
        return pd.read_csv(data_path)
    
    def test_data_loading(self, df):
        """Test that data loads successfully"""
        assert isinstance(df, pd.DataFrame)
        assert len(df) > 0
    
    def test_required_columns(self, df):
        """Test that required columns exist"""
        required_columns = ['age', 'mental_wellness_index_0_100']
        for col in required_columns:
            assert col in df.columns, f"Missing column: {col}"
    
    def test_wellness_range(self, df):
        """Test that wellness scores are in valid range"""
        wellness_scores = df['mental_wellness_index_0_100']
        assert wellness_scores.min() >= 0
        assert wellness_scores.max() <= 100