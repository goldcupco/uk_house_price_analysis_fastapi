from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.data_loader import load_and_preprocess_data
from app.visualizations import create_all_plots
from app.utils import plot_to_base64
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load data once when the application starts
df = load_and_preprocess_data()
regions = ["Across the UK"] + sorted(df['RegionName'].unique())

@app.get("/regions")
async def get_regions():
    return JSONResponse(content=regions)

@app.get("/region/{region_name}")
async def get_region_data(region_name: str):
    try:
        plots = create_all_plots(df, region_name)
        
        # Convert plots to base64-encoded images
        encoded_plots = {key: plot_to_base64(fig) for key, fig in plots.items()}
        
        return JSONResponse(content={"plots": encoded_plots})
    except Exception as e:
        logger.error(f"Error in get_region_data endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)