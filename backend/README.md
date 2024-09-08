
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
(venv) williamgroarke@Williams-Mac-mini-5 backend % /Users/williamgroarke/new1/uk_house_price_analysis/backend/venv/bin/

python3 -m unittest tests.test_main -v -f


(new_venv) williamgroarke@Williams-Mac-mini-5 backend % python3 -m unittest tests.test_main -v -f
test_get_region_data_across_uk (tests.test_main.TestMain.test_get_region_data_across_uk) ... INFO:app.main:Generating plots for region: Nationwide
INFO:app.visualizations:Data shape: (17424, 54)
INFO:app.visualizations:Columns: ['Date', 'RegionName', 'AreaCode', 'AveragePrice', 'Index', 'IndexSA', '1m%Change', '12m%Change', 'AveragePriceSA', 'SalesVolume', 'DetachedPrice', 'DetachedIndex', 'Detached1m%Change', 'Detached12m%Change', 'SemiDetachedPrice', 'SemiDetachedIndex', 'SemiDetached1m%Change', 'SemiDetached12m%Change', 'TerracedPrice', 'TerracedIndex', 'Terraced1m%Change', 'Terraced12m%Change', 'FlatPrice', 'FlatIndex', 'Flat1m%Change', 'Flat12m%Change', 'CashPrice', 'CashIndex', 'Cash1m%Change', 'Cash12m%Change', 'CashSalesVolume', 'MortgagePrice', 'MortgageIndex', 'Mortgage1m%Change', 'Mortgage12m%Change', 'MortgageSalesVolume', 'FTBPrice', 'FTBIndex', 'FTB1m%Change', 'FTB12m%Change', 'FOOPrice', 'FOOIndex', 'FOO1m%Change', 'FOO12m%Change', 'NewPrice', 'NewIndex', 'New1m%Change', 'New12m%Change', 'NewSalesVolume', 'OldPrice', 'OldIndex', 'Old1m%Change', 'Old12m%Change', 'OldSalesVolume']
INFO:app.visualizations:Data types: Date                       object
RegionName                 object
AreaCode                   object
AveragePrice              float64
Index                     float64
IndexSA                   float64
1m%Change                 float64
12m%Change                float64
AveragePriceSA            float64
SalesVolume               float64
DetachedPrice             float64
DetachedIndex             float64
Detached1m%Change         float64
Detached12m%Change        float64
SemiDetachedPrice         float64
SemiDetachedIndex         float64
SemiDetached1m%Change     float64
SemiDetached12m%Change    float64
TerracedPrice             float64
TerracedIndex             float64
Terraced1m%Change         float64
Terraced12m%Change        float64
FlatPrice                 float64
FlatIndex                 float64
Flat1m%Change             float64
Flat12m%Change            float64
CashPrice                 float64
CashIndex                 float64
Cash1m%Change             float64
Cash12m%Change            float64
CashSalesVolume           float64
MortgagePrice             float64
MortgageIndex             float64
Mortgage1m%Change         float64
Mortgage12m%Change        float64
MortgageSalesVolume       float64
FTBPrice                  float64
FTBIndex                  float64
FTB1m%Change              float64
FTB12m%Change             float64
FOOPrice                  float64
FOOIndex                  float64
FOO1m%Change              float64
FOO12m%Change             float64
NewPrice                  float64
NewIndex                  float64
New1m%Change              float64
New12m%Change             float64
NewSalesVolume            float64
OldPrice                  float64
OldIndex                  float64
Old1m%Change              float64
Old12m%Change             float64
OldSalesVolume            float64
dtype: object
INFO:app.visualizations:Date range: 01/01/1969 to 01/12/2019
INFO:app.visualizations:Data integrity check passed
INFO:app.main:Plots generated successfully. Keys: dict_keys(['plots', 'data'])
INFO:httpx:HTTP Request: GET http://testserver/api/plots/Nationwide "HTTP/1.1 200 OK"
ok
test_get_region_data_invalid_region (tests.test_main.TestMain.test_get_region_data_invalid_region) ... INFO:app.main:Generating plots for region: InvalidRegion
INFO:app.visualizations:Data shape: (17424, 54)
INFO:app.visualizations:Columns: ['Date', 'RegionName', 'AreaCode', 'AveragePrice', 'Index', 'IndexSA', '1m%Change', '12m%Change', 'AveragePriceSA', 'SalesVolume', 'DetachedPrice', 'DetachedIndex', 'Detached1m%Change', 'Detached12m%Change', 'SemiDetachedPrice', 'SemiDetachedIndex', 'SemiDetached1m%Change', 'SemiDetached12m%Change', 'TerracedPrice', 'TerracedIndex', 'Terraced1m%Change', 'Terraced12m%Change', 'FlatPrice', 'FlatIndex', 'Flat1m%Change', 'Flat12m%Change', 'CashPrice', 'CashIndex', 'Cash1m%Change', 'Cash12m%Change', 'CashSalesVolume', 'MortgagePrice', 'MortgageIndex', 'Mortgage1m%Change', 'Mortgage12m%Change', 'MortgageSalesVolume', 'FTBPrice', 'FTBIndex', 'FTB1m%Change', 'FTB12m%Change', 'FOOPrice', 'FOOIndex', 'FOO1m%Change', 'FOO12m%Change', 'NewPrice', 'NewIndex', 'New1m%Change', 'New12m%Change', 'NewSalesVolume', 'OldPrice', 'OldIndex', 'Old1m%Change', 'Old12m%Change', 'OldSalesVolume']
INFO:app.visualizations:Data types: Date                       object
RegionName                 object
AreaCode                   object
AveragePrice              float64
Index                     float64
IndexSA                   float64
1m%Change                 float64
12m%Change                float64
AveragePriceSA            float64
SalesVolume               float64
DetachedPrice             float64
DetachedIndex             float64
Detached1m%Change         float64
Detached12m%Change        float64
SemiDetachedPrice         float64
SemiDetachedIndex         float64
SemiDetached1m%Change     float64
SemiDetached12m%Change    float64
TerracedPrice             float64
TerracedIndex             float64
Terraced1m%Change         float64
Terraced12m%Change        float64
FlatPrice                 float64
FlatIndex                 float64
Flat1m%Change             float64
Flat12m%Change            float64
CashPrice                 float64
CashIndex                 float64
Cash1m%Change             float64
Cash12m%Change            float64
CashSalesVolume           float64
MortgagePrice             float64
MortgageIndex             float64
Mortgage1m%Change         float64
Mortgage12m%Change        float64
MortgageSalesVolume       float64
FTBPrice                  float64
FTBIndex                  float64
FTB1m%Change              float64
FTB12m%Change             float64
FOOPrice                  float64
FOOIndex                  float64
FOO1m%Change              float64
FOO12m%Change             float64
NewPrice                  float64
NewIndex                  float64
New1m%Change              float64
New12m%Change             float64
NewSalesVolume            float64
OldPrice                  float64
OldIndex                  float64
Old1m%Change              float64
Old12m%Change             float64
OldSalesVolume            float64
dtype: object
INFO:app.visualizations:Date range: 01/01/1969 to 01/12/2019
INFO:app.visualizations:Data integrity check passed
ERROR:app.visualizations:Error in create_all_plots for InvalidRegion: single positional indexer is out-of-bounds
ERROR:app.main:Error generating plots for InvalidRegion: single positional indexer is out-of-bounds
INFO:httpx:HTTP Request: GET http://testserver/api/plots/InvalidRegion "HTTP/1.1 500 Internal Server Error"
ok
test_get_region_data_specific_region (tests.test_main.TestMain.test_get_region_data_specific_region) ... INFO:app.main:Generating plots for region: Cambridge
INFO:app.visualizations:Data shape: (17424, 54)
INFO:app.visualizations:Columns: ['Date', 'RegionName', 'AreaCode', 'AveragePrice', 'Index', 'IndexSA', '1m%Change', '12m%Change', 'AveragePriceSA', 'SalesVolume', 'DetachedPrice', 'DetachedIndex', 'Detached1m%Change', 'Detached12m%Change', 'SemiDetachedPrice', 'SemiDetachedIndex', 'SemiDetached1m%Change', 'SemiDetached12m%Change', 'TerracedPrice', 'TerracedIndex', 'Terraced1m%Change', 'Terraced12m%Change', 'FlatPrice', 'FlatIndex', 'Flat1m%Change', 'Flat12m%Change', 'CashPrice', 'CashIndex', 'Cash1m%Change', 'Cash12m%Change', 'CashSalesVolume', 'MortgagePrice', 'MortgageIndex', 'Mortgage1m%Change', 'Mortgage12m%Change', 'MortgageSalesVolume', 'FTBPrice', 'FTBIndex', 'FTB1m%Change', 'FTB12m%Change', 'FOOPrice', 'FOOIndex', 'FOO1m%Change', 'FOO12m%Change', 'NewPrice', 'NewIndex', 'New1m%Change', 'New12m%Change', 'NewSalesVolume', 'OldPrice', 'OldIndex', 'Old1m%Change', 'Old12m%Change', 'OldSalesVolume']
INFO:app.visualizations:Data types: Date                       object
RegionName                 object
AreaCode                   object
AveragePrice              float64
Index                     float64
IndexSA                   float64
1m%Change                 float64
12m%Change                float64
AveragePriceSA            float64
SalesVolume               float64
DetachedPrice             float64
DetachedIndex             float64
Detached1m%Change         float64
Detached12m%Change        float64
SemiDetachedPrice         float64
SemiDetachedIndex         float64
SemiDetached1m%Change     float64
SemiDetached12m%Change    float64
TerracedPrice             float64
TerracedIndex             float64
Terraced1m%Change         float64
Terraced12m%Change        float64
FlatPrice                 float64
FlatIndex                 float64
Flat1m%Change             float64
Flat12m%Change            float64
CashPrice                 float64
CashIndex                 float64
Cash1m%Change             float64
Cash12m%Change            float64
CashSalesVolume           float64
MortgagePrice             float64
MortgageIndex             float64
Mortgage1m%Change         float64
Mortgage12m%Change        float64
MortgageSalesVolume       float64
FTBPrice                  float64
FTBIndex                  float64
FTB1m%Change              float64
FTB12m%Change             float64
FOOPrice                  float64
FOOIndex                  float64
FOO1m%Change              float64
FOO12m%Change             float64
NewPrice                  float64
NewIndex                  float64
New1m%Change              float64
New12m%Change             float64
NewSalesVolume            float64
OldPrice                  float64
OldIndex                  float64
Old1m%Change              float64
Old12m%Change             float64
OldSalesVolume            float64
dtype: object
INFO:app.visualizations:Date range: 01/01/1969 to 01/12/2019
INFO:app.visualizations:Data integrity check passed
INFO:app.main:Plots generated successfully. Keys: dict_keys(['plots', 'data'])
INFO:httpx:HTTP Request: GET http://testserver/api/plots/Cambridge "HTTP/1.1 200 OK"
ok
test_get_regions (tests.test_main.TestMain.test_get_regions) ... INFO:httpx:HTTP Request: GET http://testserver/api/regions "HTTP/1.1 200 OK"
ok

----------------------------------------------------------------------
Ran 4 tests in 2.696s

OK
