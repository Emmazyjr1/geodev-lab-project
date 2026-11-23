import geopandas as gpd

# Load polygon layer
roads = gpd.read_file("data/processed/Osogbo_Road_Lines.gpkg")

# Load health facilities point layer
health = gpd.read_file(
    "data/processed/Osogbo_Health_Facilities.gpkg",
    layer="facilities"
)

# Reproject to the same CRS
health = health.to_crs(roads.crs)

# Spatial join
joined = gpd.sjoin(
    health,
    roads,
    how="left",
    predicate="within"
)

# Count health facilities per polygon
counts = (
    joined.groupby("index_right")
    .size()
)

# Attach counts to every polygon
roads["facility_count"] = (
    roads.index.map(counts).fillna(0).astype(int)
)

# Print polygon counts
print(roads[["facility_count"]])

# Total-counted check
print("Total facilities counted:", roads["facility_count"].sum())
print("Total facilities in original layer:", len(health))