def count_by_extension(paths: list[str]) -> dict[str, int]:
    result = {}
    for path in paths:
        name = path.split("/")[-1]
        ext = name.rsplit(".", 1)[-1].lower() if "." in name else ""
        result[ext] = result.get(ext, 0) + 1
    return result


def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""
    best = max(paths, key=lambda p: (p.count("/"), [-ord(c) for c in p]))
    # при равенстве глубины — первый по алфавиту
    depth = best.count("/")
    same = [p for p in paths if p.count("/") == depth]
    return sorted(same)[0]


def human_size(n_bytes: int) -> str:
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    size = float(n_bytes)
    i = 0
    while size >= 1024 and i < len(units) - 1:
        size /= 1024
        i += 1
    return f"{int(size)} Б" if i == 0 else f"{size:.1f} {units[i]}"

#jsgvh