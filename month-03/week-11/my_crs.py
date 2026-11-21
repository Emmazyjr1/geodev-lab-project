import geopandas as gpd

# 1. Read roads layer
roads = gpd.read_file("data/processed/Osogbo_Road_Lines.gpkg")

# 2. Print original CRS
print("Original CRS:", roads.crs)

# 3. Estimate the appropriate UTM CRS
estimated_crs = roads.estimate_utm_crs()
print("Estimated UTM CRS:", estimated_crs)

# 4. Reproject roads to the estimated UTM CRS
roads_projected = roads.to_crs(estimated_crs)
print("Reprojected CRS:", roads_projected.crs)

# 5. Calculate road lengths in kilometres
roads_projected["length_km"] = (
    roads_projected.geometry.length / 1000
)

# 6. Print total road length
total_length = roads_projected["length_km"].sum()

print("Total road length (km):", total_length)

# 7. Print first road length
print("First road length (km):",
      roads_projected["length_km"].iloc[0])

# 8. Save processed roads
roads_projected.to_file(
    "data/processed/Osogbo_Road_Lines.gpkg",
    layer="roads",
    driver="GPKG"
)