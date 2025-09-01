#Files, Paths, and OS------------------------------------------------------

#Reading Writing Files
with open("file.txt", "r") as f:
    content = f.read()
    print(content)

with open("file.txt", "w") as f:
    f.write("Hello, world!")

with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("Line 1\nLine 2")

with open("notes.txt", "r", encoding="utf-8") as f:
    print(f.read())

#Pathlib,Os,Shutil-----------------------------------------------------------------

from pathlib import Path
p = Path("logs")
p.mkdir(exist_ok=True)
print(list(p.iterdir()))

# CSV/JSON---------------------------------------------------------------
import csv, json


rows = [{"name": "Joon", "age": 21}, {"name": "Raj", "age": 23}]
with open("people.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["name", "age"])
    w.writeheader()
    w.writerows(rows)


print(json.dumps(rows, indent=2))