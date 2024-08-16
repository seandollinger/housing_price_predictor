import pytest
import pandas as pd
from source.classes.House import House, HouseDataset  # Adjusted import based on your file path

@pytest.fixture
def sample_house():
    return House(1, "Downtown", "Colonial", "Good", 2000, "Gable", "Asphalt", "Concrete", "Gas", "Yes", "Standard", 1, 400, "01/2024")

@pytest.fixture
def sample_data():
    data = {
        'id': [1, 2],
        'neighborhood': ["Downtown", "Suburb"],
        'house_style': ["Colonial", "Ranch"],
        'overall_condition': ["Good", "Fair"],
        'year_built': [2000, 1985],
        'roof_type': ["Gable", "Hip"],
        'roof_material': ["Asphalt", "Wood"],
        'foundation_material': ["Concrete", "Brick"],
        'heating': ["Gas", "Electric"],
        'central_air': ["Yes", "No"],
        'electrical': ["Standard", "Fuse"],
        'fireplace_num': [1, 0],
        'garage_area': [400, 350],
        'date_sold': ["01/2024", "06/2023"]
    }
    return pd.DataFrame(data)

def test_add_house(sample_house):
    dataset = HouseDataset()
    dataset.add_house(sample_house)
    assert dataset.get_house_by_id(1) == sample_house

def test_load_data(sample_data):
    dataset = HouseDataset(sample_data)
    assert len(dataset.houses) == 2

def test_update_house(sample_house):
    dataset = HouseDataset()
    dataset.add_house(sample_house)
    dataset.update_house_by_id(1, {"neighborhood": "Suburb"})
    assert dataset.get_house_by_id(1).neighborhood == "Suburb"

def test_delete_house(sample_house):
    dataset = HouseDataset()
    dataset.add_house(sample_house)
    dataset.delete_house_by_id(1)
    assert dataset.get_house_by_id(1) is None

def test_get_houses_by_filters(sample_data):
    dataset = HouseDataset(sample_data)
    filters = {"neighborhood": "Downtown", "house_style": "Colonial"}
    result = dataset.get_houses_by_filters(filters)
    assert len(result) == 1 and result[0].neighborhood == "Downtown"

