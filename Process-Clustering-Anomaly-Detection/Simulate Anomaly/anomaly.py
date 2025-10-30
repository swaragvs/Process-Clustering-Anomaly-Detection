import time
import os
import sys

# --- 1. Controlled CPU Anomaly ---
def run_cpu_anomaly(duration, work_time=0.05, sleep_time=0.05):
    """
    Runs a throttled CPU load (approx. 50%) for a fixed duration.
    """
    start_time = time.time()
    print(f"--- 1. Running CPU Anomaly for {duration} seconds... ---")
    
    try:
        while time.time() - start_time < duration:
            # 1. Work phase (burns CPU)
            work_start = time.time()
            while time.time() - work_start < work_time:
                x = 99999 * 99999
                pass
            
            # 2. Sleep phase (idles)
            time.sleep(sleep_time)
            
    except KeyboardInterrupt:
        print("CPU anomaly interrupted.")
        raise  # Re-raise to stop the main script
        
    print(f"--- CPU Anomaly finished ({duration}s). ---")

# --- 2. Controlled RAM Anomaly ---
def run_ram_anomaly(duration, target_mb=500, chunk_mb=10):
    """
    Allocates up to 'target_mb' of RAM and holds it for 'duration' seconds.
    """
    print(f"\n--- 2. Running RAM Anomaly for {duration} seconds... ---")
    print(f"Allocating up to {target_mb} MB and holding...")
    
    big_list = []
    chunk = ' ' * (chunk_mb * 1024 * 1024)
    max_chunks = target_mb // chunk_mb
    start_time = time.time()

    try:
        # First, allocate the memory
        for i in range(max_chunks):
            big_list.append(chunk)
            # Stop allocating if the total time is already up
            if time.time() - start_time > duration:
                break
            time.sleep(0.05) # Small pause to make allocation gradual

        print(f"Allocated {len(big_list) * chunk_mb} MB.")
        
        # Now, hold the memory for the remaining time
        print(f"Holding memory for the remaining duration...")
        while time.time() - start_time < duration:
            time.sleep(0.5)
            
    except MemoryError:
        print(f"Hit memory limit. Holding {len(big_list) * chunk_mb} MB for the duration...")
        while time.time() - start_time < duration:
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("RAM anomaly interrupted.")
        raise # Re-raise to stop the main script
    finally:
        del big_list # Explicitly release the memory
        print(f"--- RAM Anomaly finished ({duration}s). Memory released. ---")

# --- 3. Controlled Disk I/O Anomaly ---
def run_disk_anomaly(duration, chunk_mb=20, sleep_time=0.5):
    """
    Continuously writes to a temporary file for 'duration' seconds, 
    then cleans it up.
    """
    print(f"\n--- 3. Running Disk Anomaly for {duration} seconds... ---")
    filename = "anomaly_test_file.tmp"
    chunk = b'0' * (chunk_mb * 1024 * 1024)
    start_time = time.time()
    total_written = 0

    try:
        with open(filename, 'wb') as f:
            while time.time() - start_time < duration:
                f.write(chunk)
                f.flush() # Ensure it's written to disk
                total_written += chunk_mb
                print(f"  > Wrote {chunk_mb}MB... (Total: {total_written}MB)")
                time.sleep(sleep_time)
                
                # Rewind the file if it gets too big (e.g., > 1GB)
                if total_written > 1024:
                    f.seek(0)
                    total_written = 0
                    print("  > File > 1GB, rewinding.")

    except KeyboardInterrupt:
        print("Disk anomaly interrupted.")
        raise # Re-raise to stop the main script
    except Exception as e:
        print(f"Disk Anomaly error: {e}")
    finally:
        # This cleanup is critical
        if os.path.exists(filename):
            os.remove(filename)
            print(f"Cleaned up '{filename}'.")
        print(f"--- Disk Anomaly finished ({duration}s). ---")

# --- Main execution ---
if __name__ == "__main__":
    
    # Total duration for EACH anomaly
    SIMULATION_TIME = 60 
    
    try:
        # Run CPU Anomaly
        run_cpu_anomaly(SIMULATION_TIME)
        
        print("\nPausing for 5 seconds between anomalies...")
        time.sleep(5)
        
        # Run RAM Anomaly
        run_ram_anomaly(SIMULATION_TIME)
        
        print("\nPausing for 5 seconds between anomalies...")
        time.sleep(5)
        
        # Run Disk Anomaly
        run_disk_anomaly(SIMULATION_TIME)
        
        print("\n\n--- ✅ All anomalies complete. ---")

    except KeyboardInterrupt:
        print("\n\n--- 🛑 Simulation sequence stopped by user. ---")
    finally:
        # Final cleanup just in case the script was stopped mid-disk-anomaly
        if os.path.exists("anomaly_test_file.tmp"):
            os.remove("anomaly_test_file.tmp")
            print("Final cleanup of temp file complete.")
        sys.exit(0)