import pandas as pd
import geopandas as gpd

# Load health facilities
facilities = gpd.read_file(
    "data/processed/Osogbo_Health_Facilities.gpkg",
    layer="facilities"
)

# Load road network
roads = gpd.read_file(
    "data/processed/Osogbo_Road_Lines.gpkg",
    layer="osogbo_road_lines"
)

# Inspect health facilities
print("Health Facilities")
print(facilities.head())
print("Total facilities:", len(facilities))
print("CRS:", facilities.crs)

# Inspect roads
print("\nRoad Network")
print(roads.head())
print("Total road features:", len(roads))
print("CRS:", roads.crs)

# Reproject both datasets for metric analysis
facilities = facilities.to_crs(epsg=32631)
roads = roads.to_crs(epsg=32631)

# Calculate road lengths
roads["length_km"] = roads.geometry.length / 1000

print("\nTotal road length (km):", roads["length_km"].sum())

# Calculate nearest road distance for each facility
nearest_roads = gpd.sjoin_nearest(
    facilities,
    roads[["geometry"]],
    how="left",
    distance_col="distance_to_road_m"
)

print("\nFacility proximity to roads:")
print(nearest_roads[["distance_to_road_m"]].head())

# Save results
nearest_roads.to_file(
    "data/processed/Osogbo_Facility_Road_Accessibility.gpkg",
    layer="facility_accessibility",
    driver="GPKG"
)

print("\nAccessibility analysis completed!")