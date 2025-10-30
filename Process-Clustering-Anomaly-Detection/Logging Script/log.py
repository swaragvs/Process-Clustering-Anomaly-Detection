import psutil
import csv
import time
import os

# Define your features
FEATURES = ['timestamp', 'pid', 'name', 'username', 'cpu_percent', 'memory_percent', 'disk_read_mb', 'disk_write_mb', 'net_sent_mb', 'net_recv_mb']
FILENAME = 'process_log.csv'

def get_process_data():
    """Gathers data for all running processes."""
    all_procs_data = []
    
    # Get current network I/O counters
    net_io_start = psutil.net_io_counters(pernic=False)
    
    for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_percent', 'io_counters', 'net_connections']):
        try:
            pinfo = proc.info
            
            # Get I/O data
            io_counters = pinfo.get('io_counters')
            if io_counters:
                disk_read_mb = io_counters.read_bytes / (1024 * 1024)
                disk_write_mb = io_counters.write_bytes / (1024 * 1024)
            else:
                disk_read_mb = 0
                disk_write_mb = 0
                
            # Get network I/O (This is tricky, psutil doesn't easily map net I/O to a process)
            # For simplicity, we'll log total network I/O for now.
            # A more advanced solution uses tools like nethogs or libpcap.
            
            all_procs_data.append([
                time.time(),
                pinfo['pid'],
                pinfo['name'],
                pinfo['username'],
                pinfo['cpu_percent'],
                pinfo['memory_percent'],
                disk_read_mb,
                disk_write_mb,
            ])
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
            
    # Calculate network I/O for the interval
    net_io_end = psutil.net_io_counters(pernic=False)
    net_sent_mb = (net_io_end.bytes_sent - net_io_start.bytes_sent) / (1024 * 1024)
    net_recv_mb = (net_io_end.bytes_recv - net_io_start.bytes_recv) / (1024 * 1024)

    # Add total network I/O to all entries for this timestamp (a simplification)
    final_data = [row + [net_sent_mb, net_recv_mb] for row in all_procs_data]
    return final_data

# --- Main Logging Loop ---

# Write header if file doesn't exist
if not os.path.exists(FILENAME):
    with open(FILENAME, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(FEATURES)

print("Logging processes... Press Ctrl+C to stop.")
try:
    while True:
        data = get_process_data()
        
        with open(FILENAME, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data)
            
        print(f"Logged {len(data)} processes at {time.strftime('%H:%M:%S')}")
        
        # Log every 10 seconds
        time.sleep(10) 
        
except KeyboardInterrupt:
    print("Logging stopped.")