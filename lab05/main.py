from logstats import count_levels, top_errors, format_report

path = input().strip()

with open(path, encoding="utf-8") as f:
    counts = count_levels(f)

with open(path, encoding="utf-8") as f:
    errors = top_errors(f, 10)

print(sum(counts.values()))
print(counts.get("ERROR", 0))
print(counts.get("BROKEN", 0))

with open("report.txt", "w", encoding="utf-8") as f:
    f.write(format_report(counts, errors))