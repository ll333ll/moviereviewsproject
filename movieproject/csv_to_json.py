import csv
import json

csv_file = "movies_initial.csv"
json_file = "movie/management/commands/movies.json"

movies = []

with open(csv_file, encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        movies.append({
            "title": row["title"],
            "genre": row["genre"],
            "year": row["year"],
            "plot": row["description"] if "description" in row else "No description available"
        })

# Guardar como JSON
with open(json_file, "w", encoding="utf-8") as f:
    json.dump(movies, f, indent=4)

print("✅ Archivo JSON generado correctamente.")