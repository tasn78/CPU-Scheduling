# Main
import os
from process import Process, generate_processes,save_processes_to_file, load_processes_from_file
from scheduling import fcfs_scheduling, sjf_scheduling, priority_scheduling, srtf_scheduling, round_robin_scheduling

def main():
    # Define the file where processes are saved
    filename = "processes.csv"

    # Check if the file exists
    if os.path.exists(filename):
        # Load processes from the file
        processes = load_processes_from_file(filename)
        print("Loaded processes from file:")
    else:
        # Generate 13 processes (since your ID ends in "03")
        processes = generate_processes(13)
        # Save the generated processes to a file for future use
        save_processes_to_file(processes, filename)
        print("Generated new processes and saved to file:")

    # Print out the loaded/generated processes
    for process in processes:
        print(process)

    # Call each scheduling algorithm and display the results

    # First Come First Serve (FCFS)
    print("\n--- FCFS Scheduling ---")
    fcfs_scheduling(processes)

    # Shortest Job First (SJF)
    print("\n--- SJF Scheduling ---")
    sjf_scheduling(processes)

    # Priority Scheduling
    print("\n--- Priority Scheduling ---")
    priority_scheduling(processes)

    # Shortest Remaining Time First (SRTF)
    print("\n--- SRTF Scheduling ---")
    srtf_scheduling(processes)

    # Round Robin Scheduling (with a time quantum of 2 units)
    print("\n--- Round Robin Scheduling ---")
    round_robin_scheduling(processes, time_quantum=2)


if __name__ == "__main__":
    main()