from fastapi.testclient import TestClient
from app.main import app
import pytest
import matplotlib
matplotlib.use('Agg')

client = TestClient(app)

def test_get_regions():
    response = client.get("/regions")
    assert response.status_code == 200
    regions = response.json()
    assert isinstance(regions, list)
    assert "Across the UK" in regions

def test_get_region_data_across_uk():
    response = client.get("/region/Across%20the%20UK")
    assert response.status_code == 200
    data = response.json()
    assert "plots" in data
    assert "average_price" in data["plots"]
    assert "cumulative_change" in data["plots"]

def test_get_region_data_specific_region():
    response = client.get("/region/Inner London")
    assert response.status_code == 200
    data = response.json()
    assert "plots" in data
    assert "average_price" in data["plots"]
    assert "cumulative_change" in data["plots"]
    assert "property_type" in data["plots"]
    assert "property_type_change" in data["plots"]

def test_get_region_data_invalid_region():
    response = client.get("/region/InvalidRegion")
    assert response.status_code == 500