import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Project directory
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Input files
roads_path = PROJECT_ROOT /"data" / "processed" / "Osogbo_Road_Lines.gpkg"

csv_path = (
    PROJECT_ROOT / "month-03" / "week-12"
    / "road_zonal_statistics.csv"
)

# Output folder
output_dir = Path(__file__).resolve().parent
output_dir.mkdir(parents=True, exist_ok=True)

# Read road geometries and statistics
roads = gpd.read_file(
    roads_path,
    layer="Osogbo_Road_Lines"
)

stats = pd.read_csv(csv_path)

# Join statistics to road geometries by row order
roads = roads.to_crs("EPSG:32631")
roads["geometry"] = roads.geometry.buffer(500)

if len(roads) != len(stats):
    raise ValueError("Road and statistics row counts do not match.")

roads["mean_ndvi"] = stats["mean_ndvi"]

# Plot NDVI
fig, ax = plt.subplots(figsize=(12, 9))

roads.plot(
    column="mean_ndvi", cmap="RdYlGn", legend=True, ax=ax, linewidth=0,
    missing_kwds={
        "color": "lightgrey",
        "label": "No Data"
    },
    legend_kwds={
        "label": "Mean NDVI",
        "shrink": 0.7
    }
)

ax.set_title(
    "Mean NDVI Along Osogbo Road Buffers", fontsize=14
)

ax.set_axis_off()

plt.tight_layout()

plt.savefig(
    output_dir / "mean_ndvi_map.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("NDVI map saved successfully.")