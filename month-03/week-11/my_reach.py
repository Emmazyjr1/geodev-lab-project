import geopandas as gpd

# Load datasets
roads = gpd.read_file("data/processed/Osogbo_Road_Lines.gpkg")

health = gpd.read_file(
    "data/processed/Osogbo_Health_Facilities.gpkg",
    layer="facilities"
)

# Reproject both layers to UTM Zone 31N
roads = roads.to_crs("EPSG:32631")
health = health.to_crs("EPSG:32631")

# Find nearest health facility
nearest = gpd.sjoin_nearest(
    roads,
    health,
    how="left",
    distance_col="distance_m"
)

# Convert distance to kilometres
nearest["distance_km"] = nearest["distance_m"] / 1000

# Print results
print(nearest[["distance_m", "distance_km"]])

# Summary statistics
print("Minimum distance (km):", nearest["distance_km"].min())
print("Maximum distance (km):", nearest["distance_km"].max())
print("Average distance (km):", nearest["distance_km"].mean())

# Save result
nearest.to_file(
    "data/processed/nearest_health_facility.gpkg",
    driver="GPKG"
)