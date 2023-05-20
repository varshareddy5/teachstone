import csv
import datetime
import requests

#Download this CSV file
csv_url = "https://github.com/datablist/sample-csv-files/raw/main/files/organizations/organizations-100.csv"
response = requests.get(csv_url)
csv_data = response.content.decode('utf-8')
names = []

#
reader = csv.reader(csv_data.splitlines())
next(reader)
for row in reader:
    names.append(f"{row[2]}")
sorted_names = sorted(names)
with open('/tmp/names.txt', 'w') as file:
    file.write(f"{sorted_names}\n")

#Summarize the number of employees across
total_employees = 0
reader = csv.reader(csv_data.splitlines())
next(reader)
for row in reader:
    total_employees = sum (int(row[8]) for row in reader)
with open('/tmp/employee_count.txt', 'w') as file:
    file.write(f"Total number of employees: {total_employees}\n")


lines_with_inc = []
reader = csv.reader(csv_data.splitlines())
for row in reader:
    if "Inc" in row[2]:
        lines_with_inc.append(','.join(row))
lines_with_inc_str = '\n'.join(lines_with_inc)
with open('/tmp/lines-with-inc.txt', 'w') as file:
    file.write(lines_with_inc_str)



current_date = datetime.date.today().strftime("%m/%d/%Y")
public_ip = requests.get("https://api.ipify.org").text
with open('/tmp/employee_count.txt', 'r') as file:
    header_line = file.readline()

final_report = f"Report created on {current_date} from {public_ip}\n\n"
final_report += f"{header_line}\n\n"
final_report += "Company names that contain the word Inc:\n"

csv_file = '/tmp/lines-with-inc.txt'
with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row
    data = [row[2] for row in reader]
sorted_data = sorted(data)
for name in sorted_data:
    final_report += f"* {name}\n"



with open('/tmp/names.txt', 'r') as file:
    contents = file.read()
    items = [item.strip().strip("'") for item in contents[1:-1].split(',')]
    sorted_items = sorted(items)
final_report += "\nAll names, sorted:\n"
for name in sorted_items:
    final_report += f"* {name}\n"
with open('/tmp/final-report.txt', 'w') as file:
    file.write(final_report)

print(f"Final report saved to: /tmp/final-report.txt")

