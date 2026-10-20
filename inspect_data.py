import csv

def inspect_column(filename, column) :
    with open(filename, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    values = []
    for row in rows:
        raw = row[column].strip()
        if raw == "":
            continue
        values.append(float(raw))
    return {
        "smallest": min(values),
        "largest": max(values),
        "count": len(values),
    }

area_result = inspect_column("mydata.csv", "area_km2")
name_result = inspect_column("mydata.csv", "area_wrong")

print("Area:", area_result)
print("Name:", name_result)