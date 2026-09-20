# Data Notes

## Project: Osun State GIS Data

- Study area: Osogbo LG, Osun State, Nigeria
- Purpose: To explore administrative boundaries and OpenStreetMap features using QGIS.

## Osogbo Local Government Area

- Number of official LGA: 1
- Source: https://data.grid3.org/datasets/GRID3::grid3-nga-operational-wards-v1-0/about
- Geometry: Polygon
- Fields: 14
- Coverage: 100%
- Null values: 0
- Geometry: Polygon
- Surface information: Osogbo LGA
- Coverage: 100%


## OSM Roads, Extracted via Grid3

- Source: https://data.grid3.org/datasets/GRID3::grid3-nga-roads-v1-0/explore?location=9.080717%2C8.679507%2C5
- Tool: QuickOSM in QGIS
- Query: highway= road
- Extracted: 13-09-2026
- Features: 4508
- Geometry: LineString, Polygon
- Surface information: motorways, residential streets, service roads, footways, and trails
- Coverage: 100%

## OSM Health Facilities(hospitals, clinics, Pharmacies, doctors, and dentists), Extracted via HDX

- Source: https://data.humdata.org/dataset/hotosm_nga_health_facilities
- Tool: QuickOSM in QGIS
- Query: amenity= pharmacy
- Extracted: 13-09-2026
- Features: 25
- Geometry: Point, Polygon
- Key Columns: website, opening_hours, addr:street, amenity, addr:city, full_id, osm_id, osm_type, amenity and name
- Null values: 0
- Coverage: 100%
