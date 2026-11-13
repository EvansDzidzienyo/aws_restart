import csv

import pytest

from lab6 import load_vehicle_inventory


def test_loads_vehicle_inventory_with_numeric_types(tmp_path):
    csv_path = tmp_path / "vehicles.csv"
    csv_path.write_text(
        "vin,make,model,year,range,topSpeed,zeroSixty,mileage\n"
        "ABC123,Example Motors,Sedan,2020,300,150,4.5,12000\n",
        encoding="utf-8",
    )

    vehicles = load_vehicle_inventory(csv_path)

    assert len(vehicles) == 1
    assert vehicles[0]["vin"] == "ABC123"
    assert vehicles[0]["year"] == 2020
    assert vehicles[0]["zeroSixty"] == 4.5
    assert isinstance(vehicles[0]["mileage"], int)


def test_rejects_missing_required_columns(tmp_path):
    csv_path = tmp_path / "vehicles.csv"
    csv_path.write_text("vin,make\nABC123,Example Motors\n", encoding="utf-8")

    with pytest.raises(ValueError, match="missing required columns"):
        load_vehicle_inventory(csv_path)


def test_rejects_invalid_numeric_values(tmp_path):
    csv_path = tmp_path / "vehicles.csv"
    csv_path.write_text(
        "vin,make,model,year,range,topSpeed,zeroSixty,mileage\n"
        "ABC123,Example Motors,Sedan,not-a-year,300,150,4.5,12000\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="invalid numeric value"):
        load_vehicle_inventory(csv_path)
