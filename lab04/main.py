import sys
from stats import parse_record, read_valid, average_by_city, warmest_city

def main():
    lines = sys.stdin.read().splitlines()
    
    non_empty_lines = 0
    for line in lines:
        if line.strip():
            non_empty_lines += 1
            
    valid_records = read_valid(lines)
    errors_count = non_empty_lines - len(valid_records)
    
    averages = average_by_city(valid_records)
    best_city = warmest_city(valid_records)
    
    print(len(valid_records))
    print(errors_count)
    
    if best_city:
        print(f"{averages[best_city]:.1f}")
    else:
        print("0.0")

if __name__ == "__main__":
    main()