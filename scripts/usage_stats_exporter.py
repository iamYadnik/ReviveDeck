import json
import csv
import os
import pandas as pd

STATS_FILE = "revivedeck_stats.json"

def export_to_csv(stats, output_path="revivedeck_stats_export.csv"):
    with open(output_path, "w", newline="") as csvfile:
        fieldnames = ["Game", "Launches", "Last Played", "Total Time (Seconds)"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for game, data in stats.items():
            writer.writerow({
                "Game": game,
                "Launches": data.get("launches", 0),
                "Last Played": data.get("last_played", ""),
                "Total Time (Seconds)": data.get("total_time_seconds", 0)
            })
    print(f"✅ CSV exported to {output_path}")

def export_to_excel(stats, output_path="revivedeck_stats_export.xlsx"):
    rows = []
    for game, data in stats.items():
        rows.append({
            "Game": game,
            "Launches": data.get("launches", 0),
            "Last Played": data.get("last_played", ""),
            "Total Time (Seconds)": data.get("total_time_seconds", 0)
        })
    df = pd.DataFrame(rows)
    df.to_excel(output_path, index=False)
    print(f"✅ Excel exported to {output_path}")

def load_stats():
    if not os.path.exists(STATS_FILE):
        print("❌ Stats file not found.")
        return None
    with open(STATS_FILE, "r") as f:
        return json.load(f)

if __name__ == "__main__":
    stats = load_stats()
    if stats:
        export_to_csv(stats)
        export_to_excel(stats)