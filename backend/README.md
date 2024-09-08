
# UK House Price Analysis

This project provides a web application for analyzing UK house prices using FastAPI and scikit-learn. It generates high-level graphs about house price trends and regional comparisons.

## Setup

1. Clone this repository
2. cd backend
3. Install dependencies: `pip install -r requirements.txt`
4. backend % python3 -m venv venv
backend % source ./venv/bin/activate


5. Place the UK HPI data CSV file in the `data/` folder
6. Run the application: `uvicorn app.main:app --reload`

## Usage

Access the web application by navigating to `http://localhost:8000` in your web browser.

## Testing

Run tests using: `python -m unittest discover tests`

## License

This project is licensed under the MIT License.

## Notes
This structure organizes the code into separate modules for data loading, visualization, and utility functions. The main FastAPI application is in app/main.py. The data is placed in a data/ folder, and tests are provided in the tests/ directory.
To use this structure:
Place your UK HPI data CSV file in the data/ folder.
Implement the missing parts in the visualization functions.
Run the application using uvicorn app.main:app --reload.
Access the web application at http://localhost:8000.
This structure provides a solid foundation for your UK House Price Analysis project, making it easy to maintain, test, and extend in the future.

## Testing 
(venv) williamgroarke@Williams-Mac-mini-5 backend % /Users/williamgroarke/new1/uk_house_price_analysis/backend/venv/bin/python3 -m pytest -v tests/test_main.py
================================================================ test session starts =================================================================
platform darwin -- Python 3.12.5, pytest-8.3.2, pluggy-1.5.0 -- /Users/williamgroarke/new1/uk_house_price_analysis/backend/venv/bin/python3
cachedir: .pytest_cache
rootdir: /Users/williamgroarke/new1/uk_house_price_analysis/backend
configfile: pytest.ini
plugins: anyio-4.4.0
collected 4 items                                                                                                                                    

tests/test_main.py::test_get_regions PASSED                                                                                                    [ 25%]
tests/test_main.py::test_get_region_data_across_uk PASSED                                                                                      [ 50%]
tests/test_main.py::test_get_region_data_specific_region PASSED                                                                                [ 75%]
tests/test_main.py::test_get_region_data_invalid_region PASSED                                                                                 [100%]

================================================================= 4 passed in 2.43s ==================================================================
(venv) williamgroarke@Williams-Mac-mini-5 backend % 
