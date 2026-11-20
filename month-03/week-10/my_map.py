
import geopandas as gpd
import matplotlib.pyplot as plt

# Load roads
roads = gpd.read_file(
    "data/processed/Osogbo_Road_Lines.gpkg",
    layer="osogbo_road_lines"
)

# Load health facilities
facilities = gpd.read_file(
    "data/processed/Osogbo_Health_Facilities.gpkg",
    layer="facilities"
)

# Ensure both layers have the same CRS
facilities = facilities.to_crs(roads.crs)

# Create map
fig, ax = plt.subplots(figsize=(7, 8))

roads.plot(ax=ax, color="#E6F2F3", linewidth=0.7)

facilities.plot(ax=ax, color="#094923", markersize=18)

ax.set_title("Osogbo Health Facilities Accessibility Map")
ax.set_axis_off()

fig.savefig(
    "month-03/week-10/facilities_map.png",
    dpi=150,
    bbox_inches="tight"
)

print("Map saved")