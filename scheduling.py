# scheduling.py
import random
from process import create_transient_event


# Utility function to calculate waiting time
def calculate_waiting_time(process):
    return process.completion_time - process.arrival_time - process.duration


# Utility function to calculate turnaround time
def calculate_turnaround_time(process):
    return process.completion_time - process.arrival_time


# Utility function to print process details
def print_process_info(process):
    print(f"Process {process.pid} completed at time {process.completion_time}, "
          f"Waiting Time: {process.waiting_time}, Turnaround Time: {process.turnaround_time}")


# Utility function to print algorithm summary
def print_algorithm_summary(algorithm_name, processes):
    total_waiting_time = sum(process.waiting_time for process in processes)
    total_turnaround_time = sum(process.turnaround_time for process in processes)
    avg_waiting_time = total_waiting_time / len(processes)
    avg_turnaround_time = total_turnaround_time / len(processes)

    print(f"\n--- {algorithm_name} Summary ---")
    print(f"Average Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")


# FCFS (First Come First Served) Scheduling
def fcfs_scheduling(original_processes):
    # Create a copy of processes to avoid modifying the original list
    processes = [process.clone() for process in original_processes]
    processes.sort(key=lambda x: x.arrival_time)  # Sort by arrival time

    current_time = 0
    event_time = random.randint(5, 15)  # Set a single event time for this run
    transient_event_triggered = False
    transient_process = None
    completed_processes = []

    i = 0
    while i < len(processes):
        # Check if the transient event should be triggered (only once)
        if not transient_event_triggered and current_time >= event_time:
            # Create the transient event
            transient_process = create_transient_event(current_time)

            # Set the arrival time to the current time
            transient_process.arrival_time = current_time

            # Immediately process the transient event before continuing
            if current_time < transient_process.arrival_time:
                current_time = transient_process.arrival_time

            print(f"Starting Transient Process {transient_process.pid} at time {current_time}")
            transient_process.completion_time = current_time + transient_process.duration
            transient_process.turnaround_time = calculate_turnaround_time(transient_process)
            transient_process.waiting_time = calculate_waiting_time(transient_process)

            # Update current time
            current_time = transient_process.completion_time
            print_process_info(transient_process)
            completed_processes.append(transient_process)

            # Mark the transient event as triggered
            transient_event_triggered = True

        # Handle regular processes
        process = processes[i]
        # Ensure process starts when it arrives
        if current_time < process.arrival_time:
            current_time = process.arrival_time

        print(f"Starting Process {process.pid} at time {current_time}")

        # Calculate completion time
        process.completion_time = current_time + process.duration
        process.turnaround_time = calculate_turnaround_time(process)
        process.waiting_time = calculate_waiting_time(process)

        # Update current time for the next process
        current_time = process.completion_time

        # Print process info
        print_process_info(process)
        completed_processes.append(process)
        i += 1

    print_algorithm_summary("FCFS", completed_processes)
    return completed_processes


# SJF (Shortest Job First) Scheduling
def sjf_scheduling(original_processes):
    # Create a copy of processes to avoid modifying the original list
    processes = [process.clone() for process in original_processes]

    current_time = 0
    event_time = random.randint(5, 15)  # Set a single event time for this run
    transient_event_triggered = False
    remaining_processes = sorted(processes, key=lambda x: x.arrival_time)
    completed_processes = []

    while remaining_processes:
        # Check if the transient event should be triggered (only once)
        if not transient_event_triggered and current_time >= event_time:
            # Create the transient event
            transient_process = create_transient_event(current_time)

            # Set the arrival time to the current time
            transient_process.arrival_time = current_time

            # Immediately process the transient event before continuing
            if current_time < transient_process.arrival_time:
                current_time = transient_process.arrival_time

            print(f"Starting Transient Process {transient_process.pid} at time {current_time}")
            transient_process.completion_time = current_time + transient_process.duration
            transient_process.turnaround_time = calculate_turnaround_time(transient_process)
            transient_process.waiting_time = calculate_waiting_time(transient_process)

            # Update current time
            current_time = transient_process.completion_time
            print_process_info(transient_process)
            completed_processes.append(transient_process)

            # Mark the transient event as triggered
            transient_event_triggered = True

        # Get available processes at the current time
        available_processes = [p for p in remaining_processes if p.arrival_time <= current_time]

        # No available processes - jump to next arrival time
        if not available_processes:
            current_time = min(p.arrival_time for p in remaining_processes)
            continue

        # Select process with the shortest duration among the available processes
        next_process = min(available_processes, key=lambda x: x.duration)
        print(f"Starting Process {next_process.pid} at time {current_time}")

        # Calculate completion time for the selected process
        next_process.completion_time = current_time + next_process.duration
        next_process.turnaround_time = calculate_turnaround_time(next_process)
        next_process.waiting_time = calculate_waiting_time(next_process)

        # Update current time
        current_time = next_process.completion_time

        # Print process info
        print_process_info(next_process)

        # Move process from remaining to completed
        remaining_processes.remove(next_process)
        completed_processes.append(next_process)

    print_algorithm_summary("SJF", completed_processes)
    return completed_processes


