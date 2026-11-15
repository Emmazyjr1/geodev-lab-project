import geopandas as gpd

wards = gpd.read_file("data/processed/wards.gpkg", layer="wards").to_crs(epsg=32631)
facilities = gpd.read_file(
    "data/processed/health_facilities.gpkg", layer="health_facilities").to_crs(epsg=32631)

# buffer
reach = facilities.copy()
reach["geometry"] = facilities.buffer(2000)
print("Buffered", len(reach), "facilities")