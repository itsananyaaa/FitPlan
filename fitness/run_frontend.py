"""
Streamlit Frontend App - Standalone Script
Run this to start the Streamlit frontend
Usage: streamlit run app.py
"""

if __name__ == "__main__":
    import subprocess
    import sys
    
    subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"])
