import time
import multiprocessing
import math


# VERIFICATION LOGIC Mapping to the real world workload


def verify_student_identity(student_id):
   
    computational_load = 5000
    hash_simulation = 0
    for i in range(computational_load):
        hash_simulation += math.sqrt(i)
    
    # Return a success status for the student ID
    return True


#SEQUENTIAL SYSTEM The Bottleneck

def run_sequential_verification(entry_queue):
 
    print(f"\n[!] Sequential System: One staff member is processing the line...")
    start_time = time.perf_counter()
    
    # process the student one of a time
    results = [verify_student_identity(student) for student in entry_queue]
    
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    return execution_time


# PARALLEL SYSTEM The Optimized System

def run_parallel_verification(entry_queue, active_staff_count):
    
    print(f"\n[*] Parallel System: {active_staff_count} staff members working concurrently...")
    start_time = time.perf_counter()
    
    # multiprocessing distribute the workload across CPU cores
    # partitions entry_queue into chunks for each staff member
    with multiprocessing.Pool(processes=active_staff_count) as verification_pool:
        results = verification_pool.map(verify_student_identity, entry_queue)
    
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    return execution_time


# here is the benchmark


if __name__ == "__main__":
    print("="*60)
    print("      STUDENT ID ENTRY VERIFICATION SIMULATOR")
    print("="*60)

    try:
        # user input or number of the students entry
        total_students = int(input("Enter the number of students in the queue: "))
        
        system_cores = multiprocessing.cpu_count()
        print(f"\nYour facility has {system_cores} CPU channels available.")
        active_staff = int(input("How many verification staff will work in parallel?: "))

        # this will generate unique student id
        student_id_list = list(range(100000, 100000 + total_students))

        # this will execute the sequential 
        time_sequential = run_sequential_verification(student_id_list)
        print(f">> Total Sequential Time: {time_sequential:.4f} seconds")

        # and this is parallel
        time_parallel = run_parallel_verification(student_id_list, active_staff)
        print(f">> Total Parallel Time:   {time_parallel:.4f} seconds")

        # calculation
        # Performance formula: Speedup = Sequential / Parallel
        speedup_ratio = time_sequential / time_parallel
        efficiency_percentage = (speedup_ratio / active_staff) * 100

        print("\n" + "="*45)
        print("           PERFORMANCE SUMMARY")
        print("="*45)
        print(f"Total Student ID's:     {total_students:,}")
        print(f"Parallel Staff Active:  {active_staff}")
        print(f"Sequential Execution:   {time_sequential:.4f}s")
        print(f"Parallel Execution:     {time_parallel:.4f}s")
        print("-" * 45)
        print(f"SYSTEM SPEEDUP:         {speedup_ratio:.2f}x")
        print(f"STAFF EFFICIENCY:       {efficiency_percentage:.1f}%")
        print("="*45)

        
        if speedup_ratio < 1:
            print("\nNOTE: If the parallel is slower this is due to Orchestration Overhead.")
            print("Try increasing the student count to see the benefit of more staff.")
        else:
            print(f"\nSUCCESS: The parallel system reduced the bottleneck by {speedup_ratio:.2f}x.")

    except ValueError:
        print("\n[Input Error] Please provide valid integers for students and staff.")