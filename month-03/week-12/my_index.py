
import rasterio
import numpy as np
from pathlib import Path

# Locate project root
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Landsat 8 band paths
landsat_folder = PROJECT_ROOT / "data" / "raw" / "landsat"

red_path = landsat_folder / "LC08_L2SP_190055_20250331_20250411_02_T1_SR_B4.TIF"
nir_path = landsat_folder / "LC08_L2SP_190055_20250331_20250411_02_T1_SR_B5.TIF"

# Check files
print("Band 4 exists:", red_path.exists())
print("Band 5 exists:", nir_path.exists())

# Read Red band
with rasterio.open(red_path) as src:
    red = src.read(1, masked=True).astype("float32")
    profile = src.profile.copy()

# Read NIR band
with rasterio.open(nir_path) as src:
    nir = src.read(1, masked=True).astype("float32")

# Apply Landsat Collection 2 scale factor and offset
red = red * 0.0000275 - 0.2
nir = nir * 0.0000275 - 0.2

# Calculate NDVI
denominator = nir + red

valid = (
    ~np.ma.getmaskarray(red)
    & ~np.ma.getmaskarray(nir)
    & (denominator.data != 0)
)

ndvi = np.full(red.shape, np.nan, dtype="float32")

ndvi[valid] = (
    (nir.data[valid] - red.data[valid])
    / denominator.data[valid]
)

# Print NDVI statistics
print("\nNDVI STATISTICS")
print("Minimum:", np.nanmin(ndvi))
print("Maximum:", np.nanmax(ndvi))
print("Mean:", np.nanmean(ndvi))

# Save NDVI output
output_folder = PROJECT_ROOT / "data" / "processed"
output_folder.mkdir(parents=True, exist_ok=True)

profile.update(
    dtype="float32",
    count=1,
    nodata=-9999,
    compress="lzw"
)

output_path = output_folder / "osogbo_ndvi.tif"

with rasterio.open(output_path, "w", **profile) as dst:
    dst.write(
        np.where(np.isfinite(ndvi), ndvi, -9999).astype("float32"),
        1
    )

print("\nNDVI saved successfully:", output_path)