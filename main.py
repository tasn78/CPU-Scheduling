# main.py

import os
from process import Process, generate_processes, save_processes_to_file, load_processes_from_file
from scheduling import fcfs_scheduling, sjf_scheduling, priority_scheduling, srtf_scheduling, round_robin_scheduling


def main():
    # Define the file where processes are saved
    filename = "processes.csv"

    # Check if the file exists
    if os.path.exists(filename):
        # Load processes from the file
        original_processes = load_processes_from_file(filename)
        print("Loaded processes from file:")
    else:
        # Generate 13 processes (last two digits of your ID + 10 if needed)
        original_processes = generate_processes(13)
        # Save the generated processes to a file for future use
        save_processes_to_file(original_processes, filename)
        print("Generated new processes and saved to file:")

    # Print out the loaded/generated processes
    for process in original_processes:
        print(process)

    # First Come First Serve (FCFS)
    print("\n--- FCFS Scheduling ---")
    fcfs_results = fcfs_scheduling(original_processes)

    # Shortest Job First (SJF)
    print("\n--- SJF Scheduling ---")
    sjf_results = sjf_scheduling(original_processes)

    # Priority Scheduling
    print("\n--- Priority Scheduling ---")
    priority_results = priority_scheduling(original_processes)

    # Shortest Remaining Time First (SRTF)
    print("\n--- SRTF Scheduling ---")
    srtf_results = srtf_scheduling(original_processes)

    # Round Robin Scheduling (with a time quantum of 2 units)
    print("\n--- Round Robin Scheduling ---")
    rr_results = round_robin_scheduling(original_processes, time_quantum=2)

    # Compare all algorithms
    # Calculate average metrics for each algorithm
    avg_waiting_fcfs = sum(p.waiting_time for p in fcfs_results) / len(fcfs_results)
    avg_turnaround_fcfs = sum(p.turnaround_time for p in fcfs_results) / len(fcfs_results)

    avg_waiting_sjf = sum(p.waiting_time for p in sjf_results) / len(sjf_results)
    avg_turnaround_sjf = sum(p.turnaround_time for p in sjf_results) / len(sjf_results)

    avg_waiting_priority = sum(p.waiting_time for p in priority_results) / len(priority_results)
    avg_turnaround_priority = sum(p.turnaround_time for p in priority_results) / len(priority_results)

    avg_waiting_srtf = sum(p.waiting_time for p in srtf_results) / len(srtf_results)
    avg_turnaround_srtf = sum(p.turnaround_time for p in srtf_results) / len(srtf_results)

    avg_waiting_rr = sum(p.waiting_time for p in rr_results) / len(rr_results)
    avg_turnaround_rr = sum(p.turnaround_time for p in rr_results) / len(rr_results)

    print("\n--- Comparison of Scheduling Algorithms ---")
    print("{:<15} {:<20} {:<20}".format("Algorithm", "Avg Waiting Time", "Avg Turnaround Time"))
    print("-" * 60)
    print("{:<15} {:<20.2f} {:<20.2f}".format("FCFS", avg_waiting_fcfs, avg_turnaround_fcfs))
    print("{:<15} {:<20.2f} {:<20.2f}".format("SJF", avg_waiting_sjf, avg_turnaround_sjf))
    print("{:<15} {:<20.2f} {:<20.2f}".format("Priority", avg_waiting_priority, avg_turnaround_priority))
    print("{:<15} {:<20.2f} {:<20.2f}".format("SRTF", avg_waiting_srtf, avg_turnaround_srtf))
    print("{:<15} {:<20.2f} {:<20.2f}".format("Round Robin", avg_waiting_rr, avg_turnaround_rr))


if __name__ == "__main__":
    main()