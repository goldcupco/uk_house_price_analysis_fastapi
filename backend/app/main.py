from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.visualizations import create_all_plots
from .data_loader import load_data  # Import the load_data function as requested
import io
import base64
import matplotlib.pyplot as plt
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the DataFrame once when the application starts
df = load_data()  # Use the imported load_data function

@app.get("/")
async def root():
    return {"message": "Welcome to the UK House Price Analysis API"}

@app.get("/api/regions")
async def get_regions():
    regions = df['RegionName'].unique().tolist()
    return {"regions": regions}

@app.get("/api/plots/{region}")
async def get_plots(region: str):
    try:
        logger.info(f"Generating plots for region: {region}")
        plots = create_all_plots(df, region)  # Assuming df is your DataFrame
        logger.info(f"Plots generated successfully. Keys: {plots.keys()}")
        return plots
    except Exception as e:
        logger.error(f"Error generating plots for {region}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error generating plots: {str(e)}")
    """
@app.get("/api/plots/{region_name}")
async def get_plots(region_name: str):
    try:
        plots_and_data = create_all_plots(df, region_name)
        response_data = {}
        for plot_name, content in plots_and_data.items():
            buf = io.BytesIO()
            content['plot'].savefig(buf, format='png')
            buf.seek(0)
            response_data[plot_name] = {
                'image': base64.b64encode(buf.getvalue()).decode('utf-8'),
                'data': content['data']
            }
            plt.close(content['plot'])
        return response_data
    except Exception as e:
        logger.error(f"Error generating plots for {region_name}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error generating plots: {str(e)}")
# Add other routes and functionality as needed
"""