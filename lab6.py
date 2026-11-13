"""Read a vehicle inventory CSV and display each vehicle's details."""

import csv
from pathlib import Path
from typing import Any


REQUIRED_COLUMNS = (
    "vin",
    "make",
    "model",
    "year",
    "range",
    "topSpeed",
    "zeroSixty",
    "mileage",
)


def load_vehicle_inventory(csv_path: str | Path = "car_fleet.csv") -> list[dict[str, Any]]:
    """Load vehicle rows from CSV, validating the expected columns and values."""
    path = Path(csv_path)
    with path.open("r", newline="", encoding="utf-8-sig") as csv_file:
        reader = csv.DictReader(csv_file)
        if reader.fieldnames is None:
            raise ValueError("The CSV file is empty or has no header row.")

        missing = [column for column in REQUIRED_COLUMNS if column not in reader.fieldnames]
        if missing:
            raise ValueError(f"CSV is missing required columns: {', '.join(missing)}")

        inventory = []
        for row_number, row in enumerate(reader, start=2):
            vehicle = {key: (row.get(key) or "").strip() for key in REQUIRED_COLUMNS}
            if not vehicle["vin"]:
                raise ValueError(f"Row {row_number} has no VIN.")

            try:
                vehicle["year"] = int(vehicle["year"])
                vehicle["range"] = int(vehicle["range"])
                vehicle["topSpeed"] = int(vehicle["topSpeed"])
                vehicle["zeroSixty"] = float(vehicle["zeroSixty"])
                vehicle["mileage"] = int(vehicle["mileage"])
            except ValueError as error:
                raise ValueError(f"Row {row_number} contains an invalid numeric value.") from error

            inventory.append(vehicle)

    return inventory


def main() -> None:
    inventory = load_vehicle_inventory()
    print(f"Loaded {len(inventory)} vehicles.")
    for vehicle in inventory:
        print("\n" + "-" * 32)
        for key, value in vehicle.items():
            print(f"{key}: {value}")


if __name__ == "__main__":
    main()
