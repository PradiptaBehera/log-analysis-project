import csv
 
def read_logs(file_path):
    with open(file_path, 'r') as f:
        logs = f.readlines()
    return logs
 
def parse_logs(logs):
    parsed_data = []
 
    for line in logs:
        parts = line.strip().split(" ", 1)  # split into level + message
       
        if len(parts) == 2:
            level, message = parts
            parsed_data.append((level, message))
 
    return parsed_data
 
def save_to_csv(data, output_file):
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["LEVEL", "MESSAGE"])
        writer.writerows(data)
 
def main():
    logs = read_logs("data/sample.log")
    parsed_logs = parse_logs(logs)
 
    save_to_csv(parsed_logs, "output/parsed_logs.csv")
 
    print(f"Processed {len(parsed_logs)} log entries")
    print("Output saved to output/parsed_logs.csv")
 
if __name__ == "__main__":
    main()
