# process.py
import random
import os
import csv


# Process class for creating, randomizing and handling CPU processes
class Process:
    def __init__(self, pid, arrival_time, duration, priority=None):
        self.pid = pid  # Process ID
        self.arrival_time = arrival_time  # Arrival time of the process
        self.duration = duration  # Duration (time required for the process)
        self.priority = priority  # Priority (used in Priority Scheduling)
        self.remaining_duration = duration  # For algorithms like SRTF and Round Robin
        self.completion_time = 0  # Time when the process completes
        self.turnaround_time = 0  # Turnaround time
        self.waiting_time = 0  # Waiting time
        self.next_execution_time = arrival_time # Used for SRTF

    def __repr__(self):
        return f"Process({self.pid}, {self.arrival_time}, {self.duration}, {self.priority})"

    # Create a deep copy of the process
    def clone(self):
        new_process = Process(self.pid, self.arrival_time, self.duration, self.priority)
        new_process.remaining_duration = self.remaining_duration
        return new_process


# Generates characteristics for random processes
def generate_processes(num_processes):
    processes = []
    for pid in range(1, num_processes + 1):
        arrival_time = random.randint(0, 10)  # Random arrival time between 0 and 10
        duration = random.randint(1, 10)  # Random duration between 1 and 10 units
        priority = random.randint(1, 5)  # Random priority between 1 (high) and 5 (low)
        process = Process(pid, arrival_time, duration, priority)
        processes.append(process)
    return processes


# Creates a transient event
def create_transient_event(current_time):
    new_pid = 999  # Special PID for transient event
    duration = random.randint(1, 10)
    priority = random.randint(1, 5)
    new_process = Process(new_pid, current_time + 1, duration, priority)
    print(f"New transient event (process {new_process.pid}) arrived at time {current_time + 1}!")
    print(f"Process Details: Duration={duration}, Priority={priority}")
    return new_process


# Saves processes to a file for single generation and testing
def save_processes_to_file(processes, filename="processes.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write header
        writer.writerow(["PID", "Arrival Time", "Duration", "Priority"])
        for process in processes:
            writer.writerow([process.pid, process.arrival_time, process.duration, process.priority])


# Loads randomly generated processes from a csv file
def load_processes_from_file(filename="processes.csv"):
    processes = []
    if os.path.exists(filename):  # Check if the file exists
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header
            for row in reader:
                pid = int(row[0])
                arrival_time = int(row[1])
                duration = int(row[2])
                priority = int(row[3])
                process = Process(pid, arrival_time, duration, priority)
                processes.append(process)
    else:
        print(f"File '{filename}' not found. Generating new processes.")
    return processes