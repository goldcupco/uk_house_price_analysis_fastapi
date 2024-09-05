from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.data_loader import load_and_preprocess_data
from app.visualizations import create_all_plots
from app.utils import plot_to_base64
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Load data once when the application starts
df = load_and_preprocess_data()
regions = ["Across the UK"] + sorted(df['RegionName'].unique())

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "regions": regions})

@app.get("/region/{region_name}", response_class=HTMLResponse)
async def get_region_data(request: Request, region_name: str):
    try:
        plots = create_all_plots(df, region_name)
        
        # Convert plots to base64-encoded images
        encoded_plots = {key: plot_to_base64(fig) for key, fig in plots.items()}
        
        return templates.TemplateResponse("region.html", {
            "request": request,
            "region_name": region_name,
            "plots": encoded_plots,
            "regions": regions
        })
    except Exception as e:
        logger.error(f"Error in get_region_data endpoint: {str(e)}")
        return HTMLResponse(content=f"<html><body><h1>Error</h1><p>{str(e)}</p></body></html>", status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)