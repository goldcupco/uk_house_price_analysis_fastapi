from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.data_loader import load_and_preprocess_data
from app.visualizations import create_hpi_trend_plot, create_regional_comparison_plot, create_year_on_year_change_plot
from app.utils import plot_to_base64

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    df = load_and_preprocess_data()
    
    # Generate plots
    hpi_trend = create_hpi_trend_plot(df)
    regional_comparison = create_regional_comparison_plot(df)
    yoy_change = create_year_on_year_change_plot(df)
    
    # Convert plots to base64-encoded images
    encoded_plots = [plot_to_base64(plot) for plot in [hpi_trend, regional_comparison, yoy_change]]
    
    # Generate HTML with embedded images
    html_content = f"""
    <html>
        <body>
            <h1>UK House Price Analysis</h1>
            <img src="data:image/png;base64,{encoded_plots[0]}">
            <img src="data:image/png;base64,{encoded_plots[1]}">
            <img src="data:image/png;base64,{encoded_plots[2]}">
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)