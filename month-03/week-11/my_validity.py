import geopandas as gpd

# Load polygon layer
roads = gpd.read_file("data/processed/Osogbo_Road_Lines.gpkg")

# Count invalid geometries before fixing
invalid_before = (~roads.geometry.is_valid).sum()

print("Invalid geometries before fixing:", invalid_before)

# Fix invalid geometries
roads["geometry"] = roads.geometry.make_valid()

# Count invalid geometries after fixing
invalid_after = (~roads.geometry.is_valid).sum()

print("Invalid geometries after fixing:", invalid_after)

# Report result
if invalid_before == 0:
    print("No invalid geometries found. All geometries are valid.")
elif invalid_after == 0:
    print("All invalid geometries have been fixed.")
else:
    print("Some invalid geometries remain.")

roads.to_file(
    "data/processed/valid_roads.gpkg",
    driver="GPKG"
)

print("Valid roads layer saved successfully!")