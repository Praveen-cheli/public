import csv
from collections import defaultdict

DDOS_PACKET_THRESHOLD = 1000  
UNAUTHORIZED_PORT = 22        

def analyze_network_logs(file_path):
    suspicious_ips = defaultdict(lambda: {'ddos_attempts': 0, 'unauthorized_access': 0})

    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            source_ip = row['source_ip']
            port = int(row['port'])
            packet_count = int(row['packet_count'])

            if packet_count > DDOS_PACKET_THRESHOLD:
                suspicious_ips[source_ip]['ddos_attempts'] += 1

            if port == UNAUTHORIZED_PORT:
                suspicious_ips[source_ip]['unauthorized_access'] += 1

    print("Suspicious IP Report:")
    for ip, activity in suspicious_ips.items():
        if activity['ddos_attempts'] > 0 or activity['unauthorized_access'] > 0:
            print(f"IP Address: {ip}")
            print(f"  DDoS Attempts: {activity['ddos_attempts']}")
            print(f"  Unauthorized Access Attempts on Port {UNAUTHORIZED_PORT}: {activity['unauthorized_access']}")
            print("-" * 40)

if __name__ == "__main__":
    analyze_network_logs('network_logs.csv')

