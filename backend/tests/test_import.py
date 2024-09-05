import sys
import os

def test_import():
    print("Python executable:", sys.executable)
    print("sys.path:", sys.path)
    print("Current working directory:", os.getcwd())
    print("Contents of site-packages:")
    site_packages = [p for p in sys.path if 'site-packages' in p][0]
    print(os.listdir(site_packages))
    import fastapi
    print("FastAPI imported successfully")
    print("FastAPI location:", fastapi.__file__)