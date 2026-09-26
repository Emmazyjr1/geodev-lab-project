# My Project Brief

## Part 1: The Question
How accessible are health facilities to people living in Osogbo LGA, Osun State?

## Part 2: Why It Matters?
Analyzing spatial accessibility to health facilities in Osogbo LGA matters because it reveals "healthcare deserts" and transit bottlenecks across the city's expanding population, providing the Osun State Ministry of Health with the spatial evidence needed to site new clinics and reduce emergency travel times where care is needed most.

## Part 3: Data Needed
- Dataset	          -  What it gives you
- Osun State boundary -	Shows where Osun State is
- LGA boundary	     -   Shows Osogbo LGA
- Ward boundaries	 -   Divides Osogbo into wards
- Health facilities  -   Locations of hospitals/clinics
- Population	    -    Number of people living in areas
- Roads	            -	Shows how people travel to facilities

## Part 4: Where Each Dataset Comes From	        
- Osun State boundary - GRID3 - https://data.grid3.org/datasets/GRID3::grid3-nga-operational-state-boundaries-/explore?location=9.077959%2C8.685290%2C5

- LGA boundary - GRID3 - https://data.grid3.org/datasets/GRID3::grid3-nga-operational-wards-v1-0/about  

- Ward boundaries - GRID3 - https://data.grid3.org/datasets/GRID3::grid3-nga-operational-wards-v1-0/about

- Health facilities - HDX - https://data.humdata.org/dataset/a1e3e4bc-3699-4fe1-bd17-b38f4e7108d2/resource/f45c9266-0458-4160-a902-32661a6a67ed/download/grid3_nga_health_facilities_v3_0.gpkg

		
- Roads - GRID3 - https://data.grid3.org/datasets/GRID3::grid3-nga-roads-v1-0/about          

## Part 5: What i plan to build
I would build a QGIS workflow using health facility and settlement data to generate 500-metre healthcare service catchments, mapping areas across Osogbo's wards that fall outside these catchments to identify potentially underserved areas.
