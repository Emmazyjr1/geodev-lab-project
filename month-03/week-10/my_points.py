import pandas as pd
import geopandas as gpd

# Read CSV file
table = pd.read_csv("data/raw/mydata.csv")

print("Column names:", table.columns.tolist())
print(table.head(3))

# Convert CSV coordinates into spatial points
facilities = gpd.GeoDataFrame(
    table,
    geometry=gpd.points_from_xy(table["center_lon"], table["center_lat"]),
    crs="EPSG:4326", 
)

# Inspect the GeoDataFrame
print(facilities.head(3))
print(facilities.crs)
print("Total facilities:", len(facilities))

# Save as GeoPackage
facilities.to_file("data/processed/Osogbo_Health_Facilities.gpkg", layer="facilities")
print("Saved", len(facilities), "facilities")