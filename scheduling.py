# scheduling.py
import random
from process import create_transient_event


# Utility function to calculate waiting time
def calculate_waiting_time(process):
    return process.turnaround_time - process.duration


# Utility function to calculate turnaround time
def calculate_turnaround_time(process):
    return process.completion_time - process.arrival_time


# Utility function to calculate completion time
def calculate_completion_time(process, current_time):
    return current_time + process.duration


# Utility function to print process details
def print_process_info(process):
    print(f"Process {process.pid} completed at time {process.completion_time}, "
          f"Waiting Time: {process.waiting_time}, Turnaround Time: {process.turnaround_time}")


# FCFS Scheduling
def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x.arrival_time)  # Sort by arrival time

    current_time = 0
    transient_event_triggered = False  # Flag to ensure only one transient event occurs
    # Random moment when the transient event will happen (between 0 and current time)
    event_time = random.randint(0, 10)  # Set the event time within the range of process execution

    for process in processes:
        # Trigger the transient event once at the specified time
        if not transient_event_triggered and current_time >= event_time:
            create_transient_event(current_time, processes)
            transient_event_triggered = True  # Set the flag to avoid triggering the event again

        # Ensure process starts when it arrives
        if current_time <= process.arrival_time:
            current_time = process.arrival_time

        # Calculate completion, turnaround, and waiting times
        process.completion_time = calculate_completion_time(process, current_time)
        process.turnaround_time = calculate_turnaround_time(process)
        process.waiting_time = calculate_waiting_time(process)

        # Update current time for the next process
        current_time = process.completion_time

        # Print process info
        print_process_info(process)


# SJF Scheduling
def sjf_scheduling(processes):
    processes.sort(key=lambda x: (x.arrival_time, x.duration))  # Sort by arrival time and duration

    current_time = 0
    transient_event_triggered = False  # Flag to ensure only one transient event occurs
    # Random moment when the transient event will happen (between 0 and current time)
    event_time = random.randint(0, 10)  # Set the event time within the range of process execution

    for process in processes:
        # Trigger the transient event once at the specified time
        if not transient_event_triggered and current_time >= event_time:
            create_transient_event(current_time, processes)
            transient_event_triggered = True  # Set the flag to avoid triggering the event again

        # Ensure process starts when it arrives
        if current_time <= process.arrival_time:
            current_time = process.arrival_time

        # Calculate completion, turnaround, and waiting times
        process.completion_time = calculate_completion_time(process, current_time)
        process.turnaround_time = calculate_turnaround_time(process)
        process.waiting_time = calculate_waiting_time(process)

        # Update current time for the next process
        current_time = process.completion_time

        # Print process info
        print_process_info(process)


# Priority Scheduling
def priority_scheduling(processes):
    processes.sort(key=lambda x: (x.arrival_time, x.priority))  # Sort by arrival time and priority

    current_time = 0
    transient_event_triggered = False  # Flag to ensure only one transient event occurs
    # Random moment when the transient event will happen (between 0 and current time)
    event_time = random.randint(0, 10)  # Set the event time within the range of process execution

    for process in processes:
        # Trigger the transient event once at the specified time
        if not transient_event_triggered and current_time >= event_time:
            create_transient_event(current_time, processes)
            transient_event_triggered = True  # Set the flag to avoid triggering the event again

        # Ensure process starts when it arrives
        if current_time <= process.arrival_time:
            current_time = process.arrival_time

        # Calculate completion, turnaround, and waiting times
        process.completion_time = calculate_completion_time(process, current_time)
        process.turnaround_time = calculate_turnaround_time(process)
        process.waiting_time = calculate_waiting_time(process)

        # Update current time for the next process
        current_time = process.completion_time

        # Print process info
        print_process_info(process)


# SRTF Scheduling
def srtf_scheduling(processes):
    processes.sort(key=lambda x: x.arrival_time)  # Sort by arrival time

    current_time = 0
    queue = []
    transient_event_triggered = False  # Flag to ensure only one transient event occurs
    # Random moment when the transient event will happen (between 0 and current time)
    event_time = random.randint(0, 10)  # Set the event time within the range of process execution

    while processes or queue:
        # Add all processes that have arrived to the queue
        while processes and processes[0].arrival_time <= current_time:
            queue.append(processes.pop(0))

        if queue:
            # Trigger the transient event once at the specified time
            if not transient_event_triggered and current_time >= event_time:
                create_transient_event(current_time, processes)
                transient_event_triggered = True  # Set the flag to avoid triggering the event again

            # Sort the queue by remaining duration for SRTF
            queue.sort(key=lambda x: x.remaining_duration)
            process = queue.pop(0)

            # Ensure process starts when it arrives
            if current_time <= process.arrival_time:
                current_time = process.arrival_time

            process.completion_time = calculate_completion_time(process, current_time)
            process.turnaround_time = calculate_turnaround_time(process)
            process.waiting_time = calculate_waiting_time(process)

            current_time = process.completion_time

            # Print process info
            print_process_info(process)


# Round Robin Scheduling
def round_robin_scheduling(processes, time_quantum):
    current_time = 0
    queue = processes[:]  # Create a copy of the list of processes
    transient_event_triggered = False  # Flag to ensure only one transient event occurs
    event_time = random.randint(0, 10)  # Random moment for when transient event will happen

    print(f"\n--- Round Robin Scheduling ---")

    while queue:
        print(f"\nTime Quantum {current_time}:")

        # Temporary list to track the processes in the current quantum
        processes_in_this_quantum = []

        # Loop over processes that are still in the queue
        for process in queue[:]:  # Use a slice to prevent modification while iterating
            # Trigger the transient event only once at the specified time
            if not transient_event_triggered and current_time >= event_time:
                create_transient_event(current_time, processes)
                transient_event_triggered = True  # Set the flag to avoid triggering the event again
                print(f"Transient event triggered at time {current_time}")

            if current_time <= process.arrival_time:  # Process starts as soon as it arrives
                current_time = process.arrival_time
                print(f"Process {process.pid} starts at time {current_time}")

            # Add the current process to the list of processes running in this quantum
            processes_in_this_quantum.append(f"Process {process.pid}")

            # Execute the process for the time quantum
            if process.remaining_duration > time_quantum:
                current_time += time_quantum
                process.remaining_duration -= time_quantum
                queue.append(process)  # Requeue if not finished
                print(f"Process {process.pid} requeued with remaining duration {process.remaining_duration}")
            else:
                current_time += process.remaining_duration
                process.remaining_duration = 0  # Process finishes execution
                print(f"Process {process.pid} completed at time {current_time}")

            # Only remove the process from the queue if it is completed
            if process.remaining_duration == 0:
                queue.remove(process)

            # Calculate waiting time and turnaround time
            process.turnaround_time = calculate_turnaround_time(process)
            process.waiting_time = calculate_waiting_time(process)

            # Print process info after the process is completed
            print_process_info(process)

        # Print the order of processes in the current time quantum
        print(f"Processes in this quantum: -> ".join(processes_in_this_quantum))

    print(f"Round Robin scheduling complete.")



