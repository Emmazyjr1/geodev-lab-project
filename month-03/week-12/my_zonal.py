import geopandas as gpd
import numpy as np
import rasterio
from rasterio.mask import mask
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

roads_path = PROJECT_ROOT / "data" / "processed" / "Osogbo_Road_Lines.gpkg"
dem_path = PROJECT_ROOT / "data" / "raw" / "my_dem.tif"
ndvi_path = PROJECT_ROOT / "data" / "processed" / "osogbo_ndvi.tif"

# Read your roads line layer
roads = gpd.read_file(roads_path, layer="Osogbo_Road_Lines")

# Reproject to UTM Zone 31N for metre-based buffering
roads = roads.to_crs("EPSG:32631")

# Create 100-metre buffers
roads["geometry"] = roads.geometry.buffer(500)

def calculate_mean(raster_path, geometries):
    results = []

    with rasterio.open(raster_path) as src:
        buffered_roads = geometries.to_crs(src.crs)

        for geom in buffered_roads:
            try:
                cells, _ = mask(
                    src, [geom], crop=True, filled=False
                )

                values = cells[0].compressed()
                values = values[np.isfinite(values)]

                if src.nodata is not None:
                    values = values[values != src.nodata]

                results.append(
                    float(values.mean()) if len(values) else np.nan
                )

            except ValueError:
                results.append(np.nan)

    return results

roads["mean_elevation_m"] = calculate_mean(
    dem_path, roads.geometry
)

roads["mean_ndvi"] = calculate_mean(
    ndvi_path, roads.geometry
)

# Save results
output_path = PROJECT_ROOT / "month-03" / "week-12" / "road_zonal_statistics.csv"

roads.drop(columns="geometry").to_csv(output_path, index=False)

print(roads[["mean_elevation_m", "mean_ndvi"]])
print(f"Results saved to: {output_path}")