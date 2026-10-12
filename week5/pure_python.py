f = open("scores.csv", "r", encoding="utf-8")
lines = f.readlines()
f.close()

print(len(lines))       # Prints total lines (header + data rows)[cite: 5]
print(lines[0])         # Prints the header row[cite: 5]
print(lines[1])         # Prints the first data row[cite: 5]

f = open("scores.csv", "r", encoding="utf-8")
lines = f.readlines()
f.close()

# Find column indexes dynamically
header = lines[0].strip().split(",")
cat_idx = header.index("category")
score_idx = header.index("score")

# Test looping through the first few rows
for line in lines[1:4]:
    parts = line.strip().split(",")
    print(parts[cat_idx], parts[score_idx])

f = open("scores.csv", "r", encoding="utf-8")
lines = f.readlines()
f.close()

header = lines[0].strip().split(",")
cat_idx = header.index("category")
score_idx = header.index("score")

count = 0
totals = {}
counts = {}

for line in lines[1:]:
    parts = line.strip().split(",")
    raw = parts[score_idx].strip()
    
    # Skip empty values
    if raw == "":
        continue
        
    # Skip non-numeric values (like text) safely
    try:
        score = float(raw)
    except ValueError:
        continue
        
    count = count + 1
    category = parts[cat_idx]
    
    # Initialize dictionary if it's the first time seeing this category
    if category not in totals:
        totals[category] = 0.0
        counts[category] = 0
        
    totals[category] += score
    counts[category] += 1

print("Valid rows processed:", count)
print("Totals:", totals)
print("Counts:", counts)

f = open("scores.csv", "r", encoding="utf-8")
lines = f.readlines()
f.close()

header = lines[0].strip().split(",")
cat_idx = header.index("category")
score_idx = header.index("score")

count = 0
totals = {}
counts = {}

for line in lines[1:]:
    parts = line.strip().split(",")
    raw = parts[score_idx].strip()
    
    if raw == "":
        continue
        
    try:
        score = float(raw)
    except ValueError:
        continue
        
    count = count + 1
    category = parts[cat_idx]
    
    if category not in totals:
        totals[category] = 0.0
        counts[category] = 0
        
    totals[category] += score
    counts[category] += 1

# Calculate and print sorted averages rounded to 2 decimal places[cite: 8]
for c in sorted(totals.keys()):
    avg = totals[c] / counts[c]
    print(c, round(avg, 2))

