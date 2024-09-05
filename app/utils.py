import io
import base64

def plot_to_base64(plot):
    img = io.BytesIO()
    plot.savefig(img, format='png')
    img.seek(0)
    return base64.b64encode(img.getvalue()).decode()