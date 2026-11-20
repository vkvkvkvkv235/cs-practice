def count_by_extension(paths: list[str]) -> dict[str, int]:
    result = {}
    for path in paths:
        name = path.split("/")[-1]
        dot = name.rfind(".")
        ext = name[dot + 1:].lower() if dot > 0 else ""
        result[ext] = result.get(ext, 0) + 1
    return result

def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""
    max_depth = max(p.count("/") for p in paths)
    return sorted(p for p in paths if p.count("/") == max_depth)[0]

def human_size(n_bytes: int) -> str:
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    size = float(n_bytes)
    i = 0
    while size >= 1024 and i < 4:
        size /= 1024
        i += 1
    return f"{int(size)} Б" if i == 0 else f"{size:.1f} {units[i]}"

#jsgvh