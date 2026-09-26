## Week 3 Data Preparation

The datasets were:
- Reprojected to a common working CRS
- Clipped to the study area
- Checked for data quality
- Saved as an analysis-ready GeoPackage

## Original Layer Information

- Layer name: nga_admin2
- Geometry type: Polygon
- Number of features: 774
- Original CRS: EPSG:4326 - WGS 84
- Original CRS unit: Degrees

## Projected Layer Information

- Output layer: Osogbo_utm31
- Projected CRS: EPSG:32631 - WGS 84 / UTM Zone 31N
- Projected CRS unit: Metres
- Number of features: 1
- Output format: GeoPackage

## Fields Created

| Field Name | Data Type | Description | Unit |
|---|---|---|---|
| area_wrong | Decimal number | Area calculated before reprojection | Square degrees |
| area_m2 | Decimal number | Area calculated after reprojection | Square metres |
| area_km2 | Decimal number | Area converted from square metres | Square kilometres |

## Study Area

- Study area name: Osogbo LGA
- State: Osun State
- Country: Nigeria
- Boundary type: Local Government area
- Number of features: 1

## Clipped Area

- Study area name: Roads, Health Facilities
- State: Osun State
- Country: Nigeria
- Boundary type: Local Government area (Osogbo)
- Geometry type: Polygon, Points and LineStrings
