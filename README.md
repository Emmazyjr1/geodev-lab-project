# geodev-lab-project
GIS spatial accessibility analysis of health facilities, road networks coverage in Osogbo LGA, Osun State.

## What's in here

```
<project-name>/
├── Month-1/
├── docs/
│   ├── 01-project-brief.md      Week 1
│   ├── 02-data-notes.md         Week 2
│   ├── 03-CRS, Reprojection and Area Calculation.md   Week 3
│   ├── 04-Analysis-&-Results.md  Week 4
│   └── Health_Facilities_Accessibility_Map.png

├── screenshots/
│   └── Week5.png
│   └── check.py.png
│   └── week7.png
│   └── week8.png
│   └── week9.png
│   ├── hello.py      Week 5
│   ├── check.py      Week 6
│   ├── project.toml  Week 6
│   ├── uv.lock       Week 6
│   ├── analyse.py    Week 7
│   ├── wards.csv     Week 7
│   ├── mydata.csv    Week 8
│   ├── inspect_data.py     Week 8
│   ├── summary.py     Week 9
├── data/
│   ├── raw/                     downloads, not committed
│   └── processed/               outputs, not committed
├── scripts/
└── requirements.txt
```
The data is not in this repository. Every source is linked in
[the project brief](/Month-1/docs/01-project-brief.md).

![Health Accessibility Map](/Month-1/docs/Health_Facilities_Accessibility_Map.png)


## Progress

## Month 1: GIS Foundations And Data Ecosystem
- [x] Week 1, project brief with a source link for every dataset
- [x] Week 2, data downloaded, opened and described
- [x] Week 3, reprojected, clipped and quality checked
- [x] Week 4, first spatial analysis, checked four ways

## Month 2: Development Environment And Early Python
- [x] Week 5, set up python, VS code and the terminal. Hello.py runs [week 5](hello.py)
- [x] Week 6, Environments and project setup with uv [week 6](check.py)
- [x] Week 7, Python, the six ideas [week 7](analyse.py)
- [x] Week 8, Python, files and data : Completed inspect_data.py to summarize GIS spatial accessibility analysis data for Osogbo LGA, Osun State, focusing on the area_wrong and area_km2 fields. [week 8](inspect_data.py)
- [x] week 9, Consolidation and refactoring : This week, I learned how to refactor my Python code by breaking a program into smaller, reusable functions. I created separate functions to read CSV data, clean numerical values, and calculate summary statistics such as count, smallest value, largest value, and average. This practical strengthened my understanding of writing clean, reusable code and showed me how Python can support geospatial data analysis and future GIS automation tasks. [week 9](summary.py)
      
## Month 2 Key Lessons:
- Breaking a program into smaller functions
- Reading and processing CSV datasets using Python
- Cleaning numerical values before analysis
- Using loops and dictionaries to summarise multiple columns
- Improving code readability without changing existing behaviour.

## Month 3: Geospatial Python And Automation
- [x] Week 10, GeoPandas, layers as tables [csv_to_points.py](month-03/week-10/csv_to_points.py), [explore_layer.py](month-03/week-10/explore_layer.py), [explore_pandas.py](month-03/week-11/explore_pandas.py), [filter_sort.py](month-03/week-10/filter_sort.py) [geom_props.py](month-03/week-10/geom_props.py), [join_population.py](month-03/week-10/join_population.py), [make_map.py](month-03/week-10/make_map.py), [save_outputs.py](month-03/week-10/save_outputs.py)
- [x] Week 11, Coordinate reference systems and spatial operations in code [area_wrong_and_right.py](month-03/week-11/area_wrong_and_right.py), [set_vs_to.py](month-03/week-11/set_vs_to.py), [spatial_ops.py](month-03/week-11/spatial_ops.py), [coverage_gap.py](month-03/week-11/coverage_gap.py), [nearest.py](month-03/week-11/nearest.py), [clip_dissolve.py](month-03/week-11/clip_dissolve.py), and [fix_geometry.py](month-03/week-11/fix_geometry.py) added
---



#  Author
Emmazy_Jr
