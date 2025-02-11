import csv
import re
from datetime import datetime

LOG_FILE = 'lab1.log'
OUTPUT_CSV = 'invaliduser.csv'

attempts = {}

pattern = re.compile(
    r'^(?P<timestamp>[A-Za-z]{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}).*sshd\[\d+\]:\s+Invalid user\s+(?P<username>\S+)'
)

# read logs
with open(LOG_FILE, 'r') as f:
    for line in f:
        match = pattern.search(line)
        if match:
            timestamp_str = match.group('timestamp')
            username = match.group('username')

            current_year = datetime.now().year
            try:
                ts = datetime.strptime(f"{timestamp_str} {current_year}", "%b %d %H:%M:%S %Y")
            except ValueError:
                continue

            if username not in attempts:
                attempts[username] = {'count': 1, 'first': ts, 'last': ts}
            else:
                attempts[username]['count'] += 1
                if ts < attempts[username]['first']:
                    attempts[username]['first'] = ts
                if ts > attempts[username]['last']:
                    attempts[username]['last'] = ts

# write to CSV
with open(OUTPUT_CSV, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Username', 'Total Number of Attempts', 'Time of First Attempt', 'Time of Last Attempt'])
    for username, data in attempts.items():
        writer.writerow([
            username,
            data['count'],
            data['first'].strftime('%Y-%m-%d %H:%M:%S'),
            data['last'].strftime('%Y-%m-%d %H:%M:%S')
        ])

print(f"Completed file '{OUTPUT_CSV}' with {len(attempts)} entries.")