# Priority Scheduling
def priority_scheduling(original_processes):
    # Create a copy of processes to avoid modifying the original list
    processes = [process.clone() for process in original_processes]

    current_time = 0
    event_time = random.randint(5, 15)  # Set a single event time for this run
    transient_event_triggered = False
    remaining_processes = sorted(processes, key=lambda x: x.arrival_time)
    completed_processes = []

    while remaining_processes:
        # Check if the transient event should be triggered (only once)
        if not transient_event_triggered and current_time >= event_time:
            # Create the transient event
            transient_process = create_transient_event(current_time)

            # Set the arrival time to the current time
            transient_process.arrival_time = current_time

            # Immediately process the transient event before continuing
            if current_time < transient_process.arrival_time:
                current_time = transient_process.arrival_time

            print(
                f"Starting Transient Process {transient_process.pid} (Priority {transient_process.priority}) at time {current_time}")
            transient_process.completion_time = current_time + transient_process.duration
            transient_process.turnaround_time = calculate_turnaround_time(transient_process)
            transient_process.waiting_time = calculate_waiting_time(transient_process)

            # Update current time
            current_time = transient_process.completion_time
            print_process_info(transient_process)
            completed_processes.append(transient_process)

            # Mark the transient event as triggered
            transient_event_triggered = True

        # Get available processes at current time
        available_processes = [p for p in remaining_processes if p.arrival_time <= current_time]

        if not available_processes:
            # Jump to the next arrival time if no processes are available
            current_time = min(p.arrival_time for p in remaining_processes)
            continue

        # Select process with the highest priority (lowest number) among the available processes
        next_process = min(available_processes, key=lambda x: x.priority)

        print(f"Starting Process {next_process.pid} (Priority {next_process.priority}) at time {current_time}")

        # Calculate completion time
        next_process.completion_time = current_time + next_process.duration
        next_process.turnaround_time = calculate_turnaround_time(next_process)
        next_process.waiting_time = calculate_waiting_time(next_process)

        # Update current time
        current_time = next_process.completion_time

        # Print process info
        print_process_info(next_process)

        # Move process from remaining to completed
        remaining_processes.remove(next_process)
        completed_processes.append(next_process)

    print_algorithm_summary("Priority Scheduling", completed_processes)
    return completed_processes


# SRTF (Shortest Remaining Time First) Scheduling
def srtf_scheduling(original_processes):
    # Create a copy of processes to avoid modifying the original list
    processes = [process.clone() for process in original_processes]

    print("\n--- SRTF (Shortest Remaining Time First) Scheduling ---")

    current_time = 0
    event_time = random.randint(5, 15)  # Set a single event time for this run
    transient_event_triggered = False
    remaining_processes = sorted(processes, key=lambda x: x.arrival_time)
    completed_processes = []

    while remaining_processes:
        # Check if the transient event should be triggered (only once)
        if not transient_event_triggered and current_time >= event_time:
            # Create the transient event
            transient_process = create_transient_event(current_time)

            # Set the arrival time to the current time
            transient_process.arrival_time = current_time

            # Immediately process the transient event before continuing
            if current_time < transient_process.arrival_time:
                current_time = transient_process.arrival_time

            print(
                f"Starting Transient Process {transient_process.pid} (Remaining: {transient_process.remaining_duration}) at time {current_time}")
            transient_process.completion_time = current_time + transient_process.duration
            transient_process.turnaround_time = calculate_turnaround_time(transient_process)
            transient_process.waiting_time = calculate_waiting_time(transient_process)

            # Update current time
            current_time = transient_process.completion_time
            print_process_info(transient_process)
            completed_processes.append(transient_process)

            # Mark the transient event as triggered
            transient_event_triggered = True

        # Get available processes at current time
        available_processes = [p for p in remaining_processes if p.arrival_time <= current_time]

        if not available_processes:
            # Jump to the next arrival time if no processes are available
            current_time = min(p.arrival_time for p in remaining_processes)
            continue

        # Select process with shortest remaining time from the available processes
        next_process = min(available_processes, key=lambda x: x.remaining_duration)

        print(
            f"Starting/Resuming Process {next_process.pid} (Remaining: {next_process.remaining_duration}) at time {current_time}")

        # Determine the time until the next process arrival
        next_arrival_time = float('inf')
        for p in remaining_processes:
            if p.arrival_time > current_time:
                next_arrival_time = min(next_arrival_time, p.arrival_time)

        # Determine how long this process will run
        if next_arrival_time != float('inf') and next_arrival_time < current_time + next_process.remaining_duration:
            # Process will be preempted by a new arrival
            time_slice = next_arrival_time - current_time
            next_process.remaining_duration -= time_slice
            current_time = next_arrival_time
            print(
                f"Process {next_process.pid} preempted at time {current_time}, remaining: {next_process.remaining_duration}")
        else:
            # Process will complete
            current_time += next_process.remaining_duration
            next_process.remaining_duration = 0
            next_process.completion_time = current_time
            next_process.turnaround_time = calculate_turnaround_time(next_process)
            next_process.waiting_time = calculate_waiting_time(next_process)

            # Print process info
            print_process_info(next_process)

            # Move process from remaining to completed
            remaining_processes.remove(next_process)
            completed_processes.append(next_process)

    print_algorithm_summary("SRTF", completed_processes)
    return completed_processes


