#!/usr/bin/env python3
"""
Simple test runner for the mental wellness prediction app
"""
import subprocess
import sys
from pathlib import Path

def run_tests():
    """Run all tests and display results"""
    print("🧠 Running Mental Wellness Prediction App Tests")
    print("=" * 50)
    
    try:
        # Run pytest with verbose output
        result = subprocess.run([
            sys.executable, "-m", "pytest", "tests/", "-v", "--tb=short"
        ], capture_output=True, text=True)
        
        print(result.stdout)
        
        if result.stderr:
            print("Errors/Warnings:")
            print(result.stderr)
        
        if result.returncode == 0:
            print("✅ All tests passed!")
        else:
            print("❌ Some tests failed!")
            return False
            
    except Exception as e:
        print(f"❌ Error running tests: {e}")
        return False
    
    return True

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
