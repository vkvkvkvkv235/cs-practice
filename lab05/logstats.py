LEVELS = ("DEBUG", "INFO", "WARNING", "ERROR")


def parse_event(line):
    parts = line.strip().split(maxsplit=2)
    if len(parts) != 3:
        raise ValueError("bad line")
    time, level, message = parts
    if level not in LEVELS or not message.strip():
        raise ValueError("bad line")
    return {"time": time, "level": level, "message": message}


def count_levels(lines):
    counts = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            level = parse_event(line)["level"]
        except ValueError:
            level = "BROKEN"
        counts[level] = counts.get(level, 0) + 1
    return counts


def top_errors(lines, n):
    counter = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
        except ValueError:
            continue
        if event["level"] == "ERROR":
            counter[event["message"]] = counter.get(event["message"], 0) + 1

    items = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
    return [[msg, cnt] for msg, cnt in items[:n]]


def format_report(counts, errors):
    lines = ["Отчёт по журналу", ""]
    for level in sorted(counts):
        lines.append(f"{level}: {counts[level]}")
    lines += ["", "Частые ошибки:"]
    for msg, cnt in errors:
        lines.append(f"- {msg} — {cnt}")
    lines.append("")
    return "\n".join(lines)