# Round Robin Scheduling
def round_robin_scheduling(original_processes, time_quantum):
    # Create a copy of processes to avoid modifying the original list
    processes = [process.clone() for process in original_processes]

    print(f"\n--- Round Robin Scheduling (Time Quantum = {time_quantum}) ---")

    current_time = 0
    event_time = random.randint(5, 15)  # Set a single event time for this run
    transient_event_triggered = False

    # Sort processes by arrival time
    processes.sort(key=lambda x: x.arrival_time)

    # Create a ready queue
    ready_queue = []
    completed_processes = []
    remaining_processes = processes.copy()

    while remaining_processes or ready_queue:
        # Check if the transient event should be triggered (only once)
        if not transient_event_triggered and current_time >= event_time:
            # Create the transient event
            transient_process = create_transient_event(current_time)

            # Set the arrival time to the current time
            transient_process.arrival_time = current_time

            # Immediately process the transient event before continuing
            if current_time < transient_process.arrival_time:
                current_time = transient_process.arrival_time

            print(f"Starting Transient Process {transient_process.pid} at time {current_time}")
            transient_process.completion_time = current_time + transient_process.duration
            transient_process.turnaround_time = calculate_turnaround_time(transient_process)
            transient_process.waiting_time = calculate_waiting_time(transient_process)

            # Update current time
            current_time = transient_process.completion_time
            print_process_info(transient_process)
            completed_processes.append(transient_process)

            # Mark the transient event as triggered
            transient_event_triggered = True

        # Move arrived processes to the ready queue
        i = 0
        while i < len(remaining_processes):
            if remaining_processes[i].arrival_time <= current_time:
                process = remaining_processes.pop(i)
                ready_queue.append(process)
            else:
                i += 1

        # If ready queue is empty, jump to the next arrival time
        if not ready_queue and remaining_processes:
            current_time = min(p.arrival_time for p in remaining_processes)
            continue

        if ready_queue:
            # Get the next process from the ready queue
            current_process = ready_queue.pop(0)

            print(
                f"Starting/Resuming Process {current_process.pid} at time {current_time} (Remaining: {current_process.remaining_duration})")

            # Normal process scheduling using time quantum
            if current_process.remaining_duration <= time_quantum:
                # Process will complete within this time quantum
                time_slice = current_process.remaining_duration
                current_process.remaining_duration = 0
                current_process.completion_time = current_time + time_slice
                current_process.turnaround_time = calculate_turnaround_time(current_process)
                current_process.waiting_time = calculate_waiting_time(current_process)

                # Print process info
                print_process_info(current_process)

                # Add to completed processes
                completed_processes.append(current_process)
            else:
                # Process will use the full time quantum
                time_slice = time_quantum
                current_process.remaining_duration -= time_quantum

                print(
                    f"Process {current_process.pid} used its time quantum, remaining: {current_process.remaining_duration}")

                # Update current time before adding back to ready queue
                current_time += time_slice

                # Add back to ready queue
                ready_queue.append(current_process)
                continue  # Skip the time update at the end since we already updated it

            # Update the current time
            current_time += time_slice

    print_algorithm_summary("Round Robin", completed_processes)
    return completed_processes