# My Project Brief

## Part 1: The Question
How accessible are health facilities to people living in Osogbo LGA, Osun State?

## Part 2: Why It Matters?
Analyzing spatial accessibility to health facilities in Osogbo LGA matters because it reveals "healthcare deserts" and transit bottlenecks across the city's expanding population, providing the Osun State Ministry of Health with the spatial evidence needed to site new clinics and reduce emergency travel times where care is needed most.

## Part 3: Data Needed
- Dataset	            What it gives you
- Osun State boundary	Shows where Osun State is
- LGA boundary	        Shows Osogbo LGA
- Ward boundaries	    Divides Osogbo into wards
- Health facilities     Locations of hospitals/clinics
- Settlements          	Places where people live
- Population	        Number of people living in areas
- Roads	            	Shows how people travel to facilities

## Part 4: Where Each Dataset Comes From	        
- Osun State boundary - GRID3 - https://data.grid3.org/datasets/GRID3::grid3-nga-operational-state-boundaries-/explore?location=9.077959%2C8.685290%2C5

- LGA boundary - GRID3 - https://data.grid3.org/datasets/GRID3::grid3-nga-operational-wards-v1-0/about  

- Ward boundaries - GRID3 - https://data.grid3.org/datasets/GRID3::grid3-nga-operational-wards-v1-0/about

- Health facilities - GRID3 - https://data.grid3.org/search?bbox=12.687437397251605%2C%206.573922805261585%2C%2024.332945209748512%2C%2019.224963830239595  

- Settlements - GRID3 - (Points & Polygons)
		Points - https://data.grid3.org/datasets/GRID3::grid3-nga-settlement-names/about
     	Polygons - https://data.grid3.org/datasets/GRID3::grid3-nga-settlement-extents-v4-1/about 
		
- Roads - GRID3 - https://data.grid3.org/datasets/GRID3::grid3-nga-roads-v1-0/about          

## Part 5: What i plan to build
I would build a QGIS workflow using GRID3 data to model road-network travel times and generate 5-to-30-minute healthcare service catchments, mapping underserved settlements across Osogbo's wards to identify critical "healthcare deserts."
