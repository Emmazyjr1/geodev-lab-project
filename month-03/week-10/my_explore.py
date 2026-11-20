import geopandas as gpd

print(gpd.list_layers("data/processed/Osogbo_Road_Lines.gpkg"))

road = gpd.read_file("data/processed/Osogbo_Road_Lines.gpkg", layer="Osogbo_Road_Lines")

print(road.head())
print("Rows and columns:", road.shape)
print(road.geom_type.value_counts())
print("CRS:", road.crs)
print("Bounds:", road.total_bounds)