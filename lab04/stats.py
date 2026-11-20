def parse_record(line: str) -> dict:
    parts = line.split(";")
    
    if len(parts) != 3:
        raise ValueError("Неверный формат строки")
        
    city = parts[0].strip()
    temp_str = parts[1].strip()
    date = parts[2].strip()
    
    if not city or not date:
        raise ValueError("Пустой город или дата")
        
    try:
        temp_str = temp_str.replace(",", ".")
        temperature = float(temp_str)
    except ValueError:
        raise ValueError("Температура не является числом")
        
    return {"city": city, "temperature": temperature, "date": date}


def read_valid(lines: list[str]) -> list[dict]:
    valid_records = []
    for line in lines:
        if not line.strip():
            continue
            
        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            pass
            
    return valid_records


def average_by_city(records: list[dict]) -> dict:
    if not records:
        return {}
        
    sums = {}
    counts = {}
    
    for r in records:
        city = r["city"]
        temp = r["temperature"]
        
        if city not in sums:
            sums[city] = 0
            counts[city] = 0
            
        sums[city] += temp
        counts[city] += 1
        
    averages = {}
    for city in sums:
        avg = sums[city] / counts[city]
        averages[city] = round(avg, 1)
        
    return averages


def warmest_city(records: list[dict]) -> str:
    averages = average_by_city(records)
    if not averages:
        return ""
        
    max_temp = max(averages.values())
    
    best_cities = []
    for city, temp in averages.items():
        if temp == max_temp:
            best_cities.append(city)
            
    best_cities.sort()
    return best_cities[0]