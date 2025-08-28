import subprocess
import time
import sys
from datetime import datetime

def run_batch_and_log(bat_file, log_file):
    start_time = datetime.now()
    process = subprocess.run(bat_file, shell=True)
    end_time = datetime.now()
    
    duration = (end_time - start_time).total_seconds()
    
    with open(log_file, "a") as log:
        log.write(f"{bat_file} ran on {start_time} and took {duration:.2f} seconds\n")
    
    return duration

def main(bat1, bat2, log_file):
    while True:
        # Log the start time of the entire process
        process_start_time = datetime.now()
        with open(log_file, "a") as log:
            log.write(f"Process started at {process_start_time}\n")
        
        # Run the first batch file and log
        duration_a = run_batch_and_log(bat1, log_file)
        
        # Run the second batch file and log
        duration_b = run_batch_and_log(bat2, log_file)
        
        # Calculate total duration for both batch files
        total_duration = duration_a + duration_b
        
        # Log the total time taken for both batch files and end time of the process
        process_end_time = datetime.now()
        with open(log_file, "a") as log:
            log.write(f"Total time for both batch files: {total_duration:.2f} seconds\n")
            log.write(f"Process finished at {process_end_time}\n")
            log.write("="*50 + "\n")
        
        # Wait 10 minutes before starting the next run
        time.sleep(600)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python run_batches.py <path_to_a.bat> <path_to_b.bat> <log_file>")
        print("runing the bat files using python scripts folder")
        sys.exit(1)
    
    bat1_path = sys.argv[1]
    bat2_path = sys.argv[2]
    log_file_path = sys.argv[3]
    
    main(bat1_path, bat2_path, log_file_path)
