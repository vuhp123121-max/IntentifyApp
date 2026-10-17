import csv
from collections import Counter
from pathlib import Path

data_path = Path(__file__).parent / "data" / "dataset" / "intents.csv"

with data_path.open("r", encoding="utf-8", newline="") as file:
    rows = list(csv.DictReader(file))

if not rows or "sentence" not in rows[0] or "intent" not in rows[0]:
    raise ValueError("CSV cần 2 cột: sentences, intent")

label_counts = Counter(row["intent"] for row in rows)
print(f"Số câu: {len(rows)}")
print("Số câu muốn intent:")
for intent, count in sorted(label_counts.items()):
    print(f"{intent}: {count}